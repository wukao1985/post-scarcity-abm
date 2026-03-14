"""Tests for PostLaborModel — validates V2-consistent behavior."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import numpy as np
import pytest
from models.pathway_a_abm.model import PostLaborModel, PostLaborAgent


class TestModelCreation:
    def test_creates_correct_number_of_agents(self):
        m = PostLaborModel(n_agents=50, seed=42)
        assert len(list(m.agents)) == 50

    def test_agent_profiles_distributed(self):
        m = PostLaborModel(n_agents=200, seed=42)
        profiles = [a.profile for a in m.agents]
        assert profiles.count("resilient") == 30   # 15%
        assert profiles.count("vulnerable") == 60  # 30%
        assert profiles.count("balanced") == 110   # 55%

    def test_initial_state_reasonable(self):
        m = PostLaborModel(n_agents=100, seed=42)
        for a in m.agents:
            assert 0 <= a.autonomy <= 1
            assert 0 <= a.competence <= 1
            assert 0 <= a.relatedness <= 1
            assert 0 <= a.status <= 1
            assert 0 <= a.meaning <= 1
            assert a.economic_role == 1.0
            assert a.archetype == "productive"

    def test_network_is_connected(self):
        m = PostLaborModel(n_agents=200, seed=42)
        for a in m.agents:
            neighbors = m.grid.get_neighbors(a.pos, include_center=False)
            assert len(neighbors) > 0


class TestModelDynamics:
    def test_runs_80_steps(self):
        m = PostLaborModel(n_agents=50, seed=42)
        for _ in range(80):
            m.step()
        df = m.datacollector.get_model_vars_dataframe()
        assert len(df) == 81  # initial + 80 steps

    def test_automation_ramps_up(self):
        m = PostLaborModel(n_agents=50, post_labor_fraction=0.8, seed=42)
        for _ in range(80):
            m.step()
        df = m.datacollector.get_model_vars_dataframe()
        # Should start at 0 and reach target
        assert df.iloc[0]["post_labor_current"] == 0.0
        assert df.iloc[-1]["post_labor_current"] == pytest.approx(0.8, abs=0.05)

    def test_no_automation_stays_healthy(self):
        """At 0% post-labor, meaning stays high and no sink."""
        m = PostLaborModel(n_agents=200, post_labor_fraction=0.0, seed=42)
        for _ in range(80):
            m.step()
        df = m.datacollector.get_model_vars_dataframe()
        final = df.iloc[-1]
        assert final["meaning_index"] > 0.55
        assert final["sink_index"] < 0.1

    def test_high_automation_causes_sink(self):
        """At 80% post-labor baseline, sink should be high."""
        m = PostLaborModel(n_agents=200, post_labor_fraction=0.8, seed=42)
        for _ in range(80):
            m.step()
        df = m.datacollector.get_model_vars_dataframe()
        final = df.iloc[-1]
        assert final["sink_index"] > 0.5  # should be ~0.8

    def test_meaning_bounded(self):
        m = PostLaborModel(n_agents=100, post_labor_fraction=0.9, seed=42)
        for _ in range(80):
            m.step()
        for a in m.agents:
            assert 0 <= a.meaning <= 1
            assert 0 <= a.autonomy <= 1
            assert 0 <= a.competence <= 1


class TestInterventions:
    def test_ubi_reduces_sink(self):
        """UBI should reduce sink relative to baseline."""
        results = {}
        for name, iv in [("baseline", {}), ("ubi", {"ubi": 0.7})]:
            sinks = []
            for seed in range(10):
                m = PostLaborModel(n_agents=200, post_labor_fraction=0.8,
                                   intervention=iv, seed=seed)
                for _ in range(80):
                    m.step()
                df = m.datacollector.get_model_vars_dataframe()
                sinks.append(df.iloc[-1]["sink_index"])
            results[name] = np.mean(sinks)
        assert results["ubi"] < results["baseline"]

    def test_full_bundle_prevents_collapse(self):
        """Full bundle should prevent collapse even at 80%."""
        collapses = 0
        for seed in range(10):
            m = PostLaborModel(
                n_agents=200, post_labor_fraction=0.8,
                intervention={"ubi": 0.7, "roles": 0.6, "fairness": 0.7, "status_deconc": 0.5},
                seed=seed,
            )
            for _ in range(80):
                m.step()
            df = m.datacollector.get_model_vars_dataframe()
            if df.iloc[-1]["sink_index"] > 0.7:
                collapses += 1
        assert collapses == 0

    def test_intervention_ordering(self):
        """Full bundle > UBI only > baseline for meaning at 80%."""
        configs = [
            ("baseline", {}),
            ("ubi", {"ubi": 0.7}),
            ("full", {"ubi": 0.7, "roles": 0.6, "fairness": 0.7, "status_deconc": 0.5}),
        ]
        means = {}
        for name, iv in configs:
            vals = []
            for seed in range(10):
                m = PostLaborModel(n_agents=200, post_labor_fraction=0.8,
                                   intervention=iv, seed=seed)
                for _ in range(80):
                    m.step()
                df = m.datacollector.get_model_vars_dataframe()
                vals.append(df.iloc[-1]["meaning_index"])
            means[name] = np.mean(vals)
        assert means["full"] > means["ubi"] > means["baseline"]


class TestReproducibility:
    def test_same_seed_same_result(self):
        """Same seed should produce identical results."""
        results = []
        for _ in range(2):
            m = PostLaborModel(n_agents=100, post_labor_fraction=0.8, seed=42)
            for _ in range(40):
                m.step()
            df = m.datacollector.get_model_vars_dataframe()
            results.append(df.iloc[-1]["meaning_index"])
        assert results[0] == pytest.approx(results[1], abs=1e-10)

    def test_different_seeds_different_results(self):
        """Different seeds should produce different results."""
        results = []
        for seed in [42, 123]:
            m = PostLaborModel(n_agents=100, post_labor_fraction=0.8, seed=seed)
            for _ in range(40):
                m.step()
            df = m.datacollector.get_model_vars_dataframe()
            results.append(df.iloc[-1]["meaning_index"])
        assert results[0] != pytest.approx(results[1], abs=1e-6)

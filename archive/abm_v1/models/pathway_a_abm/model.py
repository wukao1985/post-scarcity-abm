"""
Post-Scarcity ABM — V5
Mesa 3.5+ compatible implementation.

V5 changes from V4:
- Separated income_support from role_access (FATAL 1 fix):
  UBI only provides income_support; roles provide role_access.
  Psychological state uses role_access for meaning channels.
- Added virtual_role decay when agent has real role access (MAJOR 4)
- Gated virtual benefits on engagement threshold (virtual_role > 0.1) (MAJOR 4)
- Initial archetype classification before data collection (MAJOR 5)
"""
import numpy as np
import random
import mesa
from mesa.space import NetworkGrid
from mesa.datacollection import DataCollector
import networkx as nx

# Virtual engagement must exceed this threshold before providing psychological benefits
VIRTUAL_ENGAGEMENT_THRESHOLD = 0.1
VIRTUAL_ROLE_DECAY_FACTOR = 0.95


class PostLaborAgent(mesa.Agent):
    def __init__(self, model, profile="balanced"):
        super().__init__(model)
        self.profile = profile

        # Profile parameters
        profiles = {
            "resilient":  {"resilience": 0.8, "social_capital": 0.7, "skill_transferability": 0.7},
            "balanced":   {"resilience": 0.5, "social_capital": 0.5, "skill_transferability": 0.5},
            "vulnerable": {"resilience": 0.2, "social_capital": 0.3, "skill_transferability": 0.3},
        }
        p = profiles[profile]
        self.resilience            = np.clip(p["resilience"] + np.random.normal(0, 0.05), 0, 1)
        self.social_capital        = np.clip(p["social_capital"] + np.random.normal(0, 0.05), 0, 1)
        self.skill_transferability = np.clip(p["skill_transferability"] + np.random.normal(0, 0.05), 0, 1)

        # Initial psychological state (centered, not high)
        self.autonomy    = np.clip(np.random.normal(0.55, 0.08), 0, 1)
        self.competence  = np.clip(np.random.normal(0.55, 0.08), 0, 1)
        self.relatedness = np.clip(np.random.normal(0.50, 0.08), 0, 1)
        self.status      = np.clip(np.random.normal(0.50, 0.08), 0, 1)

        # Role and behavior
        self.role_access     = 1.0   # meaning-generating role participation
        self.income_support  = 1.0   # economic security (UBI, fairness)
        self.economic_role   = 1.0   # backward-compatible alias for role participation
        self.is_displaced    = False
        self.virtual_role    = 0.0
        self.archetype       = "productive"
        self.birth_intention = 0.7

        self.meaning = self._compute_meaning()

    def _effective_virtual_engagement(self):
        if self.virtual_role <= VIRTUAL_ENGAGEMENT_THRESHOLD:
            return 0.0
        return self.virtual_role

    def _compute_meaning(self):
        ew = self.model.economic_weight if hasattr(self, 'model') and self.model else 0.8
        vw = self.model.virtual_weight if hasattr(self, 'model') and self.model else 0.1
        effective_vr = self._effective_virtual_engagement()
        contribution = self.role_access * ew + effective_vr * vw
        return np.clip(
            0.25 * self.autonomy +
            0.25 * self.competence +
            0.25 * self.relatedness +
            0.10 * self.status +
            0.15 * contribution,
            0, 1)

    def _classify_archetype(self):
        aggression_drive = (1 - self.meaning) * (1 - self.social_capital) * 0.5
        if self.meaning > 0.55:
            self.archetype = "productive"
        elif aggression_drive > 0.3 and self.meaning < 0.40:
            self.archetype = "aggressor"
        elif self.meaning > 0.42:
            self.archetype = "beautiful_one"
        elif self.meaning > 0.30:
            self.archetype = "withdrawn"
        else:
            self.archetype = "collapsed"

    def _get_neighbors_state(self):
        neighbors = self.model.grid.get_neighbors(self.pos, include_center=False)
        if not neighbors:
            return {"aggressor_frac": 0.0, "collapsed_frac": 0.0,
                    "withdrawn_frac": 0.0, "mean_meaning": 0.5}
        archetypes = [n.archetype for n in neighbors]
        meanings   = [n.meaning   for n in neighbors]
        n = len(archetypes)
        return {
            "aggressor_frac": archetypes.count("aggressor") / n,
            "collapsed_frac": archetypes.count("collapsed") / n,
            "withdrawn_frac": archetypes.count("withdrawn") / n,
            "mean_meaning":   np.mean(meanings),
        }

    def step(self):
        ns = self._get_neighbors_state()
        m  = self.model

        # Per-step agent-level shock (models life events, idiosyncratic variation)
        agent_shock = np.random.normal(0, 0.03)

        # Contagion effects (negative social exposure)
        sink_exposure = ns["aggressor_frac"] + ns["collapsed_frac"] + ns["withdrawn_frac"]
        contagion = sink_exposure * m.contagion_strength

        # Status gap (inequality effect — driven by income, not role meaning)
        status_gap = np.clip(m.inequality_index * (1 - self.income_support), 0, 1)

        # Mean-reverting dynamics: state decays toward a target determined by conditions
        decay = self.model.decay  # how fast state adjusts toward target

        # Baseline human needs floor (even displaced people retain some base function)
        base = 0.32

        # Noise σ = 0.08 (V4: increased from 0.02 for realistic between-run variance)
        noise_sigma = 0.08

        # Gate virtual benefits on engagement threshold (MAJOR 4)
        effective_vr = self._effective_virtual_engagement()
        virtual_world_bonus = m.virtual_world_quality if effective_vr > 0 else 0.0

        # Autonomy target depends on role access, income support, fairness, resilience
        autonomy_target = base + (
            0.25 * self.role_access
            + 0.10 * effective_vr
            + 0.10 * m.fairness
            + 0.12 * self.resilience
            - 0.06 * status_gap
            - 0.05 * contagion
        )
        self.autonomy = np.clip(
            self.autonomy + decay * (autonomy_target - self.autonomy)
            + np.random.normal(0, noise_sigma) + agent_shock,
            0, 1)

        # Competence target
        roles_comp = 0.10 * m.roles_program if m.roles_competence_boost else 0.0
        competence_target = base + (
            0.25 * self.role_access
            + 0.10 * effective_vr * virtual_world_bonus
            + 0.12 * self.skill_transferability
            + roles_comp
            - 0.05 * contagion
        )
        self.competence = np.clip(
            self.competence + decay * (competence_target - self.competence)
            + np.random.normal(0, noise_sigma) + agent_shock,
            0, 1)

        # Relatedness target
        relatedness_target = base + (
            0.18 * self.social_capital
            + 0.10 * m.collectivism_index
            + 0.10 * self.role_access
            + 0.05 * effective_vr
            + 0.08 * m.fairness
            - 0.12 * ns["aggressor_frac"]
            - 0.05 * contagion
        )
        self.relatedness = np.clip(
            self.relatedness + decay * (relatedness_target - self.relatedness)
            + np.random.normal(0, noise_sigma) + agent_shock,
            0, 1)

        # Status target
        status_target = base + (
            0.25 * self.role_access
            + 0.10 * m.fairness
            + 0.08 * self.relatedness
            - 0.12 * m.status_concentration * (1 - self.role_access)
            - 0.04 * contagion
        )
        self.status = np.clip(
            self.status + decay * (status_target - self.status)
            + np.random.normal(0, noise_sigma) + agent_shock,
            0, 1)

        # Virtual role access (endogenous search by displaced workers)
        if self.is_displaced:
            self.virtual_role = np.clip(
                self.virtual_role + 0.05 * m.virtual_world_quality,
                0, m.virtual_world_quality)
        else:
            # Real-world role access crowds out virtual engagement over time.
            self.virtual_role = np.clip(
                self.virtual_role * VIRTUAL_ROLE_DECAY_FACTOR, 0, 1)

        # Recompute meaning (gate on engagement threshold)
        effective_vr = self._effective_virtual_engagement()
        contribution = self.role_access * m.economic_weight + effective_vr * m.virtual_weight
        self.meaning = np.clip(
            0.25 * self.autonomy +
            0.25 * self.competence +
            0.25 * self.relatedness +
            0.10 * self.status +
            0.15 * contribution
            - contagion * 0.08
            + 0.08 * self.resilience,
            0, 1)

        # Archetype classification
        self._classify_archetype()

        # Birth intention
        self.birth_intention = np.clip(
            0.4 * self.relatedness +
            0.3 * self.meaning +
            0.3 * self.autonomy
            - 0.2 * (1 - self.role_access),
            0, 1)


class PostLaborModel(mesa.Model):
    def __init__(self, n_agents=200, post_labor_fraction=0.5,
                 automation_speed=0.03, virtual_world_quality=0.0,
                 collectivism_index=0.3, contagion_strength=0.5,
                 intervention=None, seed=None,
                 economic_weight=0.8, virtual_weight=0.1,
                 ubi_strength=0.30, roles_strength=0.35,
                 roles_competence_boost=True, decay=0.08):
        super().__init__(seed=seed)
        if seed is not None:
            np.random.seed(seed)
            random.seed(seed)

        self.n_agents              = n_agents
        self.target_post_labor     = post_labor_fraction
        self.current_post_labor    = 0.0
        self.automation_speed      = automation_speed
        self.virtual_world_quality = virtual_world_quality
        self.collectivism_index    = collectivism_index
        self.contagion_strength    = contagion_strength

        # Ablation parameters (defaults preserve current behavior)
        self.economic_weight       = economic_weight
        self.virtual_weight        = virtual_weight
        self.ubi_strength          = ubi_strength
        self.roles_strength        = roles_strength
        self.roles_competence_boost = roles_competence_boost
        self.decay                 = decay

        # Intervention params
        iv = intervention or {}
        self.ubi               = iv.get("ubi", 0.0)
        self.roles_program     = iv.get("roles", 0.0)
        self.fairness          = iv.get("fairness", 0.1) + self.ubi * 0.3
        self.status_concentration = 1.0 - iv.get("status_deconc", 0.0) * 0.5
        self.inequality_index  = np.clip(1.0 - self.fairness, 0, 1)
        self._did_precollect_archetype_sync = False

        # Network (small-world, Watts-Strogatz)
        G = nx.watts_strogatz_graph(n_agents, 6, 0.1, seed=seed)
        self.grid = NetworkGrid(G)

        # Create agents with profile distribution (15% resilient, 55% balanced, 30% vulnerable)
        n_res = int(n_agents * 0.15)
        n_vul = int(n_agents * 0.30)
        n_bal = n_agents - n_res - n_vul
        profiles = ["resilient"] * n_res + ["balanced"] * n_bal + ["vulnerable"] * n_vul
        random.shuffle(profiles)
        for i, node in enumerate(G.nodes()):
            profile = profiles[i % len(profiles)]
            agent = PostLaborAgent(self, profile=profile)
            self.grid.place_agent(agent, node)

        # Initial classification pass before data collection
        self._classify_all_archetypes()

        # Data collector
        self.datacollector = DataCollector(
            model_reporters={
                "meaning_index":     lambda m: np.mean([a.meaning for a in m.agents]),
                "sink_index":        lambda m: np.mean([
                    1 if a.archetype in ("aggressor", "withdrawn", "collapsed") else 0
                    for a in m.agents]),
                "productive_frac":   lambda m: np.mean([1 if a.archetype == "productive"     else 0 for a in m.agents]),
                "beautiful_one_frac":lambda m: np.mean([1 if a.archetype == "beautiful_one"  else 0 for a in m.agents]),
                "aggressor_frac":    lambda m: np.mean([1 if a.archetype == "aggressor"       else 0 for a in m.agents]),
                "withdrawn_frac":    lambda m: np.mean([1 if a.archetype == "withdrawn"       else 0 for a in m.agents]),
                "collapsed_frac":    lambda m: np.mean([1 if a.archetype == "collapsed"       else 0 for a in m.agents]),
                "birth_intention":   lambda m: np.mean([a.birth_intention for a in m.agents]),
                "social_trust":      lambda m: np.mean([a.relatedness     for a in m.agents]),
                "post_labor_current":lambda m: m.current_post_labor,
                "band_occupancy":    lambda m: sum(1 for a in m.agents if 0.35 <= a.meaning <= 0.65) / m.n_agents,
            }
        )
        self.datacollector.collect(self)

    def _classify_all_archetypes(self):
        for agent in self.agents:
            agent._classify_archetype()

    def step(self):
        # Advance automation
        if self.current_post_labor < self.target_post_labor:
            self.current_post_labor = min(
                self.current_post_labor + self.automation_speed,
                self.target_post_labor)

        # Assign economic roles based on current automation level
        agent_list = list(self.agents)
        n_displaced = int(self.current_post_labor * self.n_agents)
        if n_displaced > 0:
            displaced = random.sample(agent_list, min(n_displaced, len(agent_list)))
            displaced_ids = set(a.unique_id for a in displaced)
        else:
            displaced_ids = set()

        for a in agent_list:
            a.is_displaced = a.unique_id in displaced_ids
            if a.is_displaced:
                # UBI provides income support only (fairness/economic buffer)
                # Roles provide role access (meaning-generating participation)
                a.income_support = self.ubi * self.ubi_strength
                a.role_access    = self.roles_program * self.roles_strength
            else:
                a.income_support = 1.0
                a.role_access    = 1.0

            # Backward-compatible field tracks role participation only; UBI lives in income_support.
            a.economic_role = a.role_access

        # Step all agents in random order
        self.agents.shuffle_do("step")
        if not self._did_precollect_archetype_sync:
            self._classify_all_archetypes()
            self._did_precollect_archetype_sync = True
        self.datacollector.collect(self)

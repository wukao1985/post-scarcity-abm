PYTHON = .venv/bin/python

.PHONY: sweep1 sweep2 sweep3 sweep4 sweep5 sweep6 all-sweeps figures test clean-data

sweep1:
	$(PYTHON) models/pathway_a_abm/runner.py 1

sweep2:
	$(PYTHON) models/pathway_a_abm/runner.py 2

sweep3:
	$(PYTHON) models/pathway_a_abm/runner.py 3

sweep4:
	$(PYTHON) models/pathway_a_abm/runner.py 4

sweep5:
	$(PYTHON) models/pathway_a_abm/runner.py 5

sweep6:
	$(PYTHON) models/pathway_a_abm/runner.py 6

all-sweeps: sweep1 sweep2 sweep3 sweep4 sweep5 sweep6

figures:
	$(PYTHON) scripts/sweep2_figures.py
	$(PYTHON) scripts/sweep3_figures.py
	$(PYTHON) scripts/sweep4_figures.py
	$(PYTHON) scripts/sweep5_figures.py
	$(PYTHON) scripts/sweep6_figures.py

test:
	$(PYTHON) -m pytest tests/ -v

clean-data:
	rm -f data/simulation/sweep*.csv

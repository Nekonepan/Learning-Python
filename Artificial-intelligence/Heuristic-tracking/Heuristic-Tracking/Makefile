PYTHON ?= python
THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
ROOT_DIR := $(abspath $(THIS_DIR)..)
VENV := $(ROOT_DIR)/.venv
VENV_PYTHON := $(VENV)/bin/python
WHEEL := $(ROOT_DIR)/ai_pkg-0.1-py3-none-any.whl
SCRIPT := $(THIS_DIR)heuristic-tracking.py

.PHONY: run clean-venv

run:
	@if $(PYTHON) -c "import ai_pkg" >/dev/null 2>&1; then \
		echo "Using system Python: $(PYTHON)"; \
		$(PYTHON) $(SCRIPT); \
	else \
		echo "ai_pkg is not installed for system Python. Trying system pip..."; \
		if $(PYTHON) -m pip install $(WHEEL) >/dev/null 2>&1 && $(PYTHON) -c "import ai_pkg" >/dev/null 2>&1; then \
			echo "Installed ai_pkg for system Python."; \
			$(PYTHON) $(SCRIPT); \
		else \
			echo "System install unavailable. Using local virtual environment."; \
			test -x $(VENV_PYTHON) || $(PYTHON) -m venv $(VENV); \
			if ! $(VENV_PYTHON) -c "import ai_pkg" >/dev/null 2>&1; then \
				$(VENV_PYTHON) -m pip install $(WHEEL); \
			fi; \
			$(VENV_PYTHON) $(SCRIPT); \
		fi \
	fi

clean-venv:
	rm -rf $(VENV)

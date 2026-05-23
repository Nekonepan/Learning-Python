PYTHON ?= python
THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
ROOT_DIR := $(abspath $(THIS_DIR)..)
VENV := $(ROOT_DIR)/.venv
VENV_PYTHON := $(VENV)/bin/python
WHEEL := $(ROOT_DIR)/ai_pkg-0.0.1-py3-none-any.whl
SCRIPT := $(THIS_DIR)Knowledge-representation.py
REQUIRED_IMPORTS := import ai_pkg, numpy

.PHONY: run clean-venv

run:
	@if $(PYTHON) -c "$(REQUIRED_IMPORTS)" >/dev/null 2>&1; then \
		echo "Using system Python: $(PYTHON)"; \
		$(PYTHON) $(SCRIPT); \
	else \
		echo "Required packages are not installed for system Python. Trying system pip..."; \
		if $(PYTHON) -m pip install numpy $(WHEEL) >/dev/null 2>&1 && $(PYTHON) -c "$(REQUIRED_IMPORTS)" >/dev/null 2>&1; then \
			echo "Installed required packages for system Python."; \
			$(PYTHON) $(SCRIPT); \
		else \
			echo "System install unavailable. Using local virtual environment."; \
			test -x $(VENV_PYTHON) || $(PYTHON) -m venv $(VENV); \
			if ! $(VENV_PYTHON) -c "$(REQUIRED_IMPORTS)" >/dev/null 2>&1; then \
				$(VENV_PYTHON) -m pip install numpy $(WHEEL); \
			fi; \
			$(VENV_PYTHON) $(SCRIPT); \
		fi \
	fi

clean-venv:
	rm -rf $(VENV)

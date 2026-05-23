PYTHON ?= $(shell command -v python3 2>/dev/null || command -v python 2>/dev/null)
THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
ROOT_DIR := $(abspath $(THIS_DIR)..)
VENV := $(ROOT_DIR)/.venv
VENV_PYTHON := $(VENV)/bin/python
WHEEL := $(ROOT_DIR)/ai_pkg-0.0.1-py3-none-any.whl
SCRIPT := $(THIS_DIR)post.py
REQUIRED_IMPORTS := import ai_pkg, numpy

.PHONY: run clean-venv

run:
	@if [ -z "$(PYTHON)" ]; then \
		echo "Python was not found. Install python3 and python3-venv, then run make again."; \
		exit 127; \
	fi; \
	if "$(PYTHON)" -c "$(REQUIRED_IMPORTS)" >/dev/null 2>&1; then \
		echo "Using system Python: $(PYTHON)"; \
		"$(PYTHON)" $(SCRIPT); \
	else \
		echo "Required packages are not installed for system Python. Trying system pip..."; \
		if "$(PYTHON)" -m pip install numpy $(WHEEL) >/dev/null 2>&1 && "$(PYTHON)" -c "$(REQUIRED_IMPORTS)" >/dev/null 2>&1; then \
			echo "Installed required packages for system Python."; \
			"$(PYTHON)" $(SCRIPT); \
		else \
			echo "System install unavailable. Using local virtual environment."; \
			if [ ! -x $(VENV_PYTHON) ]; then \
				"$(PYTHON)" -m venv $(VENV) || { \
					echo "Could not create virtual environment. On Debian/Ubuntu/Mint, install python3-venv."; \
					exit 1; \
				}; \
			fi; \
			if ! $(VENV_PYTHON) -c "$(REQUIRED_IMPORTS)" >/dev/null 2>&1; then \
				$(VENV_PYTHON) -m pip install numpy $(WHEEL); \
			fi; \
			$(VENV_PYTHON) $(SCRIPT); \
		fi \
	fi

clean-venv:
	rm -rf $(VENV)

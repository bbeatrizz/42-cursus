## VARIABLES GLOBALES

PYTHON = python3
PIP = pip3
SCRIPT = a_maze_ing.py
CONFIG = config.txt

# ====================

# REGLAS OBLIGATORIAS DEL SUBJECT

# 1. Instalar las dependencias necesarias para el linter y testing
install:
		$(PIP) install flake8 mypy
		$(PIP) install mazegen-1.0.0-py3-none-any.whl

# 2. Ejecución del programa principal pasando el arch. de config
run:
		$(PYTHON) $(SCRIPT) $(CONFIG)

# 3. Lanza el script en modo debug
debug: 
		$(PYTHON) -m pdb $(SCRIPT) $(CONFIG)

# 4. Limpia arch. temporales y caché
clean:
		rm -rf __pycache__
		rm -rf .mypy_cache
		rm -rf dist/
		rm -rf *.egg-info

# 5. Ejecución de prueba con flake y sus flags (validación)
lint: 
		flake8 .
		mypy --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs .

# 6. Ejecución de validación más estricta (esto se puede quitar, pero por si buscan cosquillas)
lint-strict:
		flake8 .
		mypy --strict .


# meli-challenger-mutant
Proyecto de evaluación propuesto por Mercado Libre

## Introduction
meli-challenger-mutant comprende las funcionalidades y microservicios para el procesamiento y disponibilizacion de estadistica de secuencias de ADN en relación a su origen humano o mutante.

## Getting Started
1.	Installation process
```bash
pip3 install virtualenv
virtualenv env --python=python3.8
. env/bin/activate
source env/bin/activate
pip3 install -r requirements/development.txt
pip3 install -r requirements/test.txt

# to deactivate venv
deactivate
```
### Run

```bash
python3 main.py runserver
```

## Build and Test
pytest -vs test
pytest -v --cov src --cov-report html test
pytest -v --cov src --cov-report html --cov-config=.coveragerc test
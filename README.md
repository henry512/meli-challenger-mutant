# meli-challenger-mutant
Proyecto de evaluación propuesto por Mercado Libre

## Introduction
meli-challenger-mutant comprende las funcionalidades y microservicios para el procesamiento y disponibilizacion de estadistica de secuencias de ADN en relación a su origen humano o mutante.
### docs references
source = ./docs/**
  Diagrama arquitectura meli-mutants.png
  Diagrama despliegue meli-mutants.png
  Documento despliegue meli-mutants.docx
  Examen Mercadolibre - Mutantes.pdf
  coverage-report meli-mutants.png
  meli-mutants.postman_collection.json
and other files docs...

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
### Run Test
```bash
pytest -vs test
```
### Run Test and Coverage
```bash
pytest -v --cov src --cov-report html test
```
### Run Test and Coverage include file .coveragerc
```bash
pytest -v --cov src --cov-report html --cov-config=.coveragerc test
```

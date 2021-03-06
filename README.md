# meli-challenger-mutant
![image](https://user-images.githubusercontent.com/34389493/148126967-21fe6558-ecab-41d9-844a-af73d38b32ec.png)

Proyecto de evaluación propuesto por Mercado Libre para la ocupación del puesto Sr. Development Analyst. #Meli #meli #ADNMeli #MercadoLibre

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
![image](https://user-images.githubusercontent.com/34389493/148126158-15fc7dcc-c3cc-47a5-9384-2932c45b0d37.png)
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

## Arquitecture and other docs
![image](https://user-images.githubusercontent.com/34389493/148126061-029386be-afc8-4644-a3c8-84b1b5baeb96.png)
![image](https://user-images.githubusercontent.com/34389493/148126104-ee0ad57c-376c-4ee2-aecb-52441675883f.png)

### Endpoints Collections
#### Postman: ./docs/meli-mutants.postman_collection.json
#### Swagger: ./src/infrastructure/swagger.yml  or  http://ec2-18-228-175-124.sa-east-1.compute.amazonaws.com:5000/ws-doc/


import flask
import pytest
from unittest.mock import MagicMock, Mock
from src.controllers import mutant, stats
from src.services import IMutantService
from src.domains import DNAStatisticsDto
import json


with open('test/mocks/data_dna.json', 'r') as file:
    dna_mock_data = json.load(file)

data_mutants = [
    value for value in dna_mock_data["mutants"]
]
data_humans = [
    value for value in dna_mock_data["humans"]
]
dna_sequence_exception = [
    value for value in dna_mock_data["dna_sequence_exception"]
]
dna_sequence_value_exception = [
    value for value in dna_mock_data["dna_sequence_value_exception"]
]
dna_type_exception = [
    value for value in dna_mock_data["dna_type_exception"]
]


app = flask.Flask(__name__)

def test_stats():
    with app.app_context():
        result = stats(mock_services_mutants())
        assert result[1] == 200


@pytest.mark.parametrize("data", data_mutants)
def test_is_mutant(data):
    with app.app_context():
        result = mutant(mock_services_mutants(), {"dna": data})
        assert result[1] == 200


@pytest.mark.parametrize("data", data_humans)
def test_is_human(data):
    with app.app_context():
        result = mutant(mock_services_mutants(), {"dna": data})
        assert result[1] == 403


@pytest.mark.parametrize("data", dna_sequence_exception)
def test_dna_sequence_exception_is_bad_request(data):
    with app.app_context():
        result = mutant(mock_services_mutants(), {"dna": data})
        assert result[1] == 400


@pytest.mark.parametrize("data", dna_sequence_value_exception)
def test_dna_sequence_value_exception_is_bad_request(data):
    with app.app_context():
        result = mutant(mock_services_mutants(), {"dna": data})
        assert result[1] == 400
    

@pytest.mark.parametrize("data", dna_type_exception)
def test_dna_type_exception_is_bad_request(data):
    with app.app_context():
        result = mutant(mock_services_mutants(), {"dna": data})
        assert result[1] == 400


# Factories Dependencies
def mock_services_mutants():
    service = MagicMock(IMutantService)
    service.save_dna = Mock(return_value=None)
    service.get_statistics = Mock(
        return_value=DNAStatisticsDto(count_human_dna=100, count_mutant_dna=40, ratio=0.4)
    )
    return service

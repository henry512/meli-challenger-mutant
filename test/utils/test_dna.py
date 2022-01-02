import pytest
from src.utils import DNA
from src.exceptions import (
    DNASequenceException, DNASequenceValuesException, DNAParametersTypeException
)
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


@pytest.mark.parametrize("data", data_mutants)
def test_dna_is_mutant(data):
    dna = DNA(data)
    assert dna.is_mutant() == True, "ADN deberia ser mutante"


@pytest.mark.parametrize("data", data_humans)
def test_dna_is_human(data):
    dna = DNA(data)
    assert dna.is_mutant() == False, "ADN deberia ser humano"


@pytest.mark.parametrize("data", dna_sequence_exception)
def test_dna_sequence_exception(data):
    with pytest.raises(DNASequenceException):
        DNA(data).is_mutant()


@pytest.mark.parametrize("data", dna_sequence_value_exception)
def test_dna_sequence_exception(data):
    with pytest.raises(DNASequenceValuesException):
        DNA(data).is_mutant()


@pytest.mark.parametrize("data", dna_type_exception)
def test_dna_sequence_exception(data):
    with pytest.raises(DNAParametersTypeException):
        DNA(data)

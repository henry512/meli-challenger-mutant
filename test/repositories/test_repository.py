from unittest.mock import MagicMock, Mock
from pandas.core.frame import DataFrame
from src.repositories import MutantRepository
from src.infrastructure import IPostgresContext
from src.config import IConfiguration
from src.domains import DNAEntity, DNAOriginEnum
from psycopg2.errors import UniqueViolation


def test_save_dna():
    context = mock_context()
    configuration = mock_configuration()
    repository = MutantRepository(context, configuration)
    repository.save_dna(
        DNAEntity(
            origin=DNAOriginEnum["MUTANT"], 
            sequence=["CTGGCC", "TATACC", "TCGGTG", "TTAATG", "TCATTT", "AGCTTG"]
        )
    )


def test_save_dna_unique_constrains_exception():
    def side_effect(*args, **kwargs):
        raise UniqueViolation("mock raises")
    context = mock_context(side_effect)
    configuration = mock_configuration()
    repository = MutantRepository(context, configuration)
    repository.save_dna(
        DNAEntity(
            origin=DNAOriginEnum["MUTANT"], 
            sequence=["CTGGCC", "TATACC", "TCGGTG", "TTAATG", "TCATTT", "AGCTTG"]
        )
    )


def test_get_statistics():
    mock_data = DataFrame([(100, "HUMAN"), (40, "MUTANT")], columns=["count_dna", "origin"])
    context = mock_context(mock_data)
    configuration = mock_configuration()
    repository = MutantRepository(context, configuration)
    result = repository.get_statistics()
    assert isinstance(result, dict) and len(result) > 0
    assert result["ratio"] == 0.4


def test_get_statistics_zero_division():
    mock_data = DataFrame([(0, "HUMAN"), (0, "MUTANT")], columns=["count_dna", "origin"])
    context = mock_context(mock_data)
    configuration = mock_configuration()
    repository = MutantRepository(context, configuration)
    result = repository.get_statistics()
    assert isinstance(result, dict) and len(result) > 0
    assert result["ratio"] == 0.0



# Factories Dependencies
def mock_context(side_effect = None):
    mock = MagicMock(IPostgresContext)
    if side_effect is not None:
        if callable(side_effect):
            mock.execute_query = Mock(side_effect=side_effect)
        else:
            mock.execute_query = Mock(return_value=side_effect)
        mock.find = Mock(return_value=side_effect)
    else:
        mock.find = Mock(return_value=DataFrame)
        mock.execute_query = Mock(return_value=None)
    
    return mock


def mock_configuration():
    mock = MagicMock(IConfiguration)
    mock.config = { 
        "DATABASE_TABLE_DNA": "mock_table"
    }
    return mock

import flask
from unittest.mock import MagicMock, Mock
from src.repositories import IMutantRepository
from src.services import MutantService
from src.domains import DNAStatisticsDto, DNAEntity, DNAOriginEnum


app = flask.Flask(__name__)

def test_save_dna():
    service = MutantService(mock_repository_mutants())
    service.save_dna(
        DNAEntity(
            origin=DNAOriginEnum["MUTANT"], 
            sequence=["CTGGCC", "TATACC", "TCGGTG", "TTAATG", "TCATTT", "AGCTTG"]
        )
    )


def test_get_statistics():
    service = MutantService(mock_repository_mutants())
    result = service.get_statistics()
    assert isinstance(result, dict) and len(result) > 0


# Factories Dependencies
def mock_repository_mutants(side_effect_exception=None):
    mock = MagicMock(IMutantRepository)
    if side_effect_exception:
        mock.save_dna = Mock(return_value=side_effect_exception)
    else:
        mock.save_dna = Mock(return_value=None)
    mock.get_statistics = Mock(
        return_value={
            "mutant": 0,
            "human": 0,
            "ratio": 0.0
        }
    )
    return mock

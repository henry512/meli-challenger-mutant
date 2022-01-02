from injector import inject
from src.domains import DNAEntity, DNAOriginEnum
from src.services import IMutantService
from flask import jsonify
from src.utils import DNA
from src.exceptions import (
    DNASequenceValuesException, DNASequenceException, DNAParametersTypeException
)


@inject
def mutant(service: IMutantService, query):
    dna = query["dna"]
    try:
        result_dna = DNA(dna).is_mutant()
    except (DNASequenceValuesException, DNASequenceException, DNAParametersTypeException) as error:
        return jsonify(str(error)), 400
    
    if result_dna:
        service.save_dna(DNAEntity(sequence=dna, origin=DNAOriginEnum.MUTANT))
        return jsonify(None), 200
    
    service.save_dna(DNAEntity(sequence=dna, origin=DNAOriginEnum.HUMAN))
    return jsonify(None), 403


@inject
def stats(service: IMutantService):
    return jsonify(service.get_statistics()), 200

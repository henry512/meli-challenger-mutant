from injector import inject
from src.domains import DNAEntity, DNAOriginEnum
from src.services import IMutantService
from flask import jsonify
from src.utils import DNA
from src.exceptions import DNASequenceValuesException, DNASequenceException


@inject
def mutant(service: IMutantService, query):
    dna = query["dna"]
    try:
        result_dna = DNA(dna).is_mutant()
    except (DNASequenceValuesException, DNASequenceException) as error:
        return jsonify(str(error)), 400
    
    if result_dna:
        service.save_dna(DNAEntity(sequence=dna, origin=DNAOriginEnum.MUTANT))
        return None, 200
    
    service.save_dna(DNAEntity(sequence=dna, origin=DNAOriginEnum.HUMAN))
    return None, 403


@inject
def stats(service: IMutantService):
    return jsonify(service.get_statistics()), 200

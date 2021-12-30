from injector import inject
from src.domains import DNAEntity
from src.domains import DNAOriginEnum
from src.services import IMutantService
from flask import jsonify


@inject
def mutant(service: IMutantService):
    print(service.get_dna("key"))
    service.save_dna(DNAEntity(sequence=["ADN"], origin=DNAOriginEnum.HUMAN))
    return jsonify(True), 200


@inject
def stats(service: IMutantService):
    statistics = service.get_statistics()
    return jsonify(statistics), 200

from injector import Binder, singleton
from src.repositories import IMutantRepository, MutantRepository
from src.config import IConfiguration, Configuration
from src.services import IMutantService, MutantService

def container(binder: Binder):
    binder.bind(
        IMutantRepository,
        to=MutantRepository,
        scope=singleton,
    )
    binder.bind(
        IMutantService,
        to=MutantService,
        scope=singleton,
    )
    binder.bind(
        IConfiguration,
        to=Configuration,
        scope=singleton,
    )

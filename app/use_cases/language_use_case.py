from typing import List
from app.interfaces.language_repository_interface import LanguageRepositoryInterface
from app.entities.language_entity import LanguageEntity

class LanguageUseCase:
    def __init__(self, language_repository: LanguageRepositoryInterface):
        self.language_repository = language_repository
        
    def get_all_languages(self) -> List[LanguageEntity]:
        return self.language_repository.get_all_languages()
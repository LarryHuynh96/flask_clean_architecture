from typing import List
from app.interfaces.language_framework_repository_interface import LanguageFrameworkRepositoryInterface
from app.entities.language_framework_entity import LanguageFrameworkEntity

class LanguageFrameworkController:
    def __init__(self, language_framework_repository: LanguageFrameworkRepositoryInterface):
        self.language_framework_repository = language_framework_repository

    def get_frameworks_by_language_id(self, language_id: str) -> List[LanguageFrameworkEntity]:
        return self.language_framework_repository.get_frameworks_by_language_id(language_id)

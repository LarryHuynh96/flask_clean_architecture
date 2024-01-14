from abc import ABC, abstractmethod
from typing import List
from app.entities.language_entity import LanguageEntity

class LanguageRepositoryInterface(ABC):
    @abstractmethod
    def get_all_languages(self) -> List[LanguageEntity]:
        pass


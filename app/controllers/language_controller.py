from flask import jsonify
from app.use_cases.language_use_case import LanguageUseCase

class LanguageController:
    def __init__(self, language_use_case: LanguageUseCase):
        self.language_use_case = language_use_case

    def get_all_languages(self):
        try:
            languages = self.language_use_case.get_all_languages()
            return jsonify([language.to_dict() for language in languages])
        except Exception as e:
            return jsonify({'error': str(e)}), 500

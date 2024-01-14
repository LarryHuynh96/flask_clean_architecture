from app.entities.language_entity import LanguageEntity
from app.interfaces.language_repository_interface import LanguageRepositoryInterface
from app.database.models import LanguageTable
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class LanguageAdapter(LanguageRepositoryInterface):
    def __init__(self, engine):
        # if engine is None:
        #     self.engine = create_engine('mysql://dev_user:dev_password@localhost/dev_database')
        # else:
        #     self.engine = engine
        self.engine = engine
        self.Session = sessionmaker(bind=self.engine)

    def get_all_languages(self):
        session = self.Session()
        try:
            languages = session.query(LanguageTable).all()
            return [LanguageEntity(id=language.id, name=language.name, status=language.status) for language in languages]
        except Exception as e:
            print(f"Error retrieving languages: {e}")
            return []
        finally:
            session.close()



from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class LanguageTable(db.Model):
    __tablename__ = 'language_table'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    status = db.Column(db.String)

    frameworks = db.relationship('LanguageFrameworkTable', back_populates='language')

class LanguageFrameworkTable(db.Model):
    __tablename__ = 'language_framework_table'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    language_id = db.Column(db.String, db.ForeignKey('language_table.id'))
    status = db.Column(db.String)

    language = db.relationship('LanguageTable', back_populates='frameworks')

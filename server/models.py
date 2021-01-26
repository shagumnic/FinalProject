"""Data model"""

from config import db, ma
#from sqlalchemy.dialects.postgresql import ARRAY

class Videogame(db.Model):
    __tablename__ = "VIDEOGAMES"
    steam_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    release_date = db.Column(db.String)
    languages_id = db.Column(db.String)
    genres_id = db.Column(db.String)


class Language(db.Model):
    __tablename__ ="LANGUAGES"
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String)
    
class Genre(db.Model):
    __tablename__="GENRES"
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String)


class VideogameSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Videogame
        load_instance = True
        sqla_session = db.session

class LanguageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Language
        load_instance = True
        sqla_session = db.session

class GenreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Genre
        load_instance = True
        sqla_session = db.session
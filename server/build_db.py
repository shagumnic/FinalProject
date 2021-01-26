"""Building the DB"""

import csv
import os
from config import db
from models import *
import urllib.parse

LANGUAGES = {'Arabic': 1, 'Bulgarian': 2, 'Simplified Chinese': 3, 'Czech': 4, "Danish": 5, "Dutch": 6, 
            'English': 7, 'Finnish': 8, 'French': 9, "German": 10, "Greek": 11,
            'Hungarian': 12, "Italian": 13, "Japanese": 14, "Korean": 15,
            "Norwegian": 16, "Polish": 17, "Portuguese": 18, "Portuguese - Brazil": 19,
            "Romanian": 20, "Russian": 21, "Spanish - Spain": 22, "Spanish - Latin America": 23,
            'Swedish': 24, "Thai": 25, "Turkish": 26, "Ukrainian": 27, "Vietnamese": 28,
            "Traditional Chinese": 29}

GENRES = {"Action": 1, "Adventure": 2, "Casual": 3, "Indie": 4,\
            "Massively Multiplayer": 5, "Racing": 6, "RPG": 7,
            "Simulation": 8, "Sports": 9, "Strategy": 10}
def build_db(filename):
    # Delete existing DB
    if os.path.exists(f"{filename}.sqlite3"):
        os.remove(f"{filename}.sqlite3")

    # Create DB Structure
    db.create_all()

    # Add data to the DB
    with open(f"{filename}.csv", encoding='utf-8') as f:
        content = csv.reader(f)
        next(content)
    
        for line in content:
            languages_list = line[4][1:len(line[4])-1].replace("'", "").split(', ')
            for index, language in enumerate(languages_list) :
                languages_list[index] = LANGUAGES[language]
            languages_string = str(languages_list)
            languages_string = languages_string[1:len(languages_string)-1]
            genres_list = line[2][1:len(line[2])-1].replace("'", "").split(', ')
            for index, genre in enumerate(genres_list) :
                genres_list[index] = GENRES[genre]
            genres_string = str(genres_list)
            genres_string = genres_string[1:len(genres_string)-1]
            videogame = Videogame(
                steam_id = line[0],
                name = line[1],
                release_date = line[3],
                languages_id = languages_string,
                genres_id = genres_string
            )

            db.session.add(videogame)
        for key in LANGUAGES :
            new_language = Language(id=LANGUAGES[key], language=key)
            db.session.add(new_language)
            
        for key in GENRES :
            new_genre = Genre(id=GENRES[key], genre=key)
            db.session.add(new_genre)    
        db.session.commit()


def main():
    build_db("video_games_data")

if __name__ == "__main__":
    main()
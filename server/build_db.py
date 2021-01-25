"""Building the DB"""

import csv
import os
from config import db
from models import Videogame, Language, Genre

LANGUAGES = {}
def build_db(filename):
    # Delete existing DB
    if os.path.exists(f"{filename}.sqlite3"):
        os.remove(f"{filename}.sqlite3")

    # Create DB Structure
    db.create_all()

    # Add data to the DB
    with open(f"{filename}.csv") as f:
        content = csv.reader(f)
        next(content)
    
        for line in content:
            videogame = Videogame(
                steamId = line[0],
                name = line[1],
                release_date = line[2]
                
            )

            db.session.add(videogame)
        db.session.commit()


def main():
    build_db("videogames")
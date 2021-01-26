import psycopg2
import os
import sqlite3
import json

this_dir = os.path.abspath(os.path.dirname(__file__))
name = 'grand'
name = '%' + name + '%'
#conn = psycopg2.connect("sqlite:///" + os.path.join(this_dir, "video_games_data.sqlite3"))
conn = sqlite3.connect('video_games_data.sqlite3')
cur = conn.cursor()
cur.execute("select * from VIDEOGAMES where name like ? limit 5", (name,))
rows = cur.fetchall()
return_json = {'results': []}
for row in rows: 
    lang_ids = row[3].split(", ")
    #langs = '(' + langs + ')'
    cur.execute('select language from LANGUAGES where id in (%s)' % ','.join('?'*len(lang_ids)), lang_ids)
    langs = cur.fetchall()
    langs = [x[0] for x in langs]
    genre_ids = row[4].split(", ")
    cur.execute('select language from LANGUAGES where id in (%s)' % ','.join('?'*len(genre_ids)), genre_ids)
    genres = cur.fetchall()
    genres = [x[0] for x in genres]
    result = {'steam_id': row[0], 'name': row[1], 'release_date': row[2], 'languages':langs, 'genres': genres}
    return_json['results'].append(result)
print(return_json)
results = json.dumps(return_json)
for result in results['results'] :
    print(result)

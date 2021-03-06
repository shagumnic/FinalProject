from flask import Flask, session, redirect, url_for, escape, request, render_template, jsonify
import os
from config import app, db
from models import *
from build_db import *
from csv import writer
import sqlite3
from flask_cors import CORS, cross_origin
import json

cors = CORS(app)

@app.route("/", methods=["GET", "POST"])
def main():
        return redirect(url_for('index'))


@app.route("/index", methods=["GET", "POST"])
def index():
        if request.method == "POST":
                if request.form.get("add") == "Add Game":
                        return redirect(url_for('add'))
                if request.form.get("listAll") == "List all":
                        return redirect(url_for('listAll'))
                if request.form.get("submit") == "Submit":
                        name = request.form['videogame']
                        conn = sqlite3.connect('video_games_data.sqlite3')
                        cur = conn.cursor()
                        cur.execute("select * from VIDEOGAMES where name like '%{}%'".format(name))
                        rows = cur.fetchall()
                        if name=="":
                                return render_template("index.html", message="Please enter a game")

                        results = data_cleaning(rows)
                        if results['results'] == []:
                                return render_template("index.html", message="No game found with that name")

                        return render_template("index.html", message=None, results=results['results'])


        return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add():
        if request.method == "POST":
                conn = sqlite3.connect('video_games_data.sqlite3')
                cur = conn.cursor()
                cur.execute("select * from VIDEOGAMES where steam_id=?", (request.form.get('steam_id'),))
                rows = cur.fetchall()
                if rows :
                        return render_template("add.html", message="The game's steam ID you're trying to add is already exists")
                language_ids = ", ".join(request.form.getlist('languages'))
                genre_ids = ", ".join(request.form.getlist('genres'))
                new_game = Videogame(
                        steam_id = request.form.get('steam_id'),
                        name = request.form.get('name'),
                        release_date = request.form.get('date'),
                        languages_id = language_ids,
                        genres_id = genre_ids
                )
                db.session.add(new_game)
                db.session.commit()
                return render_template("add.html", message="The game has been successfully added")
        return render_template("add.html", message=None)


@app.route("/list", methods=["GET", "POST"])
def listAll():
        conn = sqlite3.connect('video_games_data.sqlite3')
        cur = conn.cursor()
        cur.execute("select * from VIDEOGAMES")
        rows = cur.fetchall()
        results = data_cleaning(rows)
        return render_template("list.html", results=results['results'])

@app.route("/api/v1/", methods=["GET"])
@cross_origin()
def send_data():
        if request.args.get('name') :
                name = request.args.get('name')
                name = '%' + name + '%'
                #conn = psycopg2.connect("sqlite:///" + os.path.join(this_dir, "video_games_data.sqlite3"))
                conn = sqlite3.connect('video_games_data.sqlite3')
                cur = conn.cursor()
                cur.execute("select * from VIDEOGAMES where name like ?", (name,))
                rows = cur.fetchall()
                return_json = data_cleaning(rows)
                return jsonify(return_json)
        return jsonify({'results':[]})

def data_cleaning(rows):
        conn = sqlite3.connect('video_games_data.sqlite3')
        cur = conn.cursor()
        return_json = {'results': []}
        for row in rows: 
                lang_ids = row[3].split(", ")
                #langs = '(' + langs + ')'
                cur.execute('select language from LANGUAGES where id in (%s)' % ','.join('?'*len(lang_ids)), lang_ids)
                langs = cur.fetchall()
                langs = [x[0] for x in langs]
                revLangs = "|| "
                for languages in langs:
                        revLangs += languages+" || "
                genre_ids = row[4].split(", ")
                cur.execute('select genre from GENRES where id in (%s)' % ','.join('?'*len(genre_ids)), genre_ids)
                genres = cur.fetchall()
                genres = [x[0] for x in genres]
                revGenres = "|| "
                for gs in genres:
                        revGenres += gs+" || "
                result = {'steam_id': row[0], 'name': row[1], 'release_date': row[2], 'languages':revLangs, 'genres': revGenres}
                return_json['results'].append(result)
        return return_json
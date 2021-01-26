from flask import Flask, session, redirect, url_for, escape, request, render_template, jsonify
import os
from config import app, db
from models import *
from build_db import *
from csv import writer
import sqlite3
from flask_cors import CORS, cross_origin

@app.route("/", methods=["GET", "POST"])
def main():
        return redirect(url_for('index'))


@app.route("/index", methods=["GET", "POST"])
def index():
        if request.method == "POST":
                if request.form.get("add") == "Add":
                        return redirect(url_for('add'))
                if request.form.get("listAll") == "List all":
                        return redirect(url_for('listAll'))

        return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add():
        return render_template("add.html")


@app.route("/list", methods=["GET", "POST"])
def listAll():
        return render_template("list.html")

@app.route("/api/v1/", methods=["GET"])
@cross_origin()
def send_data():
        if request.args.get('name') :
                name = request.args.get('name')
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
                return jsonify(return_json)
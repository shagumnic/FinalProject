from flask import Flask, session, redirect, url_for, escape, request, render_template
import os
from config import app, db
from models import *
from build_db import *
from csv import writer

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

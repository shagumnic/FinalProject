from flask import Flask, session, redirect, url_for, escape, request, render_template
import os
from config import app, db
from models import *
from build_db import *
from csv import writer

@app.route("/", methods=["GET", "POST"])
def index():
        return render_template("base.html")
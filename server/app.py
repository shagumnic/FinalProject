from flask import Flask, session, redirect, url_for, escape, request, render_template
import os
from config import app, db
from models import Store, StoreSchema
from build_db import *
from csv import writer

@app.route("/", methods=["GET", "POST"])
        


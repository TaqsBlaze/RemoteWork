from crypt import methods
from http import client
from msilib.schema import Error
from flask import redirect, render_template, request, url_for, flash
from cryptography.fernet import Fernet
import flask_login
import secrets
import os
from remotework.forms.forms import *
from remotework.forms.forms import ProfileForm
from remotework.models.models import User, Entry, EntryCache, EntryHistory
from remotework import app,db
from flask_login import login_user, current_user, login_required, logout_user
from PIL import Image



def save_image(image):
    hex_name = secrets.token_hex(8)
    filename,ext = os.path.splitext(image.filename)
    new_name = hex_name + ext
    image_path = os.path.join(app.root_path, 'static/images/propix', new_name)
    image_size = (80, 80)
    saved = Image.open(image)
    saved.thumbnail(image_size)
    saved.save(image_path)
    return new_name



@app.route("/", methods = ['GET','POST'])
def index():
    
    return render_template("public/index.html")


@app.route("/signup", methods = ['GET','POST'])
def signup():
    
    return render_template("public/signup.html")


@app.route("/profile", methods = ['GET','POST'])
def profile():
    
    return render_template("public/profile.html")


@app.route("/dev-list", methods = ['GET','POST'])
def dev_list():
    
    return render_template("public/devs.html")


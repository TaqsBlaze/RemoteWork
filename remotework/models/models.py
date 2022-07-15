from datetime import datetime
from email.policy import default
from enum import unique
from log import db, login_manager
from flask_login import FlaskLoginClient, UserMixin



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model,UserMixin):
    
    #fname and lname are not unique in the event that two different pepole with same names are registered in the system
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(),unique = True, nullable = False)
    fname = db.Column(db.String(),unique = False, nullable = False)
    lname = db.Column(db.String(),unique = False, nullable = False)
    email = db.Column(db.String(), unique = True, nullable = False)
    phone = db.Column(db.String(), unique = True, nullable = False)
    country = db.Column(db.String(), unique = False, nullable = False)
    city = db.Column(db.String(), unique = False, nullable = False)
    bio = db.Column(db.String(), unique = False, nullable = True)
    profile_pic = db.Column(db.String(), default = "user.png")
    password = db.Column(db.String(), unique = True, nullable = False)
    langs = db.relationship('Langs', backref = 'user', lazy = True)
    approved = db.relationship('Approved', backref = 'user', lazy = True)
    jobs = db.relationship('Jobs', backref = 'user', lazy = True)
    refs = db.relationship('Refs', backref = 'user', lazy = True)
    
    
    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.fname}', '{self.lname}', '{self.email}', '{self.approved}')"

class Approved(db.Model):
    
    status = db.Column(db.Boolean(), unique = False, default = False)
    
    
class Langs(db.Model):
    
    langs = db.Column(db.String(), nullable = True, unique = False)
    frameworks = db.Column(db.String(), nullable = True, unique = False)
    
class Jobs(db.Model):
    
    jobs = db.Column(db.String(), nullable = True, unique = False)
    job_count = db.Column(db.Integer(), nullable = True, default = 0)
    
class Refs(db.Model):
    
    refs = db.Column(db.String(), nullable = True, unique = False)
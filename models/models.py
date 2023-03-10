from app import db

class Person(db.Model):
    name = db.Column(db.String(100))
    birth_year = db.Column(db.Integer())

class Director(Person):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.Text())

class Movie(db.Model):
    id = db.Column('movie_id', db.Integer(), primary_key=True)
    name = db.Column(db.String(100))
    rating = db.Column(db.Integer())
    directors = db.Column(db.Integer(), db.ForeignKey('Director.'))
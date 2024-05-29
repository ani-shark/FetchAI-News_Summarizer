from . import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    followers = db.Column(db.Integer)
    active = db.Column(db.Boolean(), default=True)

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    heading = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(400))
    body = db.Column(db.String, nullable=False)
    image = db.Column(db.LargeBinary)
    video = db.Column(db.LargeBinary)
    choice = db.Column(db.String(255))
    duration = db.Column(db.Integer)  # Duration saved in minutes
    comments = db.Column(db.String(255))
    latitude = db.Column(db.Float)    # Column to store latitude
    longitude = db.Column(db.Float)   # Column to store longitude

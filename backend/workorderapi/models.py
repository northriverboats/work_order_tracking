"""
models.py
- Data classes for the surveyapi application
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    workorders = db.relationship('Workorder', backref="user", lazy='dynamic')

    def __repr__(self):
        return '<User {} {}>'.format(self.login, self.email)

    def to_dict(self):
        return dict(id=self.id,
                    login=self.login,
                    name=self.name,
                    email=self.email,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    workorders=[workorder.to_dict() for workorder in
                                self.workorders])


class Workorder(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    workorder = db.Column(db.String(1024), unique=True, nullable=False)
    hull = db.Column(db.String(10), unique=True, nullable=False)
    folder = db.Column(db.String(128), nullable=False)
    found = db.Column(db.Boolean, default=False, nullable=False)
    archived = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    history = db.relationship('History', backref="workorder", lazy='dynamic')

    def __repr__(self):
        return '<Workorder {}>'.format(self.workorder)

    def to_dict(self):
        return dict(id=self.id,
                    workorder=self.workorder,
                    hull=self.hull,
                    folder=self.folder,
                    found=self.found,
                    archived=self.archived,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    user_id=self.user_id,
                    history=[histoy.to_dict() for histoy in self.history])


class History(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    workorder_id = db.Column(db.Integer, db.ForeignKey('workorder.id'))

    def __repr__(self):
        return '<post {}>'.format(self.description)

    def to_dict(self):
        return dict(id=self.id,
                    description=self.description,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    workorder_id=self.workorder_id)

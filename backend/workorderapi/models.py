"""
models.py
- Data classes for the surveyapi application
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Workorder(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    workorder = db.Column(db.String(1024), unique=True, nullable=False)
    folder = db.Column(db.String(128), nullable=False)
    found = db.Column(db.Boolean, default=False, nullable=False)
    archived = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    action = db.relationship('Action', backref="workorder", lazy=False)

    def to_dict(self):
        return dict(id=self.id,
                    workorder=self.workorder,
                    folder=self.folder,
                    found=self.found,
                    archived=self.archived,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    actions=[action.to_dict() for action in self.action])


class Action(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    workorder_id = db.Column(db.Integer, db.ForeignKey('workorder.id'))

    def to_dict(self):
        return dict(id=self.id,
                    action=self.action,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    workorder_id=self.workorder_id)

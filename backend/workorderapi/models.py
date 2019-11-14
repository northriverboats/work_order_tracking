"""
models.py
- Data classes for the surveyapi application
"""

from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    login = Column(String(128), nullable=False)
    name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    workorders = relationship('Workorder', backref="user", lazy='dynamic')

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


class Workorder(Base):
    __tablename__ = 'workorder'
    id = Column(Integer, primary_key=True)
    workorder = Column(String(1024), unique=True, nullable=False)
    hull = Column(String(10), unique=True, nullable=False)
    folder = Column(String(128), nullable=False)
    found = Column(Boolean, default=False, nullable=False)
    archived = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.id'))
    history = relationship('History', backref="workorder", lazy='dynamic')

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


class History(Base):
    __tablename__ = 'history'
    id = Column(Integer, primary_key=True)
    description = Column(String(500), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    workorder_id = Column(Integer, ForeignKey('workorder.id'))

    def __repr__(self):
        return '<post {}>'.format(self.description)

    def to_dict(self):
        return dict(id=self.id,
                    description=self.description,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    workorder_id=self.workorder_id)

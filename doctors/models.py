from doctors import db
from flask_login import UserMixin
import datetime



class Doctor(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(length = 50), nullable = False)
    email_address = db.Column(db.String(length = 50), nullable = False, unique = True)
    password = db.Column(db.String(length = 60), nullable = False)
    appointments = db.relationship('Appointment', backref = 'doctor', lazy = True)

    def as_dict(self):
        return {c.name : getattr(self, c.name) for c in self.__table__.columns}



class Appointment(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    patient_name = db.Column(db.String(length = 50), nullable = False, unique = True)
    patient_date = db.Column(db.DateTime, nullable = False)
    reason_for_visit = db.Column(db.String(length = 50), nullable = False)
    appointed_doctor = db.Column(db.Integer(), db.ForeignKey('doctor.id'))

    def as_apt_dict(self):
        return {c.name : getattr(self, c.name) for c in self.__table__.columns}



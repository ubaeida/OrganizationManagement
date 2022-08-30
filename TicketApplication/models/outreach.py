from appSettings import db
from models.gender import Gender


class Outreach(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String(50), nullable=False)
    gender: Gender = db.Column(db.String(50), nullable=False)
    family_number = db.Column(db.Integer, nullable=False)

    search = {
        'id': lambda value: Outreach.id == value,
        'fullname': lambda value: Outreach.fullname.like(f'%{value}%'),
        'gender': lambda value: Outreach.gender == value,
        'family_number': lambda value: Outreach.family_number == value,
    }

    def __init__(self, fullname, gender: Gender, family_number, id=None):
        self.id = id
        self.fullname = fullname
        self.gender = gender
        self.family_number = family_number

    def __repr__(self):
        return f'Gender : {self.gender} , fullname: {self.fullname} , id: {self.id}, family_number: {self.family_number}'

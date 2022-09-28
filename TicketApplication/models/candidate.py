from enum import Enum

from appSettings import db
from models.gender import Gender


class CandidateStatus(Enum):
    nominated = "nominated"
    accepted = "accepted"
    approved = "approved"
    rejected = "rejected"


class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String(50), nullable=False)
    gender: Gender = db.Column(db.String(50), nullable=False)
    nominator_id = db.Column(db.Integer, nullable=False)
    status: CandidateStatus = db.Column(db.String(20), nullable=False)
    updater_id = db.Column(db.Integer, nullable=False)

    search = {
        'id': lambda value: Candidate.id == value,
        'fullname': lambda value: Candidate.fullname.like(f'%{value}%'),
        'gender': lambda value: Candidate.gender == value,
        'nominator_id': lambda value: Candidate.nominator_id == value,
        'status': lambda value: Candidate.status.like(f'{value}'),
        'updater_id': lambda value: Candidate.updater_id == value,
    }

    def __init__(self, fullname, gender: Gender, nominator_id, status: CandidateStatus, updater_id, id=None, ):
        self.fullname = fullname
        self.gender = gender
        self.nominator_id = nominator_id
        self.status = status
        self.updater_id = updater_id
        self.id = id

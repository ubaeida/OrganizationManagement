from enum import Enum

from appSettings import db
from models.gender import Gender


class CaseStatus(Enum):
    active = "active"
    closed = "closed"
    waiting_to_approve = "waiting_to_approve"


class Case(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String(50), nullable=False)
    gender: Gender = db.Column(db.String(50), nullable=False)
    case_worker_id = db.Column(db.Integer, nullable=True)
    status: CaseStatus = db.Column(db.String(20), nullable=False)

    search = {
        'id': lambda value: Case.id == value,
        'fullname': lambda value: Case.fullname.like(f'%{value}%'),
        'gender': lambda value: Case.gender == value,
        'status': lambda value: Case.status.like(f'{value}'),
        'case_worker_id': lambda value: Case.case_worker_id == value,
    }

    def __init__(self, fullname, gender: Gender, case_worker_id, status: CaseStatus = "waiting_to_approve", id=None):
        self.id = id
        self.fullname = fullname
        self.gender = gender
        self.case_worker_id = case_worker_id
        self.status = status

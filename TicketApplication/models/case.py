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

    nullable = {
        'id': lambda: Case.id == None,
        'fullname': lambda: Case.fullname == None,
        'gender': lambda: Case.gender == None,
        'status': lambda: Case.status == None,
        'case_worker_id': lambda: Case.case_worker_id == None,
    }

    case_transitions = {('CASE_MANAGEMENT_OFFICER', 'awaiting_assignment', 'assign'): 'awaiting_assessment',
            ('CASE_MANAGEMENT_OFFICER', 'awaiting_approval', 'approve'): 'active',
            ('CASE_MANAGEMENT_OFFICER', 'awaiting_approval', 'committee'): 'awaiting_committee',
            ('CASE_MANAGEMENT_OFFICER', 'awaiting_approval', 'reject'): 'rejected',
            ('CASE_MANAGEMENT_OFFICER', 'awaiting_closure', 'approve'): 'closed',
            ('CASE_MANAGEMENT_OFFICER', 'awaiting_closure', 'committee'): 'awaiting_committee_closure',
            ('CASE_MANAGEMENT_OFFICER', 'awaiting_closure', 'reject'): 'active',
            ('HEAD_OFFICE', 'awaiting_committee', 'approve'): 'active',
            ('HEAD_OFFICE', 'awaiting_committee', 'reject'): 'rejected',
            ('HEAD_OFFICE', 'awaiting_committee_closure', 'reject'): 'active',
            ('HEAD_OFFICE', 'awaiting_committee_closure', 'reject'): 'closed',
            ('CASEWORKER', 'awaiting_assessment', 'assessed'): 'awaiting_approval',
            ('CASEWORKER', 'active', 'close'): 'awaiting_closure',
            }

    def __init__(self, fullname, gender: Gender, case_worker_id, status: CaseStatus = 'awaiting_assignment', id=None):
        self.id = id
        self.fullname = fullname
        self.gender = gender
        self.case_worker_id = case_worker_id
        self.status = status

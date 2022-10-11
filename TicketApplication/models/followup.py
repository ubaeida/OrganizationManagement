from appSettings import db


class Followup(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(20), nullable=False)
    case_worker_id = db.Column(db.Integer, nullable=True)
    case_id = db.Column(db.Integer, db.ForeignKey('case.id'))

    search = {
        'id': lambda value: Followup.id == value,
        'status': lambda value: Followup.status.like(f'%{value}%'),
        'case_worker_id': lambda value: Followup.case_worker_id == value,
        'case_id': lambda value: Followup.case_id == value,
    }

    nullable = {
        'id': lambda: Followup.id == None,
        'status': lambda: Followup.status == None,
        'case_id': lambda: Followup.case_idid == None,
        'case_worker_id': lambda: Followup.case_worker_id == None,
    }

    def __init__(self, id, status, case_worker_id, case_id):
        self.id = id
        self.status = status
        self.case_worker_id = case_worker_id
        self.case_id = case_id

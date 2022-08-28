from enum import Enum

from appSettings import db
from models.gender import Gender


class CandidateStatus(Enum):
    nominated = "nominated"
    accepted = "accepted"
    approved = "approved"
    rejected = "rejected"


class Candidate(db.model):
    def __init__(self, fullname, gender: Gender, nominator_id, status, updater_id, id=None, ):
        self.fullname = fullname
        self.gender = gender
        self.nominator_name = nominator_id
        self.status = status
        self.updater_id = updater_id
        self.id = id

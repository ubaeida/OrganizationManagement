from mapper.followupMapper import FollowupMapper
from models.followup import Followup
from models.case import Case
from flask_restful import abort
from appSettings import db

followupMapper = FollowupMapper()


class FollowupService:
    def get_by_id(self, id, case_id, user_type, user_id):
        if user_type == "CASEWORKER":
            followup = Followup.query.filter_by(id=id, case_id=case_id, case_worker_id=user_id).first()
            if followup is None:
                return abort(400, erorr='Not found')
            return followupMapper.to_request(followup)
        else:
            followup = Followup.query.filter_by(id=id, case_id=case_id).first()
            if followup is None:
                return abort(400, error='Not found')
            return followupMapper.to_request(followup)

    def delete(self, id):
        followup = Followup.query.get(id)
        if followup is None:
            return abort(400, error='Not found')
        else:
            db.session.delete(followup)
            db.session.commit()
            return abort(400, message='Follow is deleted')

    def put(self, id, case_id, user_id, update_followup):
        raw_to_update = Followup.query.get(id)
        if raw_to_update is None:
            return abort(400, error='Not found')
        else:
            update_followup.id = id
            update_followup.case_worker_id = user_id
            update_followup.case_id = case_id
            db.session.merge(update_followup)
            db.session.commit()
            return raw_to_update

    def add(self, followup, user_id, case_id):
        followup.case_worker_id = user_id
        followup.case_id = case_id
        db.session.add(followup)
        db.session.commit()
        return followup

    def search(self, followup, user_type, user_id):
        followup_list = []
        query = Followup.query
        if user_type == 'CASE_MANAGEMENT_OFFICER':
            for key, value in followup.items():
                if value in ('', 'null', 'none'):
                    query = query.filter(Followup.nullable[key]())
                else:
                    query = query.filter(Followup.search[key](value))
            for raw in query.all():
                followup_list.append(followupMapper.to_request(raw))
            return {'Followup': followup_list}
        if user_type == 'CASEWORKER':
            for key, value in followup.items():
                query = query.filter(Followup.search[key](value), Followup.case_worker_id == user_id)
            for raw in query.all():
                followup_list.append(followupMapper.to_request(raw))

            return {'Followup': followup_list}
        else:
            return abort(400, erorr='Not allowed for this operation')

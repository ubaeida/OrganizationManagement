from models.candidate import Candidate
from models.case import Case
from appSettings import db
from mapper.candidateMapper import CandidateMapper

candidateMapper = CandidateMapper()


class CandidateService:

    def add(self, new_candidate):
        db.session.add(new_candidate)
        db.session.commit()
        return new_candidate

    def put(self, id, updated_candidate):
        raw_to_update = Candidate.query.get(id)
        if raw_to_update is None:
            return {'error': 'not found'}
        else:
            updated_candidate.id = id
            db.session.merge(updated_candidate)
            db.session.commit()
            return raw_to_update

    def delete(self, id):
        raw_to_delete = Candidate.query.get(id)
        if raw_to_delete is None:
            return {'error': 'not found'}
        else:
            db.session.delete(raw_to_delete)
            db.session.commit()
            return f'{raw_to_delete.fullname} is deleted'

    def get_by_id(self, id, user_type):
        current_candidate = Candidate.query.get(id)
        if current_candidate is None:
            return {'error': 'not found'}
        if user_type == 'CASE_MANAGEMENT_OFFICER' and current_candidate.status == 'approved':
            return candidateMapper.to_request(current_candidate)
        if user_type == 'OUTREACH_OFFICER' or user_type == 'HOTLINE_ASSISTANT' or user_type == 'OUTREACH_ASSISTANT':
            return candidateMapper.to_request(current_candidate)

    def search(self, candidate, user_type):
        candidate_list = []
        query = Candidate.query
        if user_type == 'CASE_MANAGEMENT_OFFICER':
            query = query.filter(Candidate.status == 'approved')
        else:
            for key, value in candidate.items():
                query = query.filter(Candidate.search[key](value))
        for raw in query.all():
            candidate_list.append(
                candidateMapper.to_request(raw)
            )
        return {"Candidate": candidate_list}

    def update_status(self, id, user_type, user_id):
        current_candidate = Candidate.query.get(id)
        if current_candidate.status == 'nominated' or current_candidate.status == 'approved':
            if user_type == 'OUTREACH_OFFICER':
                status = 'approved'
                current_candidate.status = status
                current_candidate.updater_id = user_id
                db.session.commit()
            elif user_type == 'CASE_MANAGEMENT_OFFICER':
                status = 'accepted'
                current_candidate.status = status
                current_candidate.updater_id = user_id
                new_case = Case(fullname=current_candidate.fullname, gender=current_candidate.gender,
                                case_worker_id=None)
                db.session.add(new_case)
                db.session.commit()
            else:
                return {'message': 'Not allowed to do this operation'}
        else:
            return {'message': 'the candidate might approved or accepted already'}
        return {'message': 'the candidate status has been updated'}

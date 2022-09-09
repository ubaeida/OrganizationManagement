from models.candidate import Candidate
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

    def get_by_id(self, id):
        searched_raw = Candidate.query.get(id)
        if searched_raw is None:
            return {'error': 'not found'}
        else:
            return candidateMapper.to_request(searched_raw)

    def search(self, candidate):
        candidate_list = []
        query = Candidate.query
        for key, value in candidate.items():
            query = query.filter(Candidate.search[key](value))
        for raw in query.all():
            candidate_list.append(
                candidateMapper.to_request(raw)
            )
        return {"Outreach": candidate_list}

    def update_status(self, id, user_type):
        raw_to_update = Candidate.query.get(id)
        if raw_to_update.status == 'nominated':
            if user_type == 'APPROVE_ASSESSMENT':
                status = 'approved'
                raw_to_update.status = status
            else:
                status = 'accepted'
                raw_to_update.status = status
        else:
            return {'message': 'the candidate might approved or accepted already'}
        return {'message': 'the candidate status has been updated'}

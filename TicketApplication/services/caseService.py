from appSettings import db
from mapper.caseMapper import CaseMapper
from models.case import Case

caseMapper = CaseMapper()


class CaseService:
    def get_by_id(self, id, user_type, user_id):
        if user_type == "CASEWORKER":
            searched_raw = Case.query.filter_by(id=id, case_worker_id=user_id).first()
            if searched_raw is None:
                return {'error': 'not found'}
            else:
                return caseMapper.to_request(searched_raw)
        elif user_type == "CASE_MANAGEMENT_OFFICER":
            searched_raw = Case.query.get(id)
            if searched_raw is None:
                return {'error': 'not found'}
            else:
                return caseMapper.to_request(searched_raw)

    def delete(self, id):
        raw_to_delete = Case.query.get(id)
        if raw_to_delete is None:
            return {'error': 'not found'}
        else:
            db.session.delete(raw_to_delete)
            db.session.commit()
            return f'{raw_to_delete.fullname} is deleted'

    def put(self, id, updated_case):
        raw_to_update = Case.query.get(id)
        if raw_to_update is None:
            return {'error': 'not found'}
        else:
            updated_case.id = id
            db.session.merge(updated_case)
            db.session.commit()
            return raw_to_update

    def add(self, new_case):
        db.session.add(new_case)
        db.session.commit()
        return new_case

    def search(self, args):
        case_list = []
        query = Case.query
        for key, value in Case.items():
            query = query.filter(Case.search[key](value))
        for raw in query.all():
            case_list.append(
                caseMapper.to_request(raw)
            )
        return {"Case": case_list}

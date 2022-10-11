from appSettings import db
from mapper.caseMapper import CaseMapper
from models.case import Case
from flask_restful import abort

caseMapper = CaseMapper()


class CaseService:
    def get_by_id(self, id, user_type, user_id):
        if user_type == "CASEWORKER":
            searched_raw = Case.query.filter_by(id=id, case_worker_id=user_id).first()
            if searched_raw is None:
                return abort(400, erorr='Not found')
            else:
                return caseMapper.to_request(searched_raw)
        elif user_type == "CASE_MANAGEMENT_OFFICER":
            searched_raw = Case.query.get(id)
            if searched_raw is None:
                return abort(400, erorr='Not found')
            else:
                return caseMapper.to_request(searched_raw)

    def delete(self, id):
        raw_to_delete = Case.query.get(id)
        if raw_to_delete is None:
            return abort(400, erorr='Not found')
        else:
            db.session.delete(raw_to_delete)
            db.session.commit()
            return abort(200, message='Case is deleted')

    def put(self, id, updated_case):
        raw_to_update = Case.query.get(id)
        if raw_to_update is None:
            return abort(400, erorr='Not found')
        else:
            updated_case.id = id
            db.session.merge(updated_case)
            db.session.commit()
            return raw_to_update

    def add(self, new_case):
        db.session.add(new_case)
        db.session.commit()
        return new_case

    def search(self, case, user_type, user_id):
        case_list = []
        query = Case.query
        if user_type == 'CASE_MANAGEMENT_OFFICER':
            for key, value in case.items():
                if value in ('', 'null', 'none'):
                    query = query.filter(Case.nullable[key]())
                else:
                    query = query.filter(Case.search[key](value))
            for raw in query.all():
                case_list.append(
                    caseMapper.to_request(raw)
                )
            return {"Case": case_list}
        if user_type == 'CASEWORKER':
            for key, value in case.items():
                query = query.filter(Case.search[key](value), Case.case_worker_id == user_id)
            for raw in query.all():
                case_list.append(
                    caseMapper.to_request(raw)
                )
            return {"Case": case_list}
        else:
            return abort(400, erorr='Not allowed for this operation')

    def update_case_status(self, case_id, cw_id, action, user_type):
        if cw_id is None or action is None:
            return abort(400, erorr='action or params have not been sent')
        case = Case.query.get(case_id)
        case_status = Case.case_transitions.get((user_type, case.status, action))
        if case_status is None:
            return abort(400, erorr=' Not allowed')
        if (user_type, case.status, action) == ('CASE_MANAGEMENT_OFFICER', 'awaiting_assignment', 'assign'):
            if cw_id is None:
                return abort(400, erorr=' caseworker id is requested')
            case.case_worker_id = cw_id
        case.status = case_status
        db.session.commit()
        return abort(200, message=f'the case status has been updated to {case_status}')

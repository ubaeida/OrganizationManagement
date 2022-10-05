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
            return {'message': 'Not allowed for this operation'}

    def update_case_status(self, case_id, params, action, user_type):
        if params is None or action is None:
            return {'message': 'action or params have not been sent'}
        case = Case.query.get(case_id)
        if user_type == 'CASE_MANAGEMENT_OFFICER' and case.status == 'awaiting_assignment' and action == 'assign':
            for key, value in params.items():
                case.case_worker_id = value
            case.status = 'awaiting_assessment'
            db.session.commit()
            return {'message': 'the case have been assigned'}

        if user_type == 'CASE_MANAGEMENT_OFFICER' and case.status == 'awaiting_approval':
            if action == 'approve':
                case.status = 'active'
                db.session.commit()
                return {'message': 'the case status has been updated'}
            elif action == 'committee':
                case.status = 'awaiting_committee'
                db.session.commit()
                return {'message': 'the case status has been updated'}
            else:
                case.status = 'rejected'
                db.session.commit()
                return {'message': 'the case status has been updated'}

        if user_type == 'HEAD_OFFICE' and case.status == 'awaiting_committee':
            if action == 'approve':
                case.status = 'active'
                db.session.commit()
                return {'message': 'the case status has been updated'}
            else:
                case.status = 'rejected'
                db.session.commit()
                return {'message': 'the case status has been updated'}

        if user_type == 'CASE_MANAGEMENT_OFFICER' and case.status == 'awaiting_closure':
            if action == 'approve':
                case.status = 'closed'
                db.session.commit()
                return {'message': 'the case status has been updated'}
            elif action == 'committee':
                case.status = 'awaiting_committee_closure'
                db.session.commit()
                return {'message': 'the case status has been updated'}
            else:
                case.status = 'active'
                db.session.commit()
                return {'message': 'the case status has been updated'}

        if user_type == 'HEAD_OFFICE' and case.status == 'awaiting_committee_closure':
            if action == 'approve':
                case.status = 'closed'
                db.session.commit()
                return {'message': 'the case status has been updated'}
            else:
                case.status = 'active'
                db.session.commit()
                return {'message': 'the case status has been updated'}

    def update_case_status_by_cw(self, case_id, uset_type):
        case = Case.query.get(case_id)
        if uset_type == 'CASEWORKER' and case.status == 'awaiting_assessment':
            case.status = 'awaiting_approval'
            db.session.commit()
            return {'message': 'the case status has been updated'}
        if uset_type == 'CASEWORKER' and case.status == 'active':
            case.status = 'awaiting_closure'
            db.session.commit()
            return {'message': 'the case status has been updated'}

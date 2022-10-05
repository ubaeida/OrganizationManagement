from Auditor.authoritiesAuditor import AuthoritiesAuditor
from Parser.jwt_decorator import JwtAspect
from appSettings import api, Resource, request
from services.caseService import CaseService
from mapper.caseMapper import CaseMapper

caseService = CaseService()
caseMapper = CaseMapper()


class CaseController(Resource):
    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='VIEW_CASES')
    def get(self, id, **kwargs):
        user_type = kwargs['jwt_decoded']['type']
        user_id = kwargs['jwt_decoded']['id']
        return caseService.get_by_id(id, user_type, user_id)

    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='DELETE_CASE')
    def delete(self, id, **kwargs):
        return caseService.delete(id)

    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='EDIT_CASE')
    def put(self, id, **kwargs):
        if request.is_json:
            updated_case = caseMapper.g_to_bo(request.json)
            return caseMapper.to_request(caseService.put(id, updated_case))
        else:
            return {'warning': 'request must be json'}

    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='EDIT_CASE')
    def patch(self, id, **kwargs):
        user_type = kwargs['jwt_decoded']['type']
        return caseService.update_case_status_by_cw(id, user_type)

class CasesController(Resource):
    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='CREATE_CASE')
    def post(self):
        if request.is_json:
            case = caseMapper.g_to_bo(request.json)
            return caseMapper.to_request(caseService.add(case))
        else:
            return {'warning': 'request must be json'}

    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='VIEW_CASES')
    def get(self, **kwargs):
        user_type = kwargs['jwt_decoded']['type']
        user_id = kwargs['jwt_decoded']['id']
        case_key_set = set(caseMapper.g_to_bo(request.args).__dict__.keys())
        input_key_set = set(request.args.keys())
        if not input_key_set.issubset(case_key_set):
            return 'invalid search criteria'
        return caseService.search(request.args, user_type, user_id)


class CMOAssignCaseController(Resource):

    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='UPDATE_CASE_STATUS')
    def patch(self, case_id, action, **kwargs):
        user_type = kwargs['jwt_decoded']['type']
        params = request.args
        if action is not None:
            return caseService.update_case_status(case_id, params, action, user_type)


api.add_resource(CasesController, '/cases')
api.add_resource(CaseController, '/cases/<id>')
api.add_resource(CMOAssignCaseController, '/cases/<case_id>/status/<action>')

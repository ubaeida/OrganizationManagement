from Auditor.authoritiesAuditor import AuthoritiesAuditor
from Parser.jwt_decorator import JwtAspect
from appSettings import api, Resource, request
from services.caseService import CaseService
from mapper.caseMapper import CaseMapper

caseService = CaseService()
caseMapper = CaseMapper


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
    def get(self):
        case_key_set = set(caseMapper.g_to_bo(request.args).__dict__.keys())
        input_key_sey = set(request.args.keys())
        if not input_key_sey.issubset(case_key_set):
            return 'invalid search criteria'
        return caseService.search(request.args)


class CMOAssignCaseController(Resource):
    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='ASSIGN_CASE')
    def get(self, **kwargs):
        return caseService.get_unassigned_cases()

    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='ASSIGN_CASE')
    def patch(self, case_id, cw_id, **kwargs):
        user_type = kwargs['jwt_decoded']['type']
        return caseService.assign_case(case_id, cw_id, user_type)


api.add_resource(CasesController, '/cases')
api.add_resource(CaseController, '/case/<id>')
api.add_resource(CMOAssignCaseController, '/case/assign', '/case/<case_id>/assign/<cw_id>')

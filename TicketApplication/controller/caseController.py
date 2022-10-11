from Auditor.authoritiesAuditor import AuthoritiesAuditor
from Parser.jwt_decorator import JwtAspect
from appSettings import api, Resource, request
from services.caseService import CaseService
from mapper.caseMapper import CaseMapper
from flask_restful import abort

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
            return abort(400, erorr='Request must be jason')


class CasesController(Resource):
    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='CREATE_CASE')
    def post(self, **kwargs):
        if request.is_json:
            case = caseMapper.g_to_bo(request.json)
            return caseMapper.to_request(caseService.add(case))
        else:
            return abort(400, erorr='Request must be jason')

    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='VIEW_CASES')
    def get(self, **kwargs):
        user_type = kwargs['jwt_decoded']['type']
        user_id = kwargs['jwt_decoded']['id']
        case_key_set = set(caseMapper.g_to_bo(request.args).__dict__.keys())
        input_key_set = set(request.args.keys())
        if not input_key_set.issubset(case_key_set):
            return abort(400, message='invalid search criteria')
        return caseService.search(request.args, user_type, user_id)


class CMOAssignCaseController(Resource):

    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='UPDATE_CASE_STATUS')
    def patch(self, case_id, action, **kwargs):
        user_type = kwargs['jwt_decoded']['type']
        cw_id = request.json['cw_id']
        if action is not None:
            return caseService.update_case_status(case_id, cw_id, action, user_type)


api.add_resource(CasesController, '/cases')
api.add_resource(CaseController, '/cases/<id>')
api.add_resource(CMOAssignCaseController, '/cases/<case_id>/status/<action>')

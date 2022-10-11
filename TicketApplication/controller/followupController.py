from Auditor.authoritiesAuditor import AuthoritiesAuditor
from Parser.jwt_decorator import JwtAspect
from appSettings import api, Resource, request
from flask_restful import abort
from mapper.followupMapper import FollowupMapper
from services.followupService import FollowupService

followupService = FollowupService()
followupMapper = FollowupMapper()


class FollowupController(Resource):
    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='VIEW_CASES')
    def get(self, id, case_id, **kwargs):
        user_type = kwargs['jwt_decoded']['type']
        user_id = kwargs['jwt_decoded']['id']
        return followupService.get_by_id(id, case_id, user_type, user_id)

    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='DELETE_CASE')
    def delete(self, id, **kwargs):
        return followupService.delete(id)

    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='EDIT_CASE')
    def put(self, id, case_id, **kwargs):
        user_id = kwargs['jwt_decoded']['id']
        if request.is_json:
            update_followup = followupMapper.g_to_bo(request.json)
            return followupMapper.to_request(followupService.put(id, case_id, user_id, update_followup))
        else:
            return abort(400, error='Request must be json')


class FollowupsController(Resource):
    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='CREATE_CASE')
    def post(self, case_id ,**kwargs):
        user_id = kwargs['jwt_decoded']['id']
        if request.is_json:
            followup = followupMapper.g_to_bo(request.json)
            return followupMapper.to_request(followupService.add(followup, user_id, case_id))
        else:
            return abort(400, erorr='Request must be json')

    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='VIEW_CASES')
    def get(self, **kwargs):
        user_type = kwargs['jwt_decoded']['type']
        user_id = kwargs['jwt_decoded']['id']
        followup_ket_set = set(followupMapper.g_to_bo(request.args).__dict__.keys())
        input_key_set = set(request.args.keys())
        if not input_key_set.issubset(followup_ket_set):
            return abort(400, message='invalid search criteria')
        return followupService.search(request.args, user_type, user_id)


api.add_resource(FollowupController, '/cases/<case_id>/followups/<id>')
api.add_resource(FollowupsController, '/cases/<case_id>/followups')

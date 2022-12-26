from Parser.jwt_decorator import JwtAspect
from Auditor.authoritiesAuditor import AuthoritiesAuditor
from appSettings import Resource, request, api
from mapper.candidateMapper import CandidateMapper
from services.candidateService import CandidateService
from flask_restful import abort

candidateMapper = CandidateMapper()
candidateService = CandidateService()


class CandidateController(Resource):
    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='EDIT_ASSESSMENT')
    def put(self, id, **kwargs):
        if request.is_json:
            updated_candidate = candidateMapper.g_to_bo(request.json)
            user_id = kwargs['jwt_decoded']['id']
            return candidateMapper.to_request(candidateService.put(id, user_id,updated_candidate))
        else:
            return abort(400, erorr=' request must be json')

    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='DELETE_ASSESSMENT')
    def delete(self, id, **kwargs):
        return candidateService.delete(id)

    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='VIEW_ASSESSMENT,view_approved_candidates')
    def get(self, id, **kwargs):
        user_type = kwargs['jwt_decoded']['type']
        return candidateService.get_by_id(id, user_type)

    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='APPROVE_ASSESSMENT')
    def patch(self, id, **kwargs):
        global status
        if request.is_json:
            status = request.json["status"]
        user_type = kwargs['jwt_decoded']['type']
        user_id = kwargs['jwt_decoded']['id']
        return candidateMapper.to_request_with_id(candidateService.update_status(id, user_type, user_id, status))


class CandidatesController(Resource):
    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='CREATE_ASSESSMENT')
    def post(self, **kwargs):
        if request.is_json:
            request.json['nominator_id'] = kwargs['jwt_decoded']['id']
            request.json['updater_id'] = kwargs['jwt_decoded']['id']
            candidate = candidateMapper.g_to_bo(request.json)
            return candidateMapper.to_request_with_id(candidateService.add(candidate))
        else:
            return abort(400, erorr=' request must be json')

    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='VIEW_ASSESSMENT,view_approved_candidates')
    def get(self, **kwargs):
        user_type = kwargs['jwt_decoded']['type']
        candidate_key_set = set(candidateMapper.g_to_bo(request.args).__dict__.keys())
        input_key_sey = set(request.args.keys())
        if not input_key_sey.issubset(candidate_key_set):
            return abort(400, erorr=' invalid search criteria')
        return candidateService.search(request.args, user_type)


api.add_resource(CandidatesController, '/tickets/candidates')
api.add_resource(CandidateController, '/tickets/candidates/<id>')

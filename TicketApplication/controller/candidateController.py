from Parser.jwt_decorator import JwtAspect
from Auditor.authoritiesAuditor import AuthoritiesAuditor
from appSettings import Resource, request, api
from mapper.candidateMapper import CandidateMapper
from services.candidateService import CandidateService

candidateMapper = CandidateMapper()
candidateService = CandidateService()


class CandidateController(Resource):
    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='EDIT_ASSESSMENT')
    def put(self, id, **kwargs):
        if request.is_json:
            updated_candidate = candidateMapper.g_to_bo(request.json)
            return candidateMapper.to_request(candidateService.put(id, updated_candidate))
        else:
            return {'warning': 'request must be json'}

    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='DELETE_ASSESSMENT')
    def delete(self, id, **kwargs):
        return candidateService.delete(id)

    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='VIEW_ASSESSMENT')
    def get(self, id, **kwargs):
        return candidateService.get_by_id(id)

    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='APPROVE_ASSESSMENT,ACCEPT_CASE')
    def patch(self, id, **kwargs):
        user_type = kwargs['jwt_decoded']['type']
        return candidateService.update_status(id, user_type)


class CandidatesController(Resource):
    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='CREATE_ASSESSMENT')
    def post(self, **kwargs):
        if request.is_json:
            candidate = candidateMapper.g_to_bo(request.json)
            return candidateMapper.to_request(candidateService.add(candidate))
        else:
            return {'warning': 'request must be json'}

    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='VIEW_ASSESSMENT')
    def get(sel, **kwargs):
        candidate_key_set = set(candidateMapper.g_to_bo(request.args).__dict__.keys())
        input_key_sey = set(request.args.keys())
        if not input_key_sey.issubset(candidate_key_set):
            return 'invalid search criteria'
        return candidateService.search(request.args)


api.add_resource(CandidatesController, '/candidates')
api.add_resource(CandidateController, '/candidate/<id>')

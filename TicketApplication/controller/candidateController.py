from Parser.jwt_decorator import JwtAspect
from appSettings import Resource, request, api
from mapper.candidateMapper import CandidateMapper
from services.candidateService import CandidateService

candidateMapper = CandidateMapper()
candidateService = CandidateService()


class CandidateController(Resource):
    @JwtAspect.token_required
    def put(self, id):
        if request.is_json:
            updated_candidate = candidateMapper.g_to_bo(request.json)
            return candidateMapper.to_request(candidateService.put(id, updated_candidate))

    @JwtAspect.token_required
    def delete(self, id):
        return candidateService.delete(id)

    @JwtAspect.token_required
    # @Allowed_Permission('VIEW_ASSESMENT')
    def get(self, id, **kwargs):
        print('from get', kwargs['jwt_decoded'])
        return candidateService.get_by_id(id)


class CandidatesController(Resource):
    @JwtAspect.token_required
    def post(self):
        if request.is_json:
            candidate = candidateMapper.g_to_bo(request.json)
            return candidateMapper.to_request(candidateService.add(candidate))

    @JwtAspect.token_required
    def get(self):
        candidate_key_set = set(candidateMapper.g_to_bo(request.args).__dict__.keys())
        input_key_sey = set(request.args.keys())
        if not input_key_sey.issubset(candidate_key_set):
            return 'invalid search criteria'
        return candidateService.search(request.args)


api.add_resource(CandidatesController, '/candidates')
api.add_resource(CandidateController, '/candidate/<id>')

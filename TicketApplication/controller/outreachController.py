from Auditor.authoritiesAuditor import AuthoritiesAuditor
from Parser.jwt_decorator import JwtAspect
from appSettings import api, Resource, request
from mapper.outreachMapper import OutreachMapper
from services.outreachService import OutreachService
from flask_restful import abort

outreachService = OutreachService()
outreachBoMapper = OutreachMapper()


class OutreachController(Resource):
    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='EDIT_ASSESSMENT')
    def put(self, id, **kwargs):
        if request.is_json:
            updated_outreach = outreachBoMapper.g_to_bo(request.json)
            return outreachBoMapper.to_request(outreachService.put(id, updated_outreach))
        else:
            return abort(400, erorr='Request must be jason')

    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='DELETE_ASSESSMENT')
    def delete(self, id, **kwargs):
        return outreachService.delete(id)

    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='VIEW_ASSESSMENT')
    def get(self, id, **kwargs):
        return outreachService.get_by_id(id)


class OutreachesController(Resource):
    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='VIEW_ASSESSMENT')
    def get(self, **kwargs):
        outreach_key_set = set(outreachBoMapper.g_to_bo(request.args).__dict__.keys())
        input_key_set = set(request.args.keys())
        if not input_key_set.issubset(outreach_key_set):
            return abort(400, erorr='Invalid search criteria')
        return outreachService.search(request.args)

    @JwtAspect.jwt_secured
    @AuthoritiesAuditor.secured(permissions='CREATE_ASSESSMENT')
    def post(self, **kwargs):
        if request.is_json:
            outreach = outreachBoMapper.g_to_bo(request)
            return outreachBoMapper.to_request(outreachService.add(outreach))
        else:
            return abort(400, erorr='Request must be jason')


api.add_resource(OutreachesController, "/outreaches")
api.add_resource(OutreachController, "/outreaches/<id>")

from appSettings import api, Resource, request
from mapper.outreachBoMapper import OutreachBoMapper
from services.outreachService import OutreachService
from flask_restful import reqparse

outreachService = OutreachService()
outreachBoMapper = OutreachBoMapper()

# make the links and classes better
class OutreachesController(Resource):

    def get(self):
        outreach_key_set = set(outreachBoMapper.g_to_bo(request.args).__dict__.keys())
        input_key_set = set(request.args.keys())
        if not input_key_set.issubset(outreach_key_set):
            return 'invalid search criteria'

        return outreachService.search(request.args)

    def post(self):
        if request.is_json:
            outreach = outreachBoMapper.to_bo(request)
            return outreachBoMapper.to_request(outreachService.add(outreach))
        else:
            return {'error': 'request must be jason'}


class OutreachController(Resource):

    def put(self, id):
        updated_outreach = outreachBoMapper.to_bo(request.json)
        return outreachBoMapper.to_request(outreachService.put(id, updated_outreach))

    def delete(self, id):
        return outreachService.delete(id)

    def get(self, id):
        return outreachService.get_by_id(id)


api.add_resource(OutreachesController, "/outreach")
api.add_resource(OutreachController, "/outreach/<id>")

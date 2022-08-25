from appSettings import api, Resource, request
from mapper.outreachBoMapper import OutreachBoMapper
from services.outreachService import OutreachService

outreachService = OutreachService()
outreachBoMapper = OutreachBoMapper()


class OutreachController(Resource):

    def get(self):
        return outreachService.get()

    def post(self):
        if request.is_json:
            outreach = outreachBoMapper.to_bo(request)
            return outreachService.add(outreach)
        else:
            return {'error': 'request must be jason'}


class OutreachesController(Resource):

    def put(self, id):
        updated_outreach = request.json
        for v in request.json.keys():
            print(v)
        return outreachService.put(id, updated_outreach)

    def delete(self, id):
        return outreachService.delete(id)

    def get(self, id):
        return outreachService.get_by_id(id)


class SearchInOutreachController(Resource):

    def get(self, fullname):
        return outreachService.get_by_name(fullname)


api.add_resource(OutreachController, "/outreach")
api.add_resource(OutreachesController, "/outreach/<id>")
api.add_resource(SearchInOutreachController, "/outreach/search/<fullname>")

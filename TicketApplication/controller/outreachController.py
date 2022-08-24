from appSettings import app, api, Resource, request
from services.outreachService import OutreachService

outreachService = OutreachService()


class OutreachController(Resource):

    def get(self):
        return outreachService.get()

    def post(self):
        if request.is_json:
            return outreachService.add()
        else:
            return {'error': 'request must be jason'}, 400


class AdvancedOutreachController(Resource):

    def put(self, id):
        return outreachService.put(id)

    def delete(self, id):
        return outreachService.delete(id)

    def get(self, id):
        return outreachService.get_by_id(id)


class NameSearchOutreachController(Resource):

    def get(self, fullname):
        return outreachService.get_by_name(fullname)


api.add_resource(OutreachController, "/outreach")
api.add_resource(AdvancedOutreachController, "/outreach/<id>")
api.add_resource(NameSearchOutreachController, "/outreach/search/<fullname>")

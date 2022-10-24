from models.outreach import Outreach
from appSettings import Resource, request, api


class InfoController(Resource):
    def get(self):
        searched_raw = Outreach.query.all()
        return f'outreach count {len(searched_raw)}'


api.add_resource(InfoController, '/info')

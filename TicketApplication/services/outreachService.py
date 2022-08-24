from models.outreach import Outreach
from appSettings import db, Resource, request, make_response, jsonify


class OutreachService(Resource):

    def get(self):
        outreach_DB = Outreach.query.all()
        outreach_list = []
        for raw in outreach_DB:
            raw_data = {"Id": raw.id, "Full_Name": raw.fullname, "Gender": raw.gender,
                        "family_number": raw.family_number}
            outreach_list.append(raw_data)
        return {"Outreach": outreach_list}, 200

    def add(self):
        new_outreach = Outreach(fullname=request.json["fullname"], gender=request.json["gender"],
                                family_number=request.json["family_number"])
        db.session.add(new_outreach)
        db.session.commit()
        return f'added new raw for {new_outreach.fullname}', 200

    def put(self, id):
        raw_to_update = Outreach.query.get(id)
        if raw_to_update is None:
            return {'error': 'not found'}, 400
        else:
            raw_to_update.fullname = request.json['fullname']
            raw_to_update.gender = request.json['gender']
            raw_to_update.family_number = request.json['family_number']
            db.session.commit()
            return f'updated', 200

    def delete(self, id):

        raw_to_delete = Outreach.query.get(id)
        if raw_to_delete is None:
            return {'error': 'not found'}, 400
        else:
            db.session.delete(raw_to_delete)
            db.session.commit()
            return f'{raw_to_delete.fullname} is deleted', 200

    def get_by_id(self, id):
        searched_raw = Outreach.query.get(id)
        if searched_raw is None:
            return {'error': 'not found'}, 400
        else:
            return make_response(jsonify({'id': searched_raw.id, 'fullname': searched_raw.fullname, 'family_number':
                searched_raw.family_number, 'Gender': searched_raw.gender}), 201)

    def get_by_name(self, fullname):
        searched_raw = Outreach.query.filter(Outreach.fullname.startswith(fullname)).all()
        outreach_list = []
        for raw in searched_raw:
            raw_data = {"Id": raw.id, "Full_Name": raw.fullname, "Gender": raw.gender,
                        "family_number": raw.family_number}
            outreach_list.append(raw_data)
        return {"Outreach": outreach_list}, 200

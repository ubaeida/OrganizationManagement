from appSettings import db, request
from mapper.outreachBoMapper import OutreachBoMapper
from models.outreach import Outreach

outreachBoMapper = OutreachBoMapper()


class OutreachService:

    def get(self):
        outreach_DB = Outreach.query.all()
        outreach_list = []
        for raw in outreach_DB:
            out = outreachBoMapper.to_request(raw)
            outreach_list.append(out)
        return {"Outreach": outreach_list}

    def add(self, new_outreach):
        db.session.add(new_outreach)
        db.session.commit()
        return f'added new raw for {new_outreach.fullname}'

    def put(self, id, updated_outreach):  # Here need to be mapped
        raw_to_update = outreachBoMapper.to_request(Outreach.query.get(id))
        if raw_to_update is None:
            return {'error': 'not found'}
        else:
            raw_to_update.fullname = request.json['fullname']
            raw_to_update.gender = request.json['gender']
            raw_to_update.family_number = request.json['family_number']
            db.session.commit()
            return f'updated'

    def delete(self, id):
        raw_to_delete = Outreach.query.get(id)
        if raw_to_delete is None:
            return {'error': 'not found'}
        else:
            db.session.delete(raw_to_delete)
            db.session.commit()
            return f'{raw_to_delete.fullname} is deleted'

    def get_by_id(self, id):
        searched_raw = Outreach.query.get(id)
        if searched_raw is None:
            return {'error': 'not found'}
        else:
            out = outreachBoMapper.to_request(searched_raw)
            return out

    def get_by_name(self, fullname):
        searched_raw = Outreach.query.filter(Outreach.fullname.startswith(fullname)).all()
        if not searched_raw:
            return {'error': 'not found'}
        else:
            outreach_list = []
            for raw in searched_raw:
                out = outreachBoMapper.to_request(raw)
                outreach_list.append(out)
            return {"Outreach": outreach_list}

import copy

from appSettings import db
from mapper.outreachBoMapper import OutreachBoMapper
from models.outreach import Outreach

outreachBoMapper = OutreachBoMapper()


class OutreachService():

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
        return new_outreach

    def put(self, id, updated_outreach):
        raw_to_update = Outreach.query.get(id)
        if raw_to_update is None:
            return {'error': 'not found'}
        else:
            raw_to_update = updated_outreach
            raw_to_update.id = id
            # raw_to_update.fullname = updated_outreach.fullname
            # raw_to_update.gender = updated_outreach.gender
            # raw_to_update.family_number = updated_outreach.family_number
            db.session.commit()
        return raw_to_update

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

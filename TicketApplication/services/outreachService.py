from appSettings import db
from mapper.outreachBoMapper import OutreachBoMapper
from models.outreach import Outreach

outreachBoMapper = OutreachBoMapper()


class OutreachService:

    def search(self, outreach):
        outreach_list = []
        query = Outreach.query
        for key, value in outreach.items():
            query = query.filter(Outreach.search[key](value))
        print(query)
        for raw in query.all():
            outreach_list.append(
                outreachBoMapper.to_request(raw)
            )
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
            updated_outreach.id = id
            db.session.merge(updated_outreach)
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

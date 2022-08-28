from appSettings import request
from models.outreach import Outreach


class OutreachBoMapper:

    def to_bo(self, data):
        return Outreach(fullname=request.json["fullname"], gender=request.json["gender"],
                        family_number=request.json["family_number"])

    def g_to_bo(self, dictionary):
        return Outreach(fullname=dictionary.get("fullname"), gender=dictionary.get("gender"),
                        family_number=dictionary.get("family_number"))

    def to_request(self, bo):
        out = {"id": bo.id, "fullname": bo.fullname, "gender": bo.gender,
               "family_number": bo.family_number}
        return out

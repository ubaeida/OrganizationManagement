from models.outreach import Outreach


class OutreachMapper:

    def g_to_bo(self, dictionary):
        return Outreach(fullname=dictionary.get("fullname"), gender=dictionary.get("gender"),
                        family_number=dictionary.get("family_number"))

    def to_request(self, bo):
        out = {"id": bo.id, "fullname": bo.fullname, "gender": bo.gender,
               "family_number": bo.family_number}
        return out

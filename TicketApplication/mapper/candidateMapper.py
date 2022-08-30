from models.candidate import Candidate


class CandidateMapper:
    def g_to_bo(self, dictionary):
        return Candidate(fullname=dictionary.get("fullname"), gender=dictionary.get("gender"),
                         nominator_id=dictionary.get("nominator_id"), status=dictionary.get("status"),
                         updater_id=dictionary.get("updater_id"))

    def to_request(self, bo):
        out = {"fullname": bo.fullname, "gender": bo.gender, "nominator_id": bo.nominator_id,
               "status": bo.status, "updater_id": bo.updater_id}
        return out

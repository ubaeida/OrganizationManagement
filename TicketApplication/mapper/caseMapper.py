from models.case import Case


class CaseMapper:
    def g_to_bo(self, dictionary):
        return Case(fullname=dictionary.get("fullname"), gender=dictionary.get("gender"),
                    case_worker_id=dictionary.get("case_worker_id"), status=dictionary.get("status"))

    def to_request(self, bo):
        out = {"fullname": bo.fullname, "gender": bo.gender, "case_worker_id": bo.case_worker_id, "status": bo.status}
        return out

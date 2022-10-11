from models.followup import Followup


class FollowupMapper:
    def g_to_bo(self, dictionary):
        return Followup(id=dictionary.get('id'), status=dictionary.get('status'),
                        case_worker_id=dictionary.get('case_worker_id'), case_id=dictionary.get('case_id'))

    def to_request(self, bo):
        out = {'id': bo.id, 'status': bo.status, 'case_worker_id': bo.case_worker_id ,'case_id': bo.case_id}
        return out

from appSettings import *
from controller.outreachController import *
from controller.candidateController import *
from controller.caseController import *
from controller.followupController import *
import py_eureka_client.eureka_client as eureka_client
from py_eureka_client import *

OutreachController()
OutreachesController()
CandidatesController()
CandidateController()
CasesController()
CaseController()
FollowupController()
FollowupsController()

rest_port = 8050
eureka_client.init(eureka_server="http://localhost:8761",
                   app_name="ticket-application-server",
                   instance_port=rest_port)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

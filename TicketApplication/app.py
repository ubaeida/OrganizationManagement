from appSettings import *
from controller.outreachController import *
from controller.candidateController import *
from controller.caseController import *
from controller.followupController import *
from controller.InfoController import *
import os

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
InfoController()
rest_port = 8050
localhost = 'localhost'
eureka_client.init(eureka_server=os.environ.get('eureka_server'),
                   app_name="ticket-application-server",
                   instance_port=rest_port,
                   instance_host=localhost
                   )
# os.environ['eureka_server'] = "http://eureka-server:8761"
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='localhost', port=8050)
else:
    # Creates the database and tables
    # for the production environment
    app.app_context().push()
    db.create_all()

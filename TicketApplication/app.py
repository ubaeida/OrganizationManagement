from appSettings import *
from controller.outreachController import *
from controller.candidateController import *
from controller.caseController import *
from controller.followupController import *
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
rest_port = 8050
localhost = 'localhost'
# eureka_client.init(eureka_server=os.environ.get('eureka_server'),
#                    app_name= os.environ.get('app_name'),
#                    instance_port=rest_port,
#                    # instance_host=os.environ.get('instance_host')
#                    )

eureka_client.init(eureka_server="http://localhost:8761/eureka/",
                   app_name="ticket-application-server",
                   instance_port=rest_port,
                   instance_host=localhost
                   )

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=8050)
else:
    # Creates the database and tables
    # for the production environment
    app.app_context().push()
    db.create_all()

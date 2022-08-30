from appSettings import *
from controller.outreachController import *
from controller.candidateController import *

OutreachController()
OutreachesController()
CandidatesController()
CandidateController()
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

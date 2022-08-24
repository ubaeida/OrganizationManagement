from appSettings import *
from controller.outreachController import OutreachController

OutreachController()
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

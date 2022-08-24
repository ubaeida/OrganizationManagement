from sqlalchemy import create_engine


class DBConnector:
    __instance = None

    @staticmethod
    def get_instance():
        if DBConnector.__instance is None:
            DBConnector()
        return DBConnector.__instance

    def __init__(self):
        if DBConnector.__instance is not None:
            raise Exception('Connection is already exist')

        self.engine = create_engine('mysql+pymysql://root:1234@localhost:3306/organizationmanagement')
        DBConnector.__instance = self

    def get_connection(self):
        return self.engine.connect()


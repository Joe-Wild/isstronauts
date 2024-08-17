from datetime import datetime
from tinydb import TinyDB, Query

from databaseInterface import DatabaseInterface
from accomplishableAction import AccomplishableAction, ActionPeriodicity
from accomplishedAction import AccomplishedAction

class DatabaseTinyDB(DatabaseInterface): 


    # db = TinyDB('./db.json')
    # actions = db.table('actions')
    # actions.insert({'value': True})
    # actions.all()

    def connect(self, connectionString):
        # TODO
        pass

    def disconnect(self):
        # TODO
        pass


    def reset(self):
        # TODO
        pass


    def getAccomplishableActions(self):
        # TODO
        pass
    

    def addAccomplishableAction(self, accomplishableAction: AccomplishableAction):
        # TODO
        pass
    



    def getAcomplishedActionsBetween(self, dateStart: datetime, dateEnd: datetime):
        # TODO
        pass
    

    def addAcomplishedAction(self, acomplishedAction: AccomplishedAction):
        # TODO
        pass
    
from datetime import datetime

from databaseInterface import DatabaseInterface
from accomplishableAction import AccomplishableAction, ActionPeriodicity
from accomplishedAction import AccomplishedAction

class DatabaseRam(DatabaseInterface): 

    # Ram storage
    _accomplishableActions = []
    _accomplishedActions = []


    def connect(self, connectionString):
        pass

    def disconnect(self):
        pass


    def reset(self):
        
        self._accomplishableActions = [ 
            AccomplishableAction('Eat something',          ActionPeriodicity.Daily),
            AccomplishableAction('Sleep',                  ActionPeriodicity.Daily),
            AccomplishableAction("Play",                   ActionPeriodicity.Daily),
            AccomplishableAction('Read an entire book',    ActionPeriodicity.Weekly)
        ]

        self._accomplishedActions = []



    def getAccomplishableActions(self):

        return self._accomplishableActions
    

    def addAccomplishableAction(self, accomplishableAction: AccomplishableAction):

        self._accomplishableActions.append(accomplishableAction)





    def getAccomplishedActionsBetween(self, dateStart: datetime, dateEnd: datetime):

        return self._accomplishedActions


    def addAccomplishedAction(self, acomplishedAction: AccomplishedAction):

        self._accomplishedActions.append(accomplishedAction)
    


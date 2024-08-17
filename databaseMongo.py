from datetime import datetime
from pymongo import MongoClient

from databaseInterface import DatabaseInterface
from accomplishableAction import AccomplishableAction, ActionPeriodicity
from accomplishedAction import AccomplishedAction

class DatabaseMongo(DatabaseInterface): 

    def connect(self, connectionString):

        self.client = MongoClient(connectionString);

        self.database = self.client["STARs"];

        self.accomplishableActionsDocuments = self.database["accomplishableActions"]

        self.accomplishedActionsDocuments = self.database["accomplishedActions"]


    def disconnect(self):
        
        self.client.close()

    
    def reset(self):

        # clear the accomplishable actions
        self.accomplishableActionsDocuments.drop()

        # add some accomplishable actions by default 
        self.addAccomplishableAction(AccomplishableAction("1h Sport",               ActionPeriodicity.Daily))
        self.addAccomplishableAction(AccomplishableAction("30mn Reading",           ActionPeriodicity.Daily))
        self.addAccomplishableAction(AccomplishableAction("1h Foreign Languages",   ActionPeriodicity.Daily))
        self.addAccomplishableAction(AccomplishableAction("IROSa Maintenance",      ActionPeriodicity.Weekly))
        self.addAccomplishableAction(AccomplishableAction("Team Interaction",       ActionPeriodicity.Weekly))
       
        # clear the accomplished actions
        self.accomplishedActionsDocuments.drop()



    def getAccomplishableActions(self):

        documents = self.accomplishableActionsDocuments.find()

        actions = list(map(self.toAccomplishableAction, documents))

        return actions
    

    def addAccomplishableAction(self, accomplishableAction: AccomplishableAction):
        
        self.accomplishableActionsDocuments.insert_one({
            "description": accomplishableAction.description,
            "periodicity": accomplishableAction.periodicity.value
        })
    

    def getAccomplishedActionsBetween(self, dateStart: datetime, dateEnd: datetime):
        
        documents = self.accomplishedActionsDocuments.find()

        actions = list(map(self.toAccomplishedAction, documents))

        return actions
    

    def addAccomplishedAction(self, accomplishedAction: AccomplishedAction):

        self.accomplishedActionsDocuments.insert_one({
            "description": accomplishedAction.description,
            "date": accomplishedAction.date
        })
    

    def toAccomplishableAction(self, document):

        return AccomplishableAction(
            document["description"], 
            ActionPeriodicity(document["periodicity"]))
    
    
    def toAccomplishedAction(self, document):

        return AccomplishedAction(
            document["description"],
            document["date"])



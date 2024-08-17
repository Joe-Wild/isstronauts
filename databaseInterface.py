from abc import ABC, abstractmethod
from datetime import datetime

from accomplishableAction import AccomplishableAction, ActionPeriodicity
from accomplishedAction import AccomplishedAction

class DatabaseInterface(ABC):

    @abstractmethod
    def connect(self, connectionString):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def getAccomplishableActions(self):
        pass

    @abstractmethod
    def addAccomplishableAction(self, accomplishableAction: AccomplishableAction):
        pass


    @abstractmethod
    def getAccomplishedActionsBetween(self, dateStart: datetime, dateEnd: datetime):
        pass

    @abstractmethod
    def addAccomplishedAction(self, accomplishedAction: AccomplishedAction):
        pass
    


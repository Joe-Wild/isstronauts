from enum import Enum

class ActionPeriodicity(Enum):
    Daily = 1
    Weekly = 2

class AccomplishableAction:

    # id = "" not used, descriptions are unique and used to identify accomplishable actions

    def __init__(self, description, periodicity):

        self.description = description
        self.periodicity = periodicity


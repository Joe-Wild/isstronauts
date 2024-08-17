from datetime import datetime
from dotenv import dotenv_values

from databaseMongo import DatabaseMongo
from databaseRam import DatabaseRam
from userInterface import UserInterface, Features
from accomplishableAction import AccomplishableAction, ActionPeriodicity
from accomplishedAction import AccomplishedAction

# Create instances
# database = DatabaseRam()
database = DatabaseMongo()
userInterface = UserInterface()

# Connect the database
database.connect(dotenv_values(".env").get("DATABASE_MONGO_URL"))
database.reset()


def reportAccomplishedAction():

    # Get the list of accomplishable actions from the database
    accomplishableActions = database.getAccomplishableActions()

    # Display the list of accomplished actions to the user to allow him to select one
    selectedAccomplishableAction = userInterface.askForAccomplishedAction(accomplishableActions)

    # Create a new accomplishedAction using the description of the selected AccomplishableAction and the current time
    accomplishedAction = AccomplishedAction(
        selectedAccomplishableAction.description, 
        datetime.now()
    )

    # Store it into the database
    database.addAccomplishedAction(accomplishedAction)

    # Display a confirmation
    print("The action you accomplished has been saved")
    print("")



def addAccomplishableAction():

    # Ask for a new accomplishable action
    accomplishableAction = userInterface.askForAccomplishableAction()

    # Escape if empty
    if accomplishableAction.description == "":
        return
    
    # Get the list of accomplishable actions from the database...
    accomplishableActions = database.getAccomplishableActions()

    # ... to check if this description was already used
    for element in accomplishableActions:
        if element.description == accomplishableAction.description:
    
            print("You already created an accomplishable action with this description")

            return


    # Store it into the database
    database.addAccomplishableAction(accomplishableAction)

    # Display a confirmation
    print("The new accomplishable action has been saved")
    print("")

    print("The new list of accomplishable actions is now:")
    accomplishableActions = database.getAccomplishableActions()

    for element in accomplishableActions:
        print(element.description + " (" + element.periodicity.name + ")")

    print("")



def getAnalysis():

    # Get accomplished actions
    accomplishedActions = database.getAccomplishedActionsBetween(datetime.now(), datetime.now())

    for element in accomplishedActions:
        print(str(element.date) + "  " + element.description)


def databaseReset():

    database.reset()


# Main loop
while True:
    
    print("")
    print("------------------------------------------------------")
    
    selectedFeature = userInterface.askForFeature()

    match selectedFeature:

        case Features.ReportAccomplishedAction.value:
            reportAccomplishedAction()

        case Features.CreateNewAccomplishableAction.value:
            addAccomplishableAction()

        case Features.GetAnalysis.value:
            getAnalysis()

        case Features.DatabaseReset.value:
            databaseReset()

        case Features.Exit.value:
            quit()


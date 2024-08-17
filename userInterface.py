from enum import Enum
import inquirer

from accomplishableAction import AccomplishableAction, ActionPeriodicity
from accomplishedAction import AccomplishedAction


class Features(Enum):
    ReportAccomplishedAction =       "Report an accomplished action"
    CreateNewAccomplishableAction =  "Add a new accomplishable action"
    GetAnalysis =                    "Get the analysis of your accomplished actions"
    DatabaseReset =                  "Reset (or initialize) the database"
    Exit=                            "Exit"


class UserInterface:

    def __init__(self):

        pass


    def askForFeature(self):
        
        questions = [
            inquirer.List('feature',
                            message="Select a feature",
                            choices=[
                                Features.ReportAccomplishedAction.value,
                                Features.CreateNewAccomplishableAction.value,
                                Features.GetAnalysis.value,
                                Features.DatabaseReset.value,
                                Features.Exit.value
                            ],
                        ),
        ]
    
        answers = inquirer.prompt(questions)

        return answers.get('feature')
    


    def askForAccomplishedAction(self, accomplishableActions: list[AccomplishableAction]): 

        # Convert the list of accomplishableActions [a, b, c]
        # To a 'list of tuples' [(a.description, a), [(b.description, b), [(c.description, c)]

        # https://python-inquirer.readthedocs.io/en/latest/examples.html#checkbox-py
        # The choices list can also be a list of tuples.
        # The first value in each tuple should be the label displayed to the user.
        # The second value in each tuple should be the actual value for that option.
        # This allows you to have the user choose options that are not plain strings in the code.

        choices = list(map(lambda action: (action.description, action) , accomplishableActions))

        questions = [
            inquirer.List('action',
                            message="Select a feature",
                            choices=choices,
                        ),
        ]
    
        answers = inquirer.prompt(questions)

        # TODO Fix this cast to return an AccomplishedAction instead of an Any
        # return AccomplishedAction(answers.get('action'))
        
        return answers.get('action')



    def askForAccomplishableAction(self): 

        questions = [
            inquirer.Text("description", 
                message="Can you describe the action the user can accomplish?"),
            inquirer.List("periodicity",
                message="What is the periodicity of this action?",
                choices=[(ActionPeriodicity.Daily.name, ActionPeriodicity.Daily),
                         (ActionPeriodicity.Weekly.name, ActionPeriodicity.Weekly)
                        ])
        ]
    
        answers = inquirer.prompt(questions)

        return AccomplishableAction(answers.get('description'), answers.get('periodicity'))
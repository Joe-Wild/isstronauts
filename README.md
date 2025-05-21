# Main

A Habit tracker using object-oriented and functional programming in Python.

Periodically (daily & weekly) tasks to achieve (ISS maintenance, sport,...). 

Basic building blocks of this tracking app are as follows:

o A user can define multiple habits in the application. A habit has a task specification and a periodicity.

o A task can be completed, i.e., “checked-off”, by a user at any point in time.

o Each task needs to be checked-off at least once during the period the user defined for the respective habit. 

If a user misses to complete a habit during the specified period, the user is said to break the habit.

o If a user manages to complete the task of a habit x consecutive periods in a row, I.e., without breaking the habit,
we say that the user established a streak of x periods. For instance, if a user wants to work out every day and does so for two full weeks, 
they establish a 14-day streak of working out.

# Environment

    _This project runs in a dev container (VSCode). 
    _It needs Python 3.10+ minima. 
    _Having been written in Python 3.11.7.
    _Database interchangeable:
    MongoDB via MongoDBCompass provided as standard.
    _('base':conda)/anaconda24

# Dependencies

    pip install python-dotenv

    pip install inquirer

    pip install tinydb

    pip install pymongo 

     /usr/local/python/3.11.7/bin/python3.11.7 main.py 

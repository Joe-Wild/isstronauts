# Functional Programming Approach

from datetime import datetime, timedelta
from pymongo import MongoClient

def connect_to_db():
    client = MongoClient('mongodb')
    return client['your_database_name']['your_collection_name']

def calculate_start_date(period: str, now: datetime) -> datetime:
    return now - timedelta(days=1) if period == 'daily' else now - timedelta(weeks=1)

def fetch_habit_data(collection, start_date: datetime, now: datetime):
    return collection.find({'date_field': {'$gte': start_date, '$lt': now}})

def get_habit_data(period: str):
    now = datetime.now()
    collection = connect_to_db()
    start_date = calculate_start_date(period, now)
    return list(fetch_habit_data(collection, start_date, now))

# avoid changing data in place. Instead, return new data structures.
def process_habit_data(data):
    return [doc['habit_name'] for doc in data if 'habit_name' in doc]

#process data
def get_processed_habit_data(period: str):
    data = get_habit_data(period)
    return list(map(lambda doc: doc['habit_name'], filter(lambda doc: 'habit_name' in doc, data)))


#(VS)
#-------------------------------------------------------------------------------------------------------

#Imperative Programming Approach

from pymongo import MongoClient
from datetime import datetime, timedelta

client = MongoClient('mongodb://')
db = client['your_database_name']
collection = db['your_collection_name']

def get_habit_data(period):
    now = datetime.now()
    if period == 'daily':
        start_date = now - timedelta(days=1)
    else:
        start_date = now - timedelta(weeks=1)

    data = collection.find({'date_field': {'$gte': start_date, '$lt': now}})
    return list(data)

def process_habit_data(data):
    processed_data = []
    for doc in data:
        if 'habit_name' in doc:
            processed_data.append(doc['habit_name'])
    return processed_data

#Using of variables to track state as the program executes
def get_and_process_habit_data(period):
    data = get_habit_data(period)
    return process_habit_data(data)

import random
import boto3
import os
from dotenv import load_dotenv
import psycopg2
import argparse

load_dotenv()

#setting env variables
port = os.getenv("PORT")
username = os.getenv("USER")
password = os.getenv("PASSWORD")
dbname = os.getenv("DB_NAME")
endpoint = os.getenv("ENDPOINT")
REGION = os.getenv("REGION")
ACCESS_ID= os.getenv("ACCESS_ID")
SECRET_KEY = os.getenv("SECRET_KEY")
IDENTIFIER = os.getenv("IDENTIFIER")

# workout tuples used to define a min/max for particular region
ABDOMINAL_TUPLE = (150,250)
LEG_WORKOUT_TUPLE = (75, 200)
CHEST_WORKOUT_TUPLE = (75, 150)
STAY_AND_HOLD_TUPLE = (150, 280)
BACK_WORKOUT_TUPLE = (75,125)

# workouit dictionary, can be updated 
WORKOUT_DICT = {
    "crunches" : ABDOMINAL_TUPLE,
    "push-ups" : CHEST_WORKOUT_TUPLE,
    "leg raises" : ABDOMINAL_TUPLE, 
    "bicycle kicks" : ABDOMINAL_TUPLE,
    "air squats" : LEG_WORKOUT_TUPLE, 
    "planking" : STAY_AND_HOLD_TUPLE, 
    "hanging leg raises" : STAY_AND_HOLD_TUPLE, 
    "lunges" : LEG_WORKOUT_TUPLE,
    "pullups" : BACK_WORKOUT_TUPLE,
    "chinups" : BACK_WORKOUT_TUPLE
    }



        
def connect_to_db():
    connection = psycopg2.connect(database=dbname, user=username, password=password, host=endpoint, port=port, sslrootcert="SSLCERTIFICATE")
    return connection


def insert_workout_and_sets(workout: str, reps: int):
    connection = connect_to_db()
    curs = connection.cursor()
    curs.execute("insert into postgres.public.workout_table (workout_name, reps, completed_on) VALUES (%s,%s,now())",(workout, reps))
    connection.commit()
    connection.close()
    print(f"Inserted Workout : {workout} and Reps : {reps} into table")
    
def sum_workouts():
    connection = connect_to_db()
    curs = connection.cursor()
    curs.execute("select sum(reps), workout_name from postgres.public.workout_table group by workout_name ")
    for record in curs:
        print(str(record))
    connection.close()
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Changing gross-bods to dad-bods')
    parser.add_argument('--get_workout', action='store_const', const=True, help='Will retrieve workout and set')
    parser.add_argument('--sum_workout', action='store_const', const=True, help='Summarizes your workouts so far')
    args = parser.parse_args()
    
    get_workout = args.get_workout
    sum_workout = args.sum_workout
    
    
    random_workout = random.choice(list(WORKOUT_DICT.keys()))
    min_range, max_range = WORKOUT_DICT.get(random_workout)
    arbitrary_reps = random.randrange(min_range, max_range)
    if random_workout != "planking":
        print(f"Hello! Todays workout will be {random_workout}, which you'll need to do {arbitrary_reps} of!")
    else:
        print(f"Hello! Todays workout will be {random_workout}, which you'll need to do {arbitrary_reps} seconds on each side!")
    try:
        if get_workout:
            insert_workout_and_sets(workout=random_workout, reps=arbitrary_reps)
        elif sum_workout:
            sum_workouts()

    except Exception as e:
        print(f"L + ratio : {e}")
        
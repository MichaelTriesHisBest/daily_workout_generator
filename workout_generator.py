import random
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

port = os.getenv("PORT")
username = os.getenv("USER")
password = os.getenv("PASSWORD")
dbname = os.getenv("DB_NAME")
endpoint = os.getenv("ENDPOINT")
region = os.getenv("REGION")

ABDOMINAL_TUPLE = (150,250)
LEG_WORKOUT_TUPLE = (75, 200)
UPPERBODY_TUPLE = (75, 150)
STAY_AND_HOLD_TUPLE = (150, 280)
WORKOUT_DICT = {
    "crunches" : ABDOMINAL_TUPLE,
 "push-ups" : UPPERBODY_TUPLE,
 "leg raises" : ABDOMINAL_TUPLE, 
 "bicycle kicks" : ABDOMINAL_TUPLE,
 "air squats" : LEG_WORKOUT_TUPLE, 
 "planking" : STAY_AND_HOLD_TUPLE, 
 "hanging leg raises" : STAY_AND_HOLD_TUPLE, 
 "lunges" : LEG_WORKOUT_TUPLE 
 }



        
def connect_to_db():
    return ""

def insert_workout_and_sets(workout: str, reps: int):
    return ""
    
def disconnect_from_db():
    return ""
    
if __name__ == "__main__":
    random_workout = random.choice(list(WORKOUT_DICT.keys()))
    min_range, max_range = WORKOUT_DICT.get(random_workout)
    arbitrary_reps = random.randrange(min_range, max_range)
    if random_workout != "planking":
        print(f"Hello! Todays workout will be {random_workout}, which you'll need to do {arbitrary_reps} of!")
    else:
        print(f"Hello! Todays workout will be {random_workout}, which you'll need to do {arbitrary_reps} seconds on each side!")
    try:
        connect_to_db()
        insert_workout_and_sets(workout=random_workout, reps=arbitrary_reps)
    except Exception as e:
        print(f"L + ratio : {e}")
        
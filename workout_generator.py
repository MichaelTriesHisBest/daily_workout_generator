import random
import boto3


ABDOMINAL_TUPLE = (150,250)
LEG_WORKOUT_TUPLE = (75, 200)
UPPERBODY_TUPLE = (75, 150)
STAY_AND_HOLD_TUPLE = (150, 280)
WORKOUT_DICT = {"crunches" : ABDOMINAL_TUPLE, "push-ups" : UPPERBODY_TUPLE,
 "leg raises" : ABDOMINAL_TUPLE, "bicycle kicks" : ABDOMINAL_TUPLE, "air squats" : LEG_WORKOUT_TUPLE, 
 "planking" : STAY_AND_HOLD_TUPLE, "hanging leg raises" : STAY_AND_HOLD_TUPLE, 
 "lunges" : LEG_WORKOUT_TUPLE }


if __name__ == "__main__":
    random_workout = random.choice(list(WORKOUT_DICT.keys()))
    min_range, max_range = WORKOUT_DICT.get(random_workout)
    if random_workout != "planking":
        print(f"Hello! Todays workout will be {random_workout}, which you'll need to do {random.randrange(min_range, max_range)} of!")
    else:
        print(f"Hello! Todays workout will be {random_workout}, which you'll need to do {random.randrange(min_range, max_range)} seconds on each side!")
        
    connect_to_db()
    insert_workout_and_sets()
        
        
def connect_to_db():
    return ""

def insert_workout_and_sets():
    return ""
    
def disconnect_from_db():
    return ""
    
# daily_workout_generator
Helpin me stay in shape with some daily workout check-ins
### Description
Python-based script that randomly selects a workout from a curated list of workouts + reps.
Connects to RDS and saves workout + reps so I can summerize and feel decent about myself at the end of the year.
Flag operated, so --get_workout gives you a workout and --sum_workout summerizes your workout.


### TODO list 
- [x] Add workouts and tuples
- [x] Add readme
- [x] Setup env variables
- [x] Add RDS connection
- [x] Insert workouts into table
- [] Add ability to stop/start rds instance (to save $$$)
- [x] Add flags
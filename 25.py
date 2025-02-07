import json
import os
from datetime import datetime

# Class to represent a single workout session
class Workout:
    def __init__(self, date, exercise, duration, calories_burned):
        self.date = date
        self.exercise = exercise
        self.duration = duration  # in minutes
        self.calories_burned = calories_burned
    
    def __repr__(self):
        return f"Workout(date={self.date}, exercise={self.exercise}, duration={self.duration}, calories_burned={self.calories_burned})"

# FitnessTracker class to manage multiple workouts
class FitnessTracker:
    def __init__(self, filename="fitness_data.json"):
        self.filename = filename
        self.workouts = []
        self.load_data()

    def add_workout(self, workout):
        self.workouts.append(workout)
        self.save_data()

    def save_data(self):
        with open(self.filename, "w") as file:
            data = [workout.__dict__ for workout in self.workouts]
            json.dump(data, file, indent=4)

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.workouts = [Workout(**workout) for workout in data]
    
    def show_progress(self):
        total_duration = sum(workout.duration for workout in self.workouts)
        total_calories = sum(workout.calories_burned for workout in self.workouts)
        
        print(f"Total Workouts: {len(self.workouts)}")
        print(f"Total Duration: {total_duration} minutes")
        print(f"Total Calories Burned: {total_calories} kcal")

    def show_workouts(self):
        if not self.workouts:
            print("No workouts recorded yet.")
            return
        for workout in self.workouts:
            print(f"Date: {workout.date}, Exercise: {workout.exercise}, Duration: {workout.duration} minutes, Calories Burned: {workout.calories_burned} kcal")

    def find_workout_by_date(self, date):
        for workout in self.workouts:
            if workout.date == date:
                print(f"Workout on {date}: {workout.exercise}, {workout.duration} minutes, {workout.calories_burned} kcal")
                return
        print(f"No workout found for {date}")

def display_menu():
    print("\nFitness Tracker Menu:")
    print("1. Add a Workout")
    print("2. View Workouts")
    print("3. View Progress Summary")
    print("4. Find Workout by Date")
    print("5. Exit")

def add_workout_input(tracker):
    date = input("Enter the workout date (YYYY-MM-DD): ")
    exercise = input("Enter the exercise name: ")
    duration = int(input("Enter the duration (in minutes): "))
    calories_burned = int(input("Enter calories burned: "))
    
    workout = Workout(date, exercise, duration, calories_burned)
    tracker.add_workout(workout)
    print("Workout added successfully.")
def main():
    tracker = FitnessTracker()
    
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_workout_input(tracker)
        elif choice == "2":
            tracker.show_workouts()
        elif choice == "3":
            tracker.show_progress()
        elif choice == "4":
            date = input("Enter the date to search for (YYYY-MM-DD): ")
            tracker.find_workout_by_date(date)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
"""
This module allows the user to input data to sleep related prompts - this data is then stored in a json file
"""

from datetime import date, datetime
import os
import json

file_path = os.getenv("SLEEP_DATA")

data = {}
today = str(date.today())

hours = int(input("Enter your estimated hours of sleep: "))
continuous = int(input("Enter 1 if did not wake \nEnter 2 if woke once \nEnter 3 if woke more then once: "))
bed_time = datetime.strptime(input("Enter the time (HH:MM) you attempted to go to sleep: "))
out_of_bed = datetime.strptime(input("Enter the time (HH:MM) you got out of bed for the day: "))
rating = int(input("Enter a number between 1 and 10 representing how you feel: "))
while rating > 10 or rating < 1:
    rating = int(input("Enter a number between 1 and 10 representing how you feel: "))
perception = input("Enter a description of how you feel: ")

stats = {
  "hours": hours,
  "cont": continuous,
  "bed_time": bed_time,
  "out_of_bed": out_of_bed,
  "rating": rating,
  "perception": perception
}

# if i dont load i will lose or data
with open(file_path, "r") as file:
    data = json.load(file)

# then you can just treat it like a python dictionary
data[today] = stats

# Open json file 
with open(file_path, "w") as file:
    json.dump(data, file, indent=2)
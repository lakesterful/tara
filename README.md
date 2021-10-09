# Bikeshare Project
### lakesterful
This is a Bikeshare Project created for Udacity's [Programming for Data Science with Python]

## Datasets

In this project, data is provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns.  This project compares the system usage between three large cities: Chicago, New York City, and Washington, DC.

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six columns:

Start Time (e.g., 2017-01-01 00:07:57)
End Time (e.g., 2017-01-01 00:20:53)
Trip Duration (in seconds - e.g., 776)
Start Station (e.g., Broadway & Barry Ave)
End Station (e.g., Sedgwick St & North Ave)
User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

Gender
Birth Year

## Statistics Computed

#1 Popular times of travel (i.e., occurs most often in the start time)

* most common month
* most common day of week
* most common hour of day

#2 Popular stations and trip

* most common start station
* most common end station
* most common trip from start to end (i.e., most frequent combination of start station and end station)

#3 Trip duration

* total travel time
* average travel time

#4 User info

* counts of each user type
* counts of each gender (only available for NYC and Chicago)
* earliest, most recent, most common year of birth (only available for NYC and Chicago)

## Contents
The contents of the project are:
* **bikeshare.py** - The main file to run this project

It uses data for following three cities: 
* **chicago.csv**
* **new_york_city.csv**
* **washington.csv**

## Software Requirements
* Python 3
* NumPy
* Pandas (Version 0.23)

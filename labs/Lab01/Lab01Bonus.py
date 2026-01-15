#
# Caleb Hemphill
# 01/14/2026
# This program calculates the time it takes to travel
# a certain distance going a specific speed.
# Outputs the time in hours and minutes.
#
# Note: The miles and speed entered could be a floating point
# number.
#

# Get the number of miles.
miles = float(input('Enter number of miles: '))

# Get the speed in MPH.
speed = float(input('Enter speed in MPH: '))

# Calculate the travel time in hours and minutes.
travel_time = miles / speed
travel_time_hours = int(miles // speed)
travel_time_minutes = (travel_time - travel_time_hours) * 60

# Display the travel time in hours and minutes (formatted to 2 decimal places).
print(f'You should cover that distance in {travel_time_hours} hours and {travel_time_minutes:.2f} minutes.')

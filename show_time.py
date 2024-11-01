import datetime

# Get current date and time
current_time = datetime.datetime.now()

# Display the current date, time, and day
print("Current Date and Time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
print("Day of the Week:", current_time.strftime("%A"))


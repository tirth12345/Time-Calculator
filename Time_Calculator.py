def add_time(start, duration, start_day=''):
    # Define days of the week
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Split the start time into components
    start_time, start_period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))
    duration_hour, duration_minute = map(int, duration.split(":"))
    
    # Convert start_hour to 24-hour format
    if start_period == "PM" and start_hour != 12:
        start_hour += 12
    elif start_period == "AM" and start_hour == 12:
        start_hour = 0
    
    # Calculate new time in minutes
    total_minutes = (start_hour * 60 + start_minute) + (duration_hour * 60 + duration_minute)
    
    # Calculate new hour and minute
    new_hour = (total_minutes // 60) % 24
    new_minute = total_minutes % 60
    total_days = total_minutes // (24 * 60)
    
    # Determine new period and adjust hour to 12-hour format
    new_period = "AM" if new_hour < 12 else "PM"
    if new_hour == 0:
        new_hour = 12
    elif new_hour > 12:
        new_hour -= 12
    
    # Format new minute to be two digits
    new_minute = str(new_minute).zfill(2)
    
    # Calculate new day if start_day is provided
    if start_day:
        day_index = (days_of_week.index(start_day.capitalize()) + total_days) % 7
        new_day = days_of_week[day_index]
        new_time = f"{new_hour}:{new_minute} {new_period}, {new_day}"
    else:
        new_time = f"{new_hour}:{new_minute} {new_period}"
    
    # Append the number of days later if applicable
    if total_days == 1:
        new_time += " (next day)"
    elif total_days > 1:
        new_time += f" ({total_days} days later)"
    
    print(new_time)
    return new_time

# Test the function
add_time('3:30 PM', '2:12')


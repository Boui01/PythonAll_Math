from datetime import datetime, timedelta
import pytz

def time_until_next(Time , Position):
    # Set the time zone to Thailand
    thailand = pytz.timezone('Asia/Bangkok')
    
    # Get the current UTC time
    now = datetime.now(thailand)
    
    # Create a datetime object for today's 5 AM
    if Position == 'Hour':
        next = now.replace(hour=  now.hour + Time if now.hour + Time < 24 else now.hour + Time - 24)
    elif Position == 'Minute':
        next = now.replace(minute= now.minute + Time if now.minute + Time < 60 else now.minute + Time - 60)
    elif Position == 'Second':
        next = now.replace(second= now.second + Time if now.second + Time < 60 else now.second + Time - 60)
    else:
        raise ValueError('Position must be Hour, Minute or Second')
    
    
    # Return the difference between next and now
    return '\nWait : ' + now.strftime('%H:%M:%S') + '\nStart : ' + next.strftime('%H:%M:%S')


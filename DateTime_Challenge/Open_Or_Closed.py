#   PYTHON COURSE
#   ASSIGNMENT: DATETIME CHALLENGE
#   AUTHOR: KIRK HILTON

import pytz
from pytz import tzinfo
import datetime


def Portland_Branch():
    source_now = datetime.datetime.now()
    source_time_zone = pytz.timezone('US/Mountain')
    source_date_with_timezone = source_time_zone.localize(source_now)
    Port_time_zone = pytz.timezone('US/Pacific')
    Port_date_with_timezone = source_date_with_timezone.astimezone(Port_time_zone)
    Port_current = Port_date_with_timezone.strftime("%I:%M %p")
    start = '09:00:00 AM'
    end = '05:00:00 PM'
    if Port_current > start and Port_current < end:
        print("Branch Location: Portland, OR\nCurrent time: {}\nOperating hours: 9:00am - 5:00pm\nStatus: OPEN\n".format(Port_current))
        tempo.sleep(1)
    else:
        print("Branch Location: Portland, OR\nCurrent time: {}\nBranch hours: 9:00am - 5:00pm\nBranch status: CLOSED\n".format(Port_current))
        
def NewYork_Branch():
    source_now = datetime.datetime.now()
    source_time_zone = pytz.timezone('US/Mountain')
    source_date_with_timezone = source_time_zone.localize(source_now)
    NewYork_time_zone = pytz.timezone('US/Eastern')
    NewYork_date_with_timezone = source_date_with_timezone.astimezone(NewYork_time_zone)
    NewYork_current = NewYork_date_with_timezone.strftime("%I:%M %p")
    start = '09:00:00 AM'
    end = '05:00:00 PM'
    if NewYork_current > start and NewYork_current < end:
        print("Branch Location: New York, NY\nCurrent time: {}\nOperating hours: 9:00am - 5:00pm\nStatus: OPEN\n".format(NewYork_current))
        tempo.sleep(1)
    else:
        print("Branch Location: New York, NY\nCurrent time: {}\nBranch hours: 9:00am - 5:00pm\nBranch status: CLOSED\n".format(NewYork_current))

def London_Branch():
    source_now = datetime.datetime.now()
    source_time_zone = pytz.timezone('US/Mountain')
    source_date_with_timezone = source_time_zone.localize(source_now)
    London_time_zone = pytz.timezone('Europe/London')
    London_date_with_timezone = source_date_with_timezone.astimezone(London_time_zone)
    London_current = London_date_with_timezone.strftime("%I:%M %p")
    start = '09:00:00 AM'
    end = '05:00:00 PM'
    if London_current > start and London_current < end:
        print("Branch Location: London, UK\nCurrent time: {}\nOperating hours: 9:00am - 5:00pm\nStatus: OPEN\n".format(London_current))
        tempo.sleep(1)
    else:
        print("Branch Location: London, UK\nCurrent time: {}\nBranch hours: 9:00am - 5:00pm\nBranch status: CLOSED\n".format(London_current)) 
        

if __name__ == "__main__":
    Portland_Branch()
    NewYork_Branch()
    London_Branch()
  

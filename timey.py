import time
from popup import *

timer = 30*60              #30 minutes * 60 seconds
curr_time = time.time()     #in seconds
alarm = time.localtime(curr_time + timer)

while(1):
    time.sleep(1)
    now = time.localtime()
    if(now.tm_hour == alarm.tm_hour and now.tm_min == alarm.tm_min and now.tm_sec == alarm.tm_sec):
        alert_popup("Timey", "Up you go!", "Time to stretch")
        curr_time = time.time()     #in seconds
        alarm = time.localtime(curr_time + timer)
    else:
        continue
        



import time
from datetime import datetime as dt

host_path = "hosts"
redirect = "127.0.0.1"
website_list = ["www.netflix.com","www.facebook.com"]
#Condition
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Rihanna")
    else:
        print("Drake")
    time.sleep(5)
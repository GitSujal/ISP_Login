#!/usr/bin/env python2.7
import os
import subprocess
import schedule
import time

def process():
    print("Searching for status logged in or not! ...")
    subprocess.call(["python","isp_login.py"])

subprocess.call(["python", "isp_login.py"]) # Initial login.
schedule.every(15).minutes.do(process) # Schedule the login script to do its job every 15 minutes.

while True:
    schedule.run_pending()
    time.sleep(1)

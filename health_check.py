#!/usr/bin/env python3
""" server health check script to be set to a CRON job that executes the script every 60 seconds, if any issues arise, an email will be sent indicating the error"""
import shutil
import psutil
import socket

import emails #emails.py

cpu = "Error - CPU usage is over 80%"
disk = "Available disk space is less than 20%"
memory =  "Available memory is less than 500MB"
host = "Error - localhost cannot be resolved to 127.0.0.1"
body = "Please check your system and resolve the issue as soon as possible"

disk_ratio = (shutil.disk_usage("/")[2]/shutil.disk_usage("/")[0])*100
error = "0"
if disk_ratio < 20" #less than 20%
        error = disk
if psutil.cpu_percent(1) > 80: #greater than 80%
        error = cpu
if psutil.virtual_memory()[4] < 500000000: #less than 500MB
        error = memory
if socket.gethostbyname('localhost') != "127.0.0.1": #localhost isn't set to 127.0.0.1
        error = host

if error != "0":
        #print(error)
        emails.send_email(emails.generate_error_report("automation@example.com","username@example.com",error,body)

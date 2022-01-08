#!/usr/bin/env python

from time import sleep
from requests import get
from configparser import ConfigParser
from os import path
from datetime import datetime

config = ConfigParser()
config.read(f"{path.dirname(path.realpath(__file__))}/ydns_python_updater_config.ini", encoding='utf-8')

USERNAME = config["DEFAULT"]["USERNAME"]
PASSWORD = config["DEFAULT"]["PASSWORD"]
HOSTNAME = config["DEFAULT"]["HOSTNAME"]
TIME_WAIT = int(config["DEFAULT"]["TIME_WAIT"])

while True:
    try:
        update_response = get(f"https://ydns.io/api/v1/update/?host={HOSTNAME}", auth=(USERNAME, PASSWORD)).text
        remote_ip_address = get("https://ydns.io/api/v1/ip").text
        print(f"[{datetime.now()}] Update request has been sent. Response: \"{update_response}\", Remote IP Address: {remote_ip_address}")
        sleep(TIME_WAIT * 60)

    except Exception as e:
        print(f"[{datetime.now()}] Exception thrown: {e}")
        sleep(5)
        continue
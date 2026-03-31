import time
from os import error

import requests
import dotenv
import json
import os


endpoint = "https://api.helldivers2.dev/api"
waitTime = 10
lastCallTime = 0.0
_cache = {}

dotenv.load_dotenv()

client = os.getenv("X_SUPER_CLIENT")
contact = os.getenv("X_SUPER_CONTACT")
if client is None or contact is None:
    raise ValueError("No client and/or contact provided")

s = requests.Session()
s.headers.update({"X-Super-Client" : client, "X-Super-Contact" : contact})



# just a quick demo
async def get_war_state():
    global lastCallTime, _cache
    current_time = time.time()

    if _cache is not None and current_time - lastCallTime < waitTime:
        return _cache.copy()

    try:
        response = s.get(f"{endpoint}/v1/war")
        response.raise_for_status()

        data = response.json()

        _cache = data
        lastCallTime = current_time
        return data
    except requests.exceptions.RequestException as e:
        #it is screwing up somewhere
        if _cache is not None:
            return _cache.copy()

        return None




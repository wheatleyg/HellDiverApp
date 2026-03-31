from os import error

import requests
import dotenv
import json
import os


endpoint = "https://api.helldivers2.dev/api"
waitTime = 10


dotenv.load_dotenv()

client = os.getenv("X_SUPER_CLIENT")
contact = os.getenv("X_SUPER_CONTACT")
if client is None or contact is None:
    raise ValueError("No client and/or contact provided")

s = requests.Session()
s.headers.update({"X-Super-Client" : client, "X-Super-Contact" : contact})





# just a quick demo
async def get_war_state():
    response = s.get(f"{endpoint}/v1/war")
    return response, response.json()
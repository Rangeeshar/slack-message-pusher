"""
A service which could send spam notification to slack.
"""
import os
import sys
import json
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class JsonData(BaseModel):
    RecordType: str
    Type: str
    TypeCode: int
    Name: str
    Tag: str
    MessageStream: str
    Description: str
    Email: str
    From: str
    BouncedAt: str

@app.get("/")
async def healthcheck():
    return {"message": "Working"}

@app.post("/")
async def root(data: JsonData):
    """
    This is root function which checks the json
    """
    if data.Type == "SpamNotification":
        temp_data = json.loads(data.json())
        payload = {
            "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Spam notification alert*"
                },

            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Hi, The email {} bounced at {} and the reason was _{}_".format(temp_data.get("Email"),
                                                                                  temp_data.get("BouncedAt"),
                                                                                    temp_data.get("Description"))
                },
                
            }
            ]
            }
        url = os.getenv("SLACK_WEBHOOK_URL")
        byte_length = str(sys.getsizeof(payload))
        headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
    return data
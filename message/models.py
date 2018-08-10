import json
import os

import requests


COLOR_CHOICES = ['good', 'warning', 'danger', 'default']


class Slack:

    def __init__(self):
        pass

    @staticmethod
    def post_message(message):

        url = "https://hooks.slack.com/services/" + os.environ['WEB_HOOK']

        payload = str(json.dumps({
            'attachments': [message]
        }))

        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        return response.status_code == 200

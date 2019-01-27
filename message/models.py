# -*- coding: utf-8 -*-

import json
import os

import requests

from applications.models import Application

COLOR_CHOICES = ['good', 'warning', 'danger', 'default']


class Message:

    def __init__(self, application: Application, title, text, color='default'):
        self.application = application
        self.title = title
        self.text = text
        self.color = color

    def get_attachment(self):
        return {
            "title": self.title,
            "text": self.text,
            "color": self.color
        }

    def get_url(self):
        return self.application.web_hook


class Slack:

    def __init__(self):
        pass

    @staticmethod
    def post_message(message: Message):

        payload = str(json.dumps({
            'username': message.application.name,
            'icon_url': message.application.thumb_url,
            'channel': message.application.channel,
            'attachments': [message.get_attachment()]
        }))

        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }

        response = requests.request("POST", message.get_url(), data=payload, headers=headers)

        return response.status_code == 200

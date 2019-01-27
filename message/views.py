# -*- coding: utf-8 -*-

from rest_framework import views
from rest_framework.response import Response

from applications.models import Application
from message.models import Slack, Message
from message.serializers import MessageSerializer


class MessageView(views.APIView):

    @staticmethod
    def post(request):

        serializer = MessageSerializer(many=False, data=request.data)

        if serializer.is_valid():

            message = serializer.validated_data

            a = Application.objects.get(pk=request.data['application'])

            del message['application']

            message['author_name'] = a.name

            message['thumb_url'] = a.thumb_url

            m = Message(a, message['title'], message['text'], message['color'])

            if Slack.post_message(m):
                return Response(None, status=204)
            else:
                return Response({"error": "Something happened"}, status=500)

        else:
            return Response(serializer.errors, status=400)

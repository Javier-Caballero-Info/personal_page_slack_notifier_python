from rest_framework import views
from rest_framework.response import Response

from applications.models import Application
from message.models import Slack
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

            if Slack.post_message(message):
                return Response({"message": message})
            else:
                return Response({"error": "Something happened"}, status=500)

        else:
            return Response(serializer.errors, status=400)

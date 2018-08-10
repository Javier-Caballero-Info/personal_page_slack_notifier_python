# -*- coding: utf-8 -*-

from rest_framework import viewsets
from applications.serializers import ApplicationSerializer
from applications.models import Application


class ApplicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

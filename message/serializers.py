# -*- coding: utf-8 -*-

from rest_framework import serializers

from applications.models import Application
from message.models import COLOR_CHOICES


class MessageSerializer(serializers.Serializer):
    application_queryset = Application.objects.all()

    application = serializers.PrimaryKeyRelatedField(
        required=True, many=False, allow_null=False, read_only=False, queryset=application_queryset
    )

    title = serializers.CharField(
        required=True, allow_blank=False, max_length=100, write_only=True, read_only=False
    )
    text = serializers.CharField(
        required=True, allow_blank=False, max_length=1000, write_only=True, read_only=False
    )

    color = serializers.ChoiceField(choices=COLOR_CHOICES, default='default')

    def create(self, validated_data):
        print(validated_data)
        pass

    def update(self, instance, validated_data):
        pass

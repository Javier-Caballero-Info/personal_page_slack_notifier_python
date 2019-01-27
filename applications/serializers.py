# -*- coding: utf-8 -*-

import uuid

from rest_framework import serializers

from applications.models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True, format='hex_verbose')
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    channel = serializers.CharField(required=True, allow_blank=False, max_length=100)
    thumb_url = serializers.URLField(required=True, max_length=250)
    web_hook = serializers.URLField(required=True, max_length=250)

    class Meta:
        model = Application

        fields = ('url', 'id', 'name', 'thumb_url', 'channel', 'web_hook')

    def create(self, validated_data):
        validated_data['id'] = uuid.uuid4()
        return Application.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.thumb_url = validated_data.get('thumb_url', instance.thumb_url)
        instance.channel = validated_data.get('channel', instance.channel)
        instance.web_hook = validated_data.get('web_hook', instance.web_hook)
        instance.save()
        return instance

# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from users import views as user_views
from applications import views as application_views
from message import views as message_views

router = routers.DefaultRouter()

router.register(r'users', user_views.UserViewSet)
router.register(r'groups', user_views.GroupViewSet)

router.register(r'applications', application_views.ApplicationViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^messages', message_views.MessageView.as_view()),
    url(r'^admin/', admin.site.urls),
]

from django.urls import path
from apps.core.views import IndexView, SendPushNotification

apps_name = "core"

urlpatterns = [
    path('', IndexView.as_view()),
    path('send_push', SendPushNotification.as_view()),
]

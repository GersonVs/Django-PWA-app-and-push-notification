import json

from django.conf import settings
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from webpush import send_user_notification


class IndexView(View):
    def get(self, request, *args, **kwars):
        webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
        vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
        user = User.objects.get(username='admin')

        return render(request, 'home.html', {'user': user, 'vapid_key': vapid_key})


@method_decorator(csrf_exempt, name='dispatch')
class SendPushNotification(View):
    def post(self,request):
        try:
            body = request.body
            data = json.loads(body)

            if 'head' not in data or 'body' not in data or 'id' not in data:
                return JsonResponse(status=400, data={"message": "Invalid data format"})

            user_id = data['id']
            user = get_object_or_404(User, pk=user_id)
            payload = {'head': data['head'], 'body': data['body']}
            send_user_notification(user=user, payload=payload, ttl=1000)

            return JsonResponse(status=200, data={"message": "Web push successful"})
        except TypeError:
            return JsonResponse(status=500, data={"message": "An error occurred"})

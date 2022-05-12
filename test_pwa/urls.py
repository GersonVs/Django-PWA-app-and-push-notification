from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('', include('pwa.urls')),
    path('webpush/', include('webpush.urls')),

    path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/x-javascript'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from ckeditor_uploader.views import upload, browse

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path, re_path
from django.views.decorators.cache import never_cache
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    # connect app's endpoints
    path('board/', include('board.urls')),
    path('accounts/', include('allauth.urls')),
    path('', RedirectView.as_view(url='board/', permanent=False)),
    path('sign/', include('sign.urls')),
    re_path(r'^upload/', login_required(upload), name='ckeditor_upload'),
    re_path(r'^browse/', login_required(never_cache(browse)), name='ckeditor_browse'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

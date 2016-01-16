from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^html2pdf/', include('converter.urls')),
    url(r'^admin/', admin.site.urls),
]
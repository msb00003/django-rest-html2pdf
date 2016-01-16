from django.conf.urls import include, url
from django.contrib import admin
from converter import views

urlpatterns = [
    url(r'^html2pdf/(?P<json>.+)/$', views.index), 	
    url(r'^admin/', admin.site.urls),
]

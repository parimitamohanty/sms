from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'mytrip'


urlpatterns = [
    path('', views.home, name='home'),
    # url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    ]
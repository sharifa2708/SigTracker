from django.conf.urls import url
from . import views

app_name = 'main'
urlpatterns = [
    #/main/
    url(r'^', views.index, name='index'),
    #/main/1/
    url(r'^(?P<sig_id>[0-9]+)/$', views.detail, name='detail'),
]
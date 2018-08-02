from django.conf.urls import url
from . import views

app_name = 'main'
<<<<<<< HEAD
urlpatterns = [
    #/main/
    url(r'^', views.index, name='index'),
    #/main/1/
    url(r'^(?P<sig_id>[0-9]+)/$', views.detail, name='detail'),
=======

urlpatterns = [
    url(r'^$', views.index.as_view(), name='index'), # Notice the URL has been named
    url(r'^dev_sig/$', views.dev_sig.as_view(), name='dev_sig'),
    url(r'^ml_sig/$', views.ml_sig.as_view(), name='ml_sig'),
    url(r'^cp_sig/$', views.cp_sig.as_view(), name='cp_sig'),
>>>>>>> 531244f4fc50a5f7af58a82ab52f9b5d7eb22c68
]
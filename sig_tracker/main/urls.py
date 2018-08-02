from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.index.as_view(), name='index'), # Notice the URL has been named
    url(r'^dev_sig/$', views.dev_sig.as_view(), name='dev_sig'),
    url(r'^ml_sig/$', views.ml_sig.as_view(), name='ml_sig'),
    url(r'^cp_sig/$', views.cp_sig.as_view(), name='cp_sig'),
]
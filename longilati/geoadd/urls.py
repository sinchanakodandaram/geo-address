from django.conf.urls import url

from . import views

app_name = "geoadd"

urlpatterns = [
    url('', views.index, name='index'),
]
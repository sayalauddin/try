from django.conf.urls import url, include
from . import views


urlpatterns = [
    url('', view=views.home),
]
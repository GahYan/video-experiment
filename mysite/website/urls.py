from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^everything',views.everything,name='everything'),
    url(r'^preferences',views.preferences,name='preferences'),
]

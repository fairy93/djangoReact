from django.conf.urls import url

from . import views

urlpatterns = [
    url('/signup', views.signup),
    url('/login', views.login)
]

from django.urls import path
from . import views

urlpatterns = [
    path('member/singup',views.member_list)
]


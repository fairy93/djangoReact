from django.conf.urls import url
from .views import Members as members

# from .views import Members as members
urlpatterns = [
    url('/signup', members.as_view()),
    # path('member/singup',views.member_list)

]

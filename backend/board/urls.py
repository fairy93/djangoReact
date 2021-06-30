from django.conf.urls import url
from .views import Posts as posts
from icecream import ic
# from .views import Members as members
urlpatterns = [
    url('/blog', posts.as_view()),
    # path('member/singup',views.member_list)

]

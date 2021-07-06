from django.conf.urls import include, url
# from common.views import Connection

urlpatterns = [
    url(r'^api/member/', include('member.urls')),
]
import logging

logger = logging.getLogger(__name__)
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from bored.rest_viewsets import UserViewSet
from bored.views import login_user, logout_user, login_page, index
user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
})

app_name = 'bookie'
router = DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'^$', index, name='explore'),
    url(r'^login_page/?$', login_page),
    url(r'^user/login/', login_user, name='login_user'),
    url(r'^user/logout/?$', logout_user, name='logout_user'),
    #url(r'^user/email/forgetpw/?$', views.forget_password),  # forget password
    url(r'^api/', include(router.urls)),
]

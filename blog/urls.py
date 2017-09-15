from django.conf.urls import url, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^toggle-like$', views.toggle_like, name='toggle_like'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

#TODO add view for listing likes on blog post

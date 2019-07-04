from django.conf.urls import url, include
from rest_framework import routers
from users.views import SchoolViewSet

router = routers.DefaultRouter()
router.register(r'users', SchoolViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
]
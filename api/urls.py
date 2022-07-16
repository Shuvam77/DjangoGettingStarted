from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, MeetingViewSet


router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', MeetingViewSet, basename='meeting')


urlpatterns = router.urls
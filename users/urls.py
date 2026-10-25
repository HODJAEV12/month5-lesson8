from django.urls import path, include
from .views import UsersViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UsersViewSets, basename='users')

urlpatterns = [
    path('', include(router.urls))
]
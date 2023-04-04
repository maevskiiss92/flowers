from django.urls import path, include
from rest_framework import routers
from .views import FlowersAPIView
router = routers.DefaultRouter()
router = routers.DefaultRouter()
router.register(r'flowers', FlowersAPIView)

urlpatterns = [
    path('', include(router.urls))
]
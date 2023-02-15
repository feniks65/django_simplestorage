from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, FileViewSet

router = DefaultRouter()
router.register(r'files', FileViewSet)

urlpatterns = [
    path('api/auth/register/', UserViewSet.as_view({"post": "register"}), name='register'),
    path('api/auth/login/', UserViewSet.as_view({"post": "login"}), name='login'),
    path('api/', include(router.urls)),
]


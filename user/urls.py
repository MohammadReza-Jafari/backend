from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView

from user.views import RegisterViewSet


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/', RegisterViewSet.as_view({'post': 'create'}), name='register'),
]

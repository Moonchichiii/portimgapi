from django.urls import path
from .views import register, CustomTokenObtainPairView, logout, current_user, get_csrf_token, CustomTokenRefreshView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('current_user/', current_user, name='current_user'),
    path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),
    path('refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]

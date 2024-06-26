from django.urls import path
from .views import ChatBotView,get_csrf_token


urlpatterns = [
    path('', ChatBotView.as_view, name='chatbot'),
    path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),
]
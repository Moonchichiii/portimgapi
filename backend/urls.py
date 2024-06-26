from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/users/', include('users.urls')),
    path('api/profiles/', include('profiles.urls')),
    path('api/blog/', include('blog.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/chatbot/', include('chatbot.urls')),
    path('ws/chat/', include('chat.urls')),
]

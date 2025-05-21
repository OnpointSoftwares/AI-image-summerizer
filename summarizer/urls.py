from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_view, name='chatbot'),
    path('chat/', views.chatbot_ajax, name='chatbot-url'),
    path('chat/clear/', views.clear_chat_history, name='clear-chat'),
    path('chat/history/', views.get_chat_history, name='get-chat-history'),
    path('new-chat/', views.chatbot_view, {'new_chat': True}, name='new-chat'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.create_user),
    path('chat-rooms/', views.create_chat_room),
    path('chat-rooms/<str:room_name>/join/', views.join_chat_room),
    path('chat-rooms/<str:room_name>/messages/', views.get_messages),
    path('chat-rooms/<str:room_name>/messages/', views.send_message),
]

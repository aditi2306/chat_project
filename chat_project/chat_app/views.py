# chat_app/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, ChatRoom, Message
import json

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        user = User.objects.create(username=username)
        return JsonResponse({'username': user.username})
    else:
        # Handle GET requests or other methods if needed
        return JsonResponse({'message': 'This endpoint only accepts POST requests.'})

@csrf_exempt
def create_chat_room(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        room_name = data.get('room_name')
        if ChatRoom.objects.filter(name=room_name).exists():
            return JsonResponse({'message': 'Room already exists'}, status=400)
        chat_room = ChatRoom.objects.create(name=room_name)
        return JsonResponse({'message': 'Chat room created successfully'})
    else:
        # Handle GET requests or other methods if needed
        return JsonResponse({'message': 'This endpoint only accepts POST requests.'})

@csrf_exempt
def join_chat_room(request, room_name):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        try:
            user = User.objects.get(username=username)
            chat_room = ChatRoom.objects.get(name=room_name)
            Message.objects.create(sender=user, chat_room=chat_room, content=f'{username} joined the room')
            return JsonResponse({'message': f'{username} joined the room'})
        except (User.DoesNotExist, ChatRoom.DoesNotExist):
            return JsonResponse({'message': 'User or room not found'}, status=404)
    else:
        # Handle GET requests or other methods if needed
        return JsonResponse({'message': 'This endpoint only accepts POST requests.'})

@csrf_exempt
def send_message(request, room_name):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        content = data.get('content')
        try:
            user = User.objects.get(username=username)
            chat_room = ChatRoom.objects.get(name=room_name)
            Message.objects.create(sender=user, chat_room=chat_room, content=content)
            return JsonResponse({'message': 'Message sent successfully'})
        except (User.DoesNotExist, ChatRoom.DoesNotExist):
            return JsonResponse({'message': 'User or room not found'}, status=404)
    else:
        # Handle GET requests or other methods if needed
        return JsonResponse({'message': 'This endpoint only accepts POST requests.'})

def get_messages(request, room_name):
    try:
        chat_room = ChatRoom.objects.get(name=room_name)
        messages = Message.objects.filter(chat_room=chat_room)
        message_list = [{'sender': message.sender.username, 'content': message.content} for message in messages]
        return JsonResponse(message_list, safe=False)
    except ChatRoom.DoesNotExist:
        return JsonResponse({'message': 'Room not found'}, status=404)

from django.contrib.messages import get_messages

def clear_messages(request):
    storage = get_messages(request)
    for _ in storage:
        pass 
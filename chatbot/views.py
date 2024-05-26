from django.shortcuts import render
from .nvidia import get_chatbot_response

def chatbot_view(request):
    if 'messages' not in request.session:
        request.session['messages'] = []

    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        response = get_chatbot_response(user_input)

        # Append user and bot messages to session
        request.session['messages'].append({'type': 'user', 'text': user_input})
        request.session['messages'].append({'type': 'bot', 'text': response})

        # Ensure the session is saved
        request.session.modified = True

    return render(request, 'chatbot/chat.html', {'messages': request.session['messages']})

from django.shortcuts import render
from django.http import JsonResponse
from .forms import ChatForm
from src.gemini_api import chat_with_gemini
from django.core.files.storage import FileSystemStorage
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import datetime
import re
import json

# Session timeout in seconds (1 hour)
SESSION_TIMEOUT = 3600
DARTMAN_IDENTITY = (
    "You are DartMan, a helpful assistant. When asked who you are, always reply: 'I am DartMan, a helpful assistant.' "
    "Never say you are an AI or a large language model. Always stay in character as DartMan.\n"
)

def clear_chat_history(request):
    """Clear the current chat history"""
    if 'chat_history' in request.session:
        del request.session['chat_history']
    return JsonResponse({'status': 'success'})

def get_chat_history(request):
    """Retrieve the current chat history"""
    return JsonResponse({
        'chat_history': request.session.get('chat_history', []),
        'session_start': request.session.get('session_start')
    })

def chatbot_view(request):
    # Initialize session if it doesn't exist
    if 'session_start' not in request.session:
        request.session['session_start'] = datetime.datetime.now().isoformat()
        request.session.set_expiry(3600)  # Session expires after 1 hour of inactivity
    
    # Initialize chat history if it doesn't exist
    if 'chat_history' not in request.session:
        request.session['chat_history'] = []
    
    chat_history = request.session['chat_history']
    
    # Get current chat ID or initialize if not exists
    current_chat_id = request.session.get('current_chat_id', 0)
    if 'new_chat' in request.GET:
        current_chat_id += 1
        request.session['current_chat_id'] = current_chat_id
        request.session['chat_history'] = []
        chat_history = []
    
    # Store the current chat history
    request.session.modified = True
    image_url = None
    if request.method == 'POST':
        form = ChatForm(request.POST, request.FILES)
        if form.is_valid():
            user_message = form.cleaned_data['message']
            image = form.cleaned_data.get('image')
            chat_history.append({'role': 'user', 'content': user_message})
            bot_reply = chat_with_gemini(
                [{'role': 'user', 'content': DARTMAN_IDENTITY + user_message}] if len(chat_history) == 1 else chat_history
            )
            chat_history.append({'role': 'assistant', 'content': bot_reply})
            if image:
                fs = FileSystemStorage()
                filename = fs.save(image.name, image)
                image_url = fs.url(filename)
            request.session['chat_history'] = chat_history
    else:
        form = ChatForm()
    return render(request, 'summarizer/chat.html', {
        'form': form,
        'chat_history': chat_history,
        'image_url': image_url,
    })

def chatbot_ajax(request):
    if request.method == 'POST':
        # Ensure session is properly initialized
        if 'chat_history' not in request.session:
            request.session['chat_history'] = []
            
        chat_history = request.session['chat_history']
        user_message = request.POST.get('message', '').strip()
        
        if not user_message:
            return JsonResponse({'error': 'Empty message'}, status=400)
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        full_message = f"{DARTMAN_IDENTITY}{user_message}\n{current_time}"
        chat_id = request.session.get('chat_id', 0)
        
        chat_history.append({'role': 'user', 'content': full_message})
        
        
        bot_reply = chat_with_gemini(
            [{'role': 'user', 'content': full_message}] if len(chat_history) == 1 else chat_history
        )
        # Detect code blocks and extract language
        is_code = False
        language = None
        
        # Check for markdown code blocks with language
        md_code_match = re.search(r'```(\w*)\n([\s\S]*?)\n```', bot_reply, re.DOTALL)
        if md_code_match:
            is_code = True
            language = md_code_match.group(1) or 'text'
            # Remove the markdown code block markers for cleaner display
            bot_reply = re.sub(r'```(\w*)\n([\s\S]*?)\n```', r'\2', bot_reply, flags=re.DOTALL)
        # Check for HTML code blocks
        elif re.search(r'<code.*?>.*?</code>', bot_reply, re.DOTALL):
            is_code = True
            language = 'html'
            # Remove HTML code block markers for cleaner display
            bot_reply = re.sub(r'<code.*?>(.*?)</code>', r'\1', bot_reply, flags=re.DOTALL)
        download_url = None
        if "Generated file:" in bot_reply: 
            download_url = "/path/to/generated/file.pdf"  
        image_url = None
        if request.FILES.get('image'):
            image = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            image_url = fs.url(filename)

        # Add assistant's response to chat history
        chat_history.append({
            'role': 'assistant', 
            'content': bot_reply, 
            'is_code': is_code,
            'language': language if is_code else None,
            'timestamp': datetime.datetime.now().isoformat()
        })
        
        # Update session with new chat history
        request.session['chat_history'] = chat_history
        request.session.modified = True  # Ensure session is saved
        
        # Limit chat history to last 20 messages to prevent session from getting too large
        if len(chat_history) > 20:
            request.session['chat_history'] = chat_history[-20:]
            request.session['truncated_messages'] = True

        return JsonResponse({
            'user_message': user_message,
            'bot_reply': bot_reply,
            'is_code': is_code,
            'download_url': download_url,
            'image_url': image_url 
        })
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
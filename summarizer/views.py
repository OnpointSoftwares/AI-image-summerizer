from django.shortcuts import render
from django.http import JsonResponse
from .forms import ChatForm
from src.gemini_api import chat_with_gemini
from django.core.files.storage import FileSystemStorage
import re
DARTMAN_IDENTITY = (
    "You are DartMan, a helpful assistant. When asked who you are, always reply: 'I am DartMan, a helpful assistant.' "
    "Never say you are an AI or a large language model. Always stay in character as DartMan.\n"
)

def chatbot_view(request):
    chat_history = request.session.get('chat_history', [])
    print(chat_history)
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
        chat_history = request.session.get('chat_history', [])
        user_message = request.POST.get('message', '').strip()
        
        if not user_message:
            return JsonResponse({'error': 'Empty message'}, status=400)
        
        # Prepend DartMan identity to the user message
        full_message = DARTMAN_IDENTITY + user_message
        chat_history.append({'role': 'user', 'content': user_message})
        
        # Get the bot's reply
        bot_reply = chat_with_gemini(
            [{'role': 'user', 'content': full_message,'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] if len(chat_history) == 1 else chat_history
        )

        # Check if the bot's reply contains any code
        is_code = False
        if re.search(r'<code.*?>.*?</code>', bot_reply, re.DOTALL) or re.search(r'```.*?```', bot_reply, re.DOTALL):
            is_code = True

        # Handle file generation (you can adjust the logic as per your app)
        download_url = None
        if "Generated file:" in bot_reply:  # Example check for a generated file
            # Here, you'd generate the file or use your logic to provide the correct file URL
            # For example:
            download_url = "/path/to/generated/file.pdf"  # Replace with actual file URL logic

        # If the bot's reply contains an image or other media (simulating a file upload)
        image_url = None
        if request.FILES.get('image'):
            image = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            image_url = fs.url(filename)

        chat_history.append({'role': 'assistant', 'content': bot_reply, 'is_code': is_code})
        
        # Store the updated chat history in the session
        request.session['chat_history'] = chat_history

        # Return the response with bot's reply, code check, and download URL if necessary
        return JsonResponse({
            'user_message': user_message,
            'bot_reply': bot_reply,
            'is_code': is_code,
            'download_url': download_url,
            'image_url': image_url  # Include image URL if an image was uploaded
        })
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
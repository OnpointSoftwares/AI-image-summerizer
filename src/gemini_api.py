import requests

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

# Set your Gemini API key in an environment variable or directly here (NOT RECOMMENDED)
GEMINI_API_KEY = "AIzaSyCYgM0mbrRIzyr8maQRVsQ0qlGZaRS71pg" # Set this securely!

def summarize_text(text, api_key=None):
    """Send text to Gemini API and return the summary."""
    key = api_key or GEMINI_API_KEY
    if not key:
        raise ValueError("Gemini API key not set.")
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": text}]}],
        "generationConfig": {"maxOutputTokens": 128}
    }
    params = {"key": key}
    response = requests.post(GEMINI_API_URL, headers=headers, params=params, json=data)
    response.raise_for_status()
    result = response.json()
    try:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        return "[Gemini API: Unable to summarize]"

def chat_with_gemini(chat_history, api_key=None):
    """Send chat history to Gemini API and return the assistant's reply."""
    key = api_key or GEMINI_API_KEY
    if not key:
        raise ValueError("Gemini API key not set.")
    headers = {"Content-Type": "application/json"}
    contents = []
    for msg in chat_history:
        contents.append({"role": msg["role"], "parts": [{"text": msg["content"]}]})
    data = {
        "contents": contents,
        "generationConfig": {"maxOutputTokens": 256}
    }
    params = {"key": key}
    response = requests.post(GEMINI_API_URL, headers=headers, params=params, json=data)
    response.raise_for_status()
    result = response.json()
    try:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        return "[Gemini API: Unable to generate response]"

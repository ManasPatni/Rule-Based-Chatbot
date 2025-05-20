import re
import httpx

# WARNING: Never hardcode your API key in production!
GROQ_API_KEY = "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"

def get_llm_response(user_input):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": user_input}],
        "temperature": 0.7
    }

    try:
        response = httpx.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"⚠️ Error from LLM: {str(e)}"

def get_response(user_input):
    rules = {
        r"(?i)\bhello\b|\bhi\b": "Hello! How can I help you?",
        r"(?i)\bhow are you\b": "I'm just a bot, but I'm doing great!",
        r"(?i)\bwhat is your name\b": "I'm a chatbot created by Manas.",
        r"(?i)\bbye\b|\bgoodbye\b": "Goodbye! Have a great day!",
        r"(?i)\bhelp\b": "Sure, I'm here to help. Ask me anything!"
    }

    for pattern, response in rules.items():
        if re.search(pattern, user_input):
            return response

    # Always fallback to LLaMA 3 for unmatched queries
    return get_llm_response(user_input)

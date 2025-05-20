from chatbot import get_response

def test_greeting():
    assert get_response("hello") == "Hello! How can I help you?"

def test_name_query():
    assert get_response("what is your name") == "I'm a chatbot created by Manas."

def test_fallback_response():
    response = get_response("Who is the president of India?")
    assert isinstance(response, str) and len(response) > 0

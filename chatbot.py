import cohere
import os
from dotenv import load_dotenv

load_dotenv()
cohere_token = os.getenv('cohere_token')
chat_history = []
co = cohere.Client(cohere_token)

def emotion_message(emotion):
    message = "please respond as if you are a friend conversation style; respond how a person would respond in real life if I am a person and I look " + emotion
    
    response = co.chat(
        message,
        model = "command",
        temperature = 0.9,
        
    )
    response = response.text
    user_message = {"user_name": "User", "text": message}
    bot_message = {"user_name": "Chatbot", "text": response}
        
    chat_history.append(user_message)
    chat_history.append(bot_message)

    message = "talk as if you see someone " + emotion
    response = co.chat(
        message,
        model = "command",
        temperature = 0.9,
        
    )
    response = response.text
    user_message = {"user_name": "User", "text": message}
    bot_message = {"user_name": "Chatbot", "text": response}
        
    chat_history.append(user_message)
    chat_history.append(bot_message)
    
    print(response)
    return response


def general_questions(message):
    response = co.chat(
        message,
        temperature = 0.9,
        chat_history = chat_history,
        
    )
    response = response.text
    print(response, "\n")

    user_message = {"user_name": "User", "text": message}
    bot_message = {"user_name": "Chatbot", "text": response}
    
    chat_history.append(user_message)
    chat_history.append(bot_message)

    print(response)
    return response


emotion_message("happy")

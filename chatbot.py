import cohere
from main import emotion
api_token = "sd2Smgp5jfEcah7lt0PzqkIeTt1G5dEjFgCcc60x"

co = cohere.Client(api_token)

chat_history = []

message = "please respond as if you are a friend to the following messages, respond how a person would respond in real life if I am a person and I look " + emotion

response = co.chat(
        message,
        model = "command",
        temperature = 0.9
    )
response = response.text
user_message = {"user_name": "User", "text": message}
bot_message = {"user_name": "Chabot", "text": response}
    
chat_history.append(user_message)
chat_history.append(bot_message)


print(response)


while(message != "end"):
    message = input()
    response = co.chat(
        message,
        temperature = 0.9,
        chat_history = chat_history
    )
    response = response.text
    print(response, "\n")

    user_message = {"user_name": "User", "text": message}
    bot_message = {"user_name": "Chabot", "text": response}
    
    chat_history.append(user_message)
    chat_history.append(bot_message)




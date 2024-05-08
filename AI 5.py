# Develop an elementary chatbot for any suitable customer 

# interaction application

import random

responses = {
    "hi": ["Hello!", "Hi there!", "Hi!"],
    "how are you": ["I'm doing well, thank you!", "I'm fine, thanks for asking.", "I'm good, thanks!"],
    "what's your name": ["My name is Chatbot.", "I'm Chatbot!", "I'm  just a simple chatbot without a name."],
    "bye": ["Goodbye!", "See you later!", "Have a nice day!"],
    "thank you": ["You're welcome!", "No problem!", "Anytime!"],
    "default": ["I'm sorry, I don't understand.", "Can you please rephrase that?", 
                "I'm not sure what you mean."]
}

def chatbot():
    print(random.choice(responses["hi"]))
    while True:
        message = input("> ")
        if "hi" in message.lower():
            print(random.choice(responses["hi"]))
            
        elif "how are you" in message.lower():
            print(random.choice(responses["how are you"]))
            
        elif "what's your name" in message.lower():
            print(random.choice(responses["what's your name"]))
            
        elif "bye" in message.lower():
            print(random.choice(responses["bye"]))
            
            break
        
        elif "thank" in message.lower():
            
            print(random.choice(responses["thank you"]))
            
        else:
            print(random.choice(responses["default"]))
            
chatbot()





# 2nd backup code

# import nltk
# from nltk.chat.util import Chat, reflections

# # Define pairs of patterns and responses for the chatbot
# pairs = [
#     [
#         "hi",
#         ["Hello!", "Hey there!", "Hi!"]
#     ],
#     [
#         "how are you ?",
#         ["I'm doing well, thank you!", "I'm good, thanks for asking.", "I'm fine, how about you?"]
#     ],
#     [
#         "what is your name ?",
#         ["You can call me ChatBot.", "I'm ChatBot!", "My name is ChatBot."]
#     ],
#     [
#         "what can you do ?",
#         ["I can help you with pizza orders, weather information, and more! Just ask."]
#     ],
#     [
#         "weather in",
#         ["The weather is perfect!", "It's sunny right now."]
#     ],
#     [
#         "order pizza",
#         ["Sure, what type and size of pizza would you like to order?"]
#     ],
#     [
#         "thank you",
#         ["You're welcome!", "No problem!", "Anytime!"]
#     ],
#     [
#         "quit",
#         ["Bye! Take care.", "Goodbye! See you later.", "Come back soon!"]
#     ]
# ]

# # Create a chatbot using the defined pairs
# chatbot = Chat(pairs, reflections)

# # Start interacting with the user
# print("Welcome to ChatBot!")
# while True:
#     user_input = input("You: ")
#     response = chatbot.respond(user_input)
#     print("ChatBot:", response)
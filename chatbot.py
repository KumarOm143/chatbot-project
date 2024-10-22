import nltk
from nltk.chat.util import Chat, reflections
import random

# Sample pairs of input and output
pairs = [
    ['hi', 'hello'],
    ['how are you?', 'I am good, thank you! How about you?'],
    ['what is your name?', 'I am a chatbot created for this project.'],
    ['bye', 'Goodbye! Have a great day!'],
    ['tell me a joke', 'Why don’t scientists trust atoms? Because they make up everything!'],
    ['what is your favorite color?', 'I love all colors! But I think blue is quite calming.'],
    ['what can you do?', 'I can chat with you, tell jokes, and answer simple questions!'],
    ['who created you?', 'I was created as part of a chatbot development project.'],
    ['what is your purpose?', 'My purpose is to assist and entertain you with conversation!'],
    ['tell me about yourself', 'I am a simple chatbot designed to have fun conversations!'],
    ['help', 'Sure! You can ask me questions or just chat with me.'],
    ['how is the weather?', 'I am not sure about the weather, but I hope it’s nice outside!'],
    ['what is your favorite food?', 'I don’t eat, but if I could, I think I’d love pizza!'],
]


# Function to handle unknown user input
def unknown_response():
    responses = [
        "I'm sorry, I don't understand that.",
        "Can you rephrase that?",
        "I'm not sure how to respond to that.",
        "That's interesting! Can you tell me more?",
    ]
    return random.choice(responses)


# Function to start the chat
def start_chat():
    print("Chatbot: Hello! How can I help you today?")
    print("Type 'bye' to exit the chat.")

    while True:
        user_input = input("You: ").lower()

        if user_input == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Check for predefined responses
        response_found = False
        for pair in pairs:
            if user_input in pair[0]:
                print("Chatbot:", pair[1])
                response_found = True
                break

        # If no predefined response is found, use unknown response
        if not response_found:
            print("Chatbot:", unknown_response())


if __name__ == "__main__":
    start_chat()

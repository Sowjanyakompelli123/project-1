import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
# Using reflections helps to convert input pronouns to correct responses, like "I'm" to "you are"
pairs = [
    [
        r"(hi|hello|hey)",
        ["Hello!", "Hi there!", "Hey! How can I help you today?"]
    ],
    [
        r"how are you(.*)?",
        ["I'm here to help you! How can I assist you?", "I'm a chatbot, so I don't have feelings, but thanks for asking!"]
    ],
    [
        r"what is your name?",
        ["I'm a chatbot created by a Python enthusiast. You can call me Chatbot!"]
    ],
    [
        r"who created you?",
        ["I was created by a Python programmer using the NLTK library."]
    ],
    [
        r"can you help me with (.*)?",
        ["I'll do my best to help you with %1! Could you tell me more about it?", "I’d love to help you with %1! Let's discuss it."]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a nice day!", "See you soon!", "Take care!"]
    ],
    [
        r"(.*)",
        ["I'm not sure how to respond to that. Could you tell me more?", "Interesting. Can you tell me more?", "I see. How can I assist you further?"]
    ]
]

# Create a Chat instance with pairs and reflections
chatbot = Chat(pairs, reflections)

# Function to start conversation with the chatbot
def start_chat():
    print("Hello! I'm your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

# Run the chatbot
start_chat()
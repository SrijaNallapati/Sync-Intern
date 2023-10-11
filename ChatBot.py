import random  

# Define a list of predefined responses
responses = {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thanks!", "I'm doing well, how about you?"],
    "what is your name": ["My name Virtual assistant"],
    "tell me a joke": ["The right eye said to the left eye - between you and me something smells", "What's orange and sounds like a parrot - A carrot"],
    "what is the full form of google?": ["Google stands for Global organization of oriented group language of earth"],
    "what is the weather today": ["It's 28 and partly cloudy", "it's 33  and mostly sunny"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["I'm not sure what you mean.", "Could you please rephrase that?"]
}

# Function to get a response from the chatbot
def get_response(input_text):
    # Convert input to lowercase for case-insensitive matching
    input_text = input_text.lower() 

    # Check if the input matches any predefined responses
    if input_text in responses:
        return random.choice(responses[input_text])
    else:
        return random.choice(responses["default"])

# Main chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)

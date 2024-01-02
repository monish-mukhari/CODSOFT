import re

def simple_chatbot(user_input):

    user_input = user_input.lower()


    if re.search(r'\b(hi|hello|hey)\b', user_input):
        return "Hello! How can I help you today?"

    elif re.search(r'\b(how are you|how do you do)\b', user_input):
        return "I'm just a computer program, but thanks for asking! How can I assist you?"

    elif re.search(r'\b(goodbye|bye|see you)\b', user_input):
        return "Goodbye! Have a great day!"

    elif re.search(r'\b(weather|temperature)\b', user_input):
        return "I'm sorry, I don't have real-time weather information. You can check a weather website or app for the current conditions."

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask another question?"

# Example usage:
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)

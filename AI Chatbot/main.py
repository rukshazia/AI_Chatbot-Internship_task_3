from datetime import datetime

def get_reply(msg):
    msg = msg.lower()

    if "hello" in msg or "hi" in msg:
        return "Hi! How can I help you today?"
    elif "how are you" in msg:
        return "I'm fine, thanks! How about you?"
    elif "what is your name?" in msg:
        return "i dont have a name. I am a simple AI chatbot."
    elif "time" in msg or "what is the time" in msg:
        return "The current time is " + datetime.now().strftime("%I:%M %p")
    elif "day" in msg or "what day is it" in msg or "tell me the day" in msg:
        return "Today is " + datetime.now().strftime("%A") + "."
    elif "bye" in msg:
        return "Goodbye! Have a great day."
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"


print("Chatbot: Hi! Type 'bye' to end the chat.\n")

while True:
    user_input = input("You: ")
    reply = get_reply(user_input)
    print("Chatbot:", reply)

    if "bye" in user_input.lower():
        break
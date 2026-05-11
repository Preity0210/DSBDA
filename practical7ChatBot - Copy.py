print("Chatbot: Hello! Type 'bye' to stop.")

while True:

    user = input("You: ").lower()

    if user == "hello":
        print("Chatbot: Hi!")

    elif user == "how are you":
        print("Chatbot: I am fine.")

    elif user == "your name":
        print("Chatbot: I am AI Chatbot.")

    elif user == "bye":
        print("Chatbot: Goodbye!")
        break

    else:
        print("Chatbot: Sorry, I don't understand.")
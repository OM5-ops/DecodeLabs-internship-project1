print("=" * 40)
print("      SIMPLE AI CHATBOT")
print("=" * 40)
print("Type 'exit' to end the chat.\n")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am doing great!")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "your name":
        print("Bot: My name is ChatBot.")

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")
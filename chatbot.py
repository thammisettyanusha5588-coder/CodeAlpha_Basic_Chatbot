import datetime

def chatbot():
    print("=" * 50)
    print("🤖 WELCOME TO SMART CHATBOT")
    print("Type 'help' to see commands")
    print("Type 'bye' to exit")
    print("=" * 50)

    while True:
        user = input("\nYou: ").lower().strip()

        if user == "hello":
            print("Bot: Hello! Nice to meet you 😊")

        elif user == "how are you":
            print("Bot: I am doing great! Thanks for asking 😄")

        elif user == "what is your name":
            print("Bot: My name is SmartBot 🤖")

        elif user == "time":
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print("Bot: Current Time is", current_time)

        elif user == "date":
            current_date = datetime.datetime.now().strftime("%d-%m-%Y")
            print("Bot: Today's Date is", current_date)

        elif user == "help":
            print("\nAvailable Commands:")
            print("• hello")
            print("• how are you")
            print("• what is your name")
            print("• time")
            print("• date")
            print("• bye")

        elif user == "bye":
            print("Bot: Goodbye! Have a wonderful day 👋")
            break

        else:
            print("Bot: Sorry, I don't understand that command.")

chatbot()
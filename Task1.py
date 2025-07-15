def chatbot():
    print("chatbot: Hello! How can I help you today? (Type 'bye' to exit)")
    while True:
        user_input = input("You:").lower()
        if user_input in ['hi','hello','hey']:
            print("Chatbot: Hello there!")
        elif 'your name' in user_input:
            print("Chatbot: I'm a simple rule-based chatbot.")
        elif 'how are you' in user_input:
            print("Chatbot: I'm just code, but i'm doing great! How about you?")
        elif 'help' in user_input:
            print("Chatbot: Sure, I can help! Ask me about time, weather,or just say hi.")
        elif 'time' in user_input:
            from datetime import datetime
            print(f"Chatbot: The current time is {datetime.now().strftime('%H:%M:%S;')}.")
        elif 'weather' in user_input:
            print("Chatbot: I can't check the weather right now, but it's always a good day to code!")
        elif user_input in['bye','exit','quit']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: Sorry, I didn't understand that. Try asking something else.")
chatbot()
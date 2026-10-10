# Rule-based chatbot
def chatbot():
    print("Hello! I am your customer support bot. Type 'exit' to leave.")

    # Predefined responses
    responses = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hi there! How can I assist you?",
        "price": "Our products range from $10 to $100. Which product are you interested in?",
        "product": "We have laptops, phones, and accessories. Which one would you like?",
        "payment": "We accept credit cards, debit cards, and PayPal.",
        "shipping": "Shipping takes 3-5 business days.",
        "return": "You can return products within 30 days of purchase.",
        "thanks": "You’re welcome! Is there anything else I can help you with?",
        "thank you": "Happy to help! Let me know if you need anything else."
    }

    while True:
        user_input = input("You: ").lower()  # Convert input to lowercase
        if user_input == "exit":
            print("Bot: Thank you for visiting. Goodbye!")
            break

        found_response = False
        for keyword, response in responses.items():
            if keyword in user_input:
                print("Bot:", response)
                found_response = True
                break

        if not found_response:
            print("Bot: I'm sorry, I didn't understand that. Can you please rephrase?")

# Run the chatbot
chatbot()

def process_input(user_input):
    if user_input is None:
        return "Sorry, I didn’t catch that. Can you repeat?"

    user_input = user_input.lower()

    if "hi" in user_input or "hello" in user_input:
        return "Hello! Welcome to Guru Smart Services. Are you looking for car wash, home cleaning, or salon appointment?"

    elif "car" in user_input:
        return "Awesome! Please tell your city or location for the car wash."

    elif "home" in user_input:
        return "Great choice! We offer full home cleaning. May I know your area?"

    elif "salon" in user_input or "appointment" in user_input:
        return "Sure, we can book salon appointments too. What date and time would you prefer?"

    elif "bye" in user_input or "thank you" in user_input:
        return "Thank you for calling Guru Smart Services. Have a great day!"

    else:
        return "I’m here to help. Please tell me the service you want."

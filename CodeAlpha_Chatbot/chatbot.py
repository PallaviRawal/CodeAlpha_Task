import json
import random

with open("training_data.json") as file:
    data = json.load(file)

def get_response(user_input):
    user_input = user_input.lower()

    for intent in data.values():
        for pattern in intent["patterns"]:
            if pattern in user_input:
                return random.choice(intent["responses"])

    return "Sorry, I didn't understand that. Can you rephrase?"

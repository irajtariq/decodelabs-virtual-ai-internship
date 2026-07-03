"""
Project 1: Rule-Based AI Chatbot
DecodeLabs Internship
Made by: Iraj Tariq

A simple chatbot that uses a dictionary of known "intents" (keywords) mapped to responses.
It runs in a loop, cleans up user input, and exits cleanly on a command like "bye" or "exit".

Extra Upgrades I Added:
- More keywords (jokes, weather small talk, personality)
- Random reply variation for "how are you" using random.choice()
- Repeat-greeting detection using a conversation counter
"""

import random

# 1. KNOWLEDGE BASE

# Each key is a keyword/intent the bot listens for.
# Each value is the response the bot gives when it hears that keyword.

knowledge_base = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Nice to see you.",
    "how are you": None,  # handled later specially with random.choice()
    "your name": "I'm ChatBot 1.0, built for the DecodeLabs internship by Iraj Tariq.",
    "help": "I can chat about greetings, my name, jokes, or the weather. Try me!",
    "thank you": "You're welcome!",
    "thanks": "No problem at all!",
    "joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
    "weather": "I can't check outside, but I hope it's sunny where you are!",
    "who made you": "I was built during a DecodeLabs internship project by Iraj Tariq!",
}

# A few different replies for "how are you":
how_are_you_replies = [
    "I'm just a bunch of if-else statements, but I'm doing great!",
    "Running smoothly, thanks for asking!",
    "Can't complain — I don't have feelings, but I appreciate you asking!",
]

# Words to end the conversation:
exit_commands = ["bye", "exit", "quit", "goodbye"]

# Greeting words:
greeting_words = ["hello", "hi"]


# 2. INTENT MATCHING FUNCTION

def get_response(user_input, greeting_count):
    """
    Checks the cleaned user input against the knowledge base.
    Returns a matching response, or a fallback if nothing matches.
    'greeting_count' lets us change the reply if the user keeps saying hello/hi over and over.
    """
    # Sanitization:
    cleaned = user_input.lower().strip()

    # Special case with random reply:
    if "how are you" in cleaned:
        return random.choice(how_are_you_replies)

    # Special case: repeated greeting -> nested condition
    for word in greeting_words:
        if word in cleaned:
            if greeting_count == 0:
                return "Hi there! How can I help you today?"
            elif greeting_count == 1:
                return "You said hi again! Are we starting over? 😄"
            else:
                return "Okay, we've said hello a lot now — what do you actually need help with?"

    # Check the rest of the knowledge base
    for keyword, response in knowledge_base.items():
        if keyword in ("how are you",) or keyword in greeting_words:
            continue
        if keyword in cleaned:
            return response

    # Fallback:
    return "Sorry, I didn't understand that. Could you rephrase?"


# 3. MAIN CHAT LOOP

def run_chatbot():
    print("=" * 50)
    print(" Welcome to AI ChatBot 1.0 (type 'bye' to exit)")
    print("=" * 50)

    greeting_count = 0  # tracks amount of times user greets bot
    while True:  # continuous input loop
        user_input = input("You: ")

        # Sanitization:
        cleaned_input = user_input.lower().strip()

        # Exit Strategy:
        if cleaned_input in exit_commands:
            print("Bot: Goodbye! Have a great day.")
            break  # exits while loop

        # Empty input handling
        if cleaned_input == "":
            print("Bot: ...I didn't quite catch that. Try typing something!")
            continue

        if any(word in cleaned_input for word in greeting_words):
            response = get_response(user_input, greeting_count)
            greeting_count += 1
        else:
            response = get_response(user_input, greeting_count)

        print(f"Bot: {response}")


# 4. RUN THE PROGRAM

if __name__ == "__main__":
    run_chatbot()

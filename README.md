# Project 1: Rule-Based AI Chatbot

A simple terminal-based chatbot that responds to predefined user inputs using rule-based (if-else / dictionary) logic — no machine learning involved. This project focuses on control flow, decision-making logic, and the foundational concepts that more advanced AI systems build on.

## Features
- Continuous input loop — keeps the conversation going until the user exits
- Input sanitization — handles different casing and extra whitespace
- Knowledge base of 10 intents (greetings, jokes, weather, thanks, etc.)
- Fallback response for unrecognized input
- Clean exit on commands like `bye`, `exit`, `quit`
- Randomized replies for "how are you" so the bot doesn't repeat itself
- Greeting counter — the bot responds differently if you say hi multiple times

## Tech Used
- Python 3.x (standard library only — `random` module)

## How to Run
```bash
python3 chatbot.py
```

Then just start typing. Type `bye`, `exit`, or `quit` to end the conversation.

## Sample Conversation

You: hello

Bot: Hi there! How can I help you today?

You: how are you

Bot: Running smoothly, thanks for asking!

You: joke

Bot: Why do programmers prefer dark mode? Because light attracts bugs!

You: asdkjaskjd

Bot: Sorry, I didn't understand that. Could you rephrase?

You: bye

Bot: Goodbye! Have a great day.

## What I Learned
- Structuring conversational logic using dictionaries instead of long if-else chains
- Why input sanitization matters even in simple systems
- Handling edge cases (empty input, repeated commands) without crashing
- Designing a clean exit path for a continuous loop

## Possible Future Improvements
- Add more intents / broaden vocabulary
- Store conversation history to a log file
- Add a lightweight UI (Streamlit) in a later iteration
"""Task B: A simple terminal QA bot using input and if/elif/else.

Run on Linux: python3 qa_bot.py
"""

import re


def main():
    print("Ask me about HKU, robot, Jetson, AI, or human.")
    print("Type 'quit' to stop.\n")

    while True:
        try:
            question = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye!")
            break

        # Extract whole English words, so 'AI' does not accidentally match 'chair'.
        words = set(re.findall(r"[a-z]+", question.lower()))

        if "quit" in words or "exit" in words:
            print("Bot: Goodbye!")
            break
        elif "hku" in words:
            print("Bot: HKU stands for the University of Hong Kong.")
        elif "robot" in words or "robots" in words:
            print("Bot: A robot senses its surroundings and performs actions.")
        elif "jetson" in words:
            print("Bot: Jetson Nano is a small computer for edge AI projects.")
        elif "ai" in words:
            print("Bot: AI helps computers do tasks such as image recognition.")
        elif "human" in words or "humans" in words:
            print("Bot: Humans can learn, reason, and make decisions.")
        else:
            print("Bot: Try asking about HKU, robot, Jetson, AI, or human.")


if __name__ == "__main__":
    main()

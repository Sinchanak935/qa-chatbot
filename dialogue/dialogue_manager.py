class DialogueManager:

    def __init__(self):
        self.last_question = None
        self.last_answer = None
        self.running = True

    def handle_message(self, message):

        message = message.strip()

        if not message:
            return "Please enter a question."

        # Greeting
        greetings = [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good afternoon",
            "good evening"
        ]

        if message.lower() in greetings:
            return "Hello! 👋 Ask me a question and I'll try to answer it."

        # Thanks
        thanks = [
            "thanks",
            "thank you",
            "thankyou"
        ]

        if message.lower() in thanks:
            return "You're welcome! 😊"

        # Goodbye
        goodbyes = [
            "bye",
            "goodbye",
            "exit",
            "quit"
        ]

        if message.lower() in goodbyes:
            self.running = False
            return "Goodbye! 👋"

        # Simple follow-up
        if (
            message.lower().startswith("what about")
            and self.last_question
        ):
            return (
                "That's a follow-up question. "
                "We'll connect this to the QA system next."
            )

        self.last_question = message

        return None


if __name__ == "__main__":

    dialogue = DialogueManager()

    print("Chatbot started!")
    print("Type 'bye' to exit.")

    while dialogue.running:

        user_message = input("\nYou: ")

        response = dialogue.handle_message(
            user_message
        )

        if response:
            print("Bot:", response)
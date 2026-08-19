from qa_engine import QAEngine
from dialogue.dialogue_manager import DialogueManager


class Chatbot:

    def __init__(self):

        print("Initializing chatbot...")

        self.qa_engine = QAEngine()

        self.dialogue = DialogueManager()

        print("Chatbot ready!")


    def respond(self, message):

        # First let dialogue manager handle
        dialogue_response = (
            self.dialogue.handle_message(message)
        )

        # If dialogue manager has a response,
        # return it
        if dialogue_response:

            return dialogue_response


        # Otherwise send question to QA engine
        result = self.qa_engine.answer(
            message
        )

        answer = result["answer"]

        confidence = result["confidence"]

        # Save answer for dialogue
        self.dialogue.last_answer = answer


        # Low confidence
        if confidence < 0.20:

            return (
                "I'm not very confident about that answer. "
                "I found: " + answer
            )


        return answer


if __name__ == "__main__":

    chatbot = Chatbot()

    print("\n==============================")
    print("QA CHATBOT")
    print("==============================")

    print(
        "Ask questions about science, "
        "geography, and history."
    )

    print("Type 'bye' to exit.")


    while chatbot.dialogue.running:

        user_message = input("\nYou: ")

        response = chatbot.respond(
            user_message
        )

        print("Bot:", response)
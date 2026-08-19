import re

from knowledge_base import KnowledgeBase


class KnowledgeQA:

    def __init__(self):

        self.kb = KnowledgeBase()


    def answer(self, question):

        question_lower = question.lower()


        # Capital questions
        if "capital" in question_lower:

            countries = [
                "India",
                "France",
                "Japan",
                "Australia"
            ]

            for country in countries:

                if country.lower() in question_lower:

                    answer = self.kb.query(
                        country,
                        "capital"
                    )

                    if answer:

                        return {
                            "answer": answer,
                            "confidence": 1.0,
                            "source": "SQLite Knowledge Base"
                        }


        # Continent questions
        if "continent" in question_lower:

            countries = [
                "India",
                "France",
                "Japan",
                "Australia"
            ]

            for country in countries:

                if country.lower() in question_lower:

                    answer = self.kb.query(
                        country,
                        "continent"
                    )

                    if answer:

                        return {
                            "answer": answer,
                            "confidence": 1.0,
                            "source": "SQLite Knowledge Base"
                        }


        return {
            "answer": None,
            "confidence": 0.0,
            "source": None
        }


if __name__ == "__main__":

    qa = KnowledgeQA()

    questions = [
        "What is the capital of India?",
        "What is the capital of Japan?",
        "Which continent is France in?"
    ]

    for question in questions:

        result = qa.answer(question)

        print("\nQuestion:", question)
        print("Answer:", result["answer"])
        print("Source:", result["source"])
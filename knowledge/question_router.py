class QuestionRouter:

    def route(self, question):

        question_lower = question.lower()

        knowledge_keywords = [
            "capital",
            "continent",
            "occupation"
        ]

        for keyword in knowledge_keywords:

            if keyword in question_lower:

                return "knowledge"

        return "document"
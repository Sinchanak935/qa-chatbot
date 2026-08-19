from retrieval.retriever import Retriever
from qa.factoid_qa import FactoidQA


class QAEngine:

    def __init__(self):

        print("Starting QA system...")

        self.retriever = Retriever()

        self.qa = FactoidQA()

        print("QA system ready!")


    def answer(self, question):

        print("\nSearching documents...")

        results = self.retriever.search(
            question,
            top_k=3
        )

        if not results:

            return {
                "answer": "I could not find an answer.",
                "confidence": 0.0,
                "source": None,
                "passage": None
            }


        # Highest-ranked passage
        best_result = results[0]

        print(
            "Best source:",
            best_result["source"]
        )

        print(
            "Retrieval score:",
            round(best_result["score"], 3)
        )


        # Extract answer from passage
        qa_result = self.qa.answer(
            question,
            best_result["text"]
        )


        return {
            "answer": qa_result["answer"],
            "confidence": qa_result["score"],
            "retrieval_score": best_result["score"],
            "source": best_result["source"],
            "passage": best_result["text"]
        }


if __name__ == "__main__":

    engine = QAEngine()

    question = "Who developed the theory of relativity?"

    result = engine.answer(question)


    print("\n==============================")
    print("QUESTION")
    print("==============================")

    print(question)


    print("\n==============================")
    print("ANSWER")
    print("==============================")

    print(result["answer"])


    print("\n==============================")
    print("QA CONFIDENCE")
    print("==============================")

    print(
        round(result["confidence"], 3)
    )


    print("\n==============================")
    print("RETRIEVAL SCORE")
    print("==============================")

    print(
        round(result["retrieval_score"], 3)
    )


    print("\n==============================")
    print("SOURCE")
    print("==============================")

    print(result["source"])


    print("\n==============================")
    print("PASSAGE")
    print("==============================")

    print(result["passage"])
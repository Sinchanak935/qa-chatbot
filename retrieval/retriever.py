import os
import glob

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Retriever:

    def __init__(self, data_folder="data/documents"):

        self.documents = []
        self.sources = []

        files = glob.glob(
            os.path.join(data_folder, "*.txt")
        )

        for file in files:

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                text = f.read()

            # Keep paragraphs instead of splitting every sentence
            paragraphs = [
                p.strip()
                for p in text.split("\n\n")
                if p.strip()
            ]

            for paragraph in paragraphs:

                self.documents.append(paragraph)

                self.sources.append(
                    os.path.basename(file)
                )

        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english"
        )

        self.document_vectors = (
            self.vectorizer.fit_transform(
                self.documents
            )
        )


    def search(self, query, top_k=3):

        query_vector = self.vectorizer.transform(
            [query]
        )

        similarities = cosine_similarity(
            query_vector,
            self.document_vectors
        )[0]

        ranked_indices = (
            similarities.argsort()[::-1][:top_k]
        )

        results = []

        for index in ranked_indices:

            results.append({
                "text": self.documents[index],
                "source": self.sources[index],
                "score": float(
                    similarities[index]
                )
            })

        return results


if __name__ == "__main__":

    retriever = Retriever()

    question = "Who developed the theory of relativity?"

    results = retriever.search(
        question,
        top_k=3
    )

    print("\nQuestion:")
    print(question)

    print("\nRetrieved passages:")

    for result in results:

        print("\n-----------------------------")

        print(
            "Source:",
            result["source"]
        )

        print(
            "Similarity:",
            round(result["score"], 3)
        )

        print(
            "Passage:",
            result["text"]
        )
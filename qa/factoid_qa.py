from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch


class FactoidQA:

    def __init__(self):

        print("Loading QA model...")

        model_name = "distilbert-base-cased-distilled-squad"

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name
        )

        self.model = AutoModelForQuestionAnswering.from_pretrained(
            model_name
        )

        print("QA model loaded!")


    def answer(self, question, context):

        inputs = self.tokenizer(
            question,
            context,
            return_tensors="pt",
            truncation=True,
            max_length=512
        )

        with torch.no_grad():

            outputs = self.model(**inputs)

        start_logits = outputs.start_logits
        end_logits = outputs.end_logits

        start_position = torch.argmax(
            start_logits
        )

        end_position = torch.argmax(
            end_logits
        )

        if end_position < start_position:

            end_position = start_position

        answer_tokens = inputs["input_ids"][
            0,
            start_position:end_position + 1
        ]

        answer = self.tokenizer.decode(
            answer_tokens,
            skip_special_tokens=True
        )

        start_probability = torch.softmax(
            start_logits,
            dim=1
        )[0, start_position]

        end_probability = torch.softmax(
            end_logits,
            dim=1
        )[0, end_position]

        confidence = (
            start_probability * end_probability
        ).item()

        return {
            "answer": answer,
            "score": confidence
        }


if __name__ == "__main__":

    qa = FactoidQA()

    question = "Who discovered penicillin?"

    context = (
        "Penicillin was discovered by Alexander Fleming "
        "in 1928. Fleming was a Scottish physician "
        "and bacteriologist."
    )

    result = qa.answer(
        question,
        context
    )

    print("\n============================")
    print("QUESTION")
    print("============================")
    print(question)

    print("\n============================")
    print("ANSWER")
    print("============================")
    print(result["answer"])

    print("\n============================")
    print("CONFIDENCE")
    print("============================")
    print(round(result["score"], 3))
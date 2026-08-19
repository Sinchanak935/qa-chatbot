import streamlit as st

from chatbot import Chatbot


st.set_page_config(
    page_title="QA Chatbot",
    page_icon="🤖"
)


st.title("🤖 Multi-Source QA Chatbot")

st.write(
    "Ask questions about science, history, "
    "geography, and general facts."
)


if "chatbot" not in st.session_state:

    st.session_state.chatbot = Chatbot()


if "messages" not in st.session_state:

    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )


user_question = st.chat_input(
    "Ask a question..."
)


if user_question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    with st.chat_message("user"):

        st.write(user_question)


    with st.chat_message("assistant"):

        with st.spinner(
            "Finding the answer..."
        ):

            result = (
                st.session_state
                .chatbot
                .respond(user_question)
            )


        # Handle chatbot result

        if isinstance(result, dict):

            answer = result.get(
                "answer",
                "I couldn't find an answer."
            )

            confidence = result.get(
                "confidence",
                0.0
            )

            source = result.get(
                "source",
                "Unknown"
            )

        else:

            answer = str(result)

            confidence = 0.0

            source = "Unknown"


        st.write(answer)

        st.caption(
            f"Source: {source}"
        )

        st.caption(
            f"Confidence: {confidence:.2f}"
        )


    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
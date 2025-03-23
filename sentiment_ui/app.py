import streamlit as st
import requests

# API endpoints
API_URL = "http://127.0.0.1:8000/analyze"
FEEDBACK_URL = "http://127.0.0.1:8000/feedback"
FINE_TUNE_URL = "http://127.0.0.1:8000/fine-tune"
UPLOAD_URL = "http://127.0.0.1:8000/upload"

def main():
    st.title("Sentiment Analysis Engine")
    st.write("Enter text to analyze sentiment and classify the text.")

    # Input field
    text_input = st.text_area("Enter your text here:", "I love this new phone! It's amazing.")

    # Analyze button
    if st.button("Analyze"):
        if text_input:
            try:
                # Make a POST request to the API with JSON payload
                payload = {"text": text_input}
                response = requests.post(API_URL, json=payload)
                response.raise_for_status()  # Raise an error for bad status codes

                # Parse the response
                result = response.json()
                sentiment_score = result["sentiment_score"]
                category = result["category"]

                # Display results
                st.subheader("Results")
                st.write(f"**Sentiment Score:** {sentiment_score}")
                st.write(f"**Category:** {category}")

                # Feedback section
                st.write("---")
                st.subheader("Provide Feedback")
                correct_category = st.text_input("If the category is incorrect, enter the correct category:")
                if st.button("Submit Feedback"):
                    if correct_category:
                        feedback_payload = {"text": text_input, "correct_category": correct_category}
                        feedback_response = requests.post(FEEDBACK_URL, json=feedback_payload)
                        feedback_response.raise_for_status()
                        st.success("Feedback submitted successfully!")
                    else:
                        st.error("Please enter a correct category.")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to the API: {e}")
        else:
            st.error("Please enter some text.")

    # File upload section
    st.write("---")
    st.subheader("Or upload a text file")
    uploaded_file = st.file_uploader("Choose a text file", type=["txt"])
    if uploaded_file is not None:
        try:
            # Make a POST request to the upload endpoint
            files = {"file": uploaded_file}
            response = requests.post(UPLOAD_URL, files=files)
            response.raise_for_status()

            # Parse the response
            result = response.json()
            st.subheader("Results")
            st.write(f"**Filename:** {result['filename']}")
            st.write(f"**Sentiment Score:** {result['sentiment_score']}")
            st.write(f"**Category:** {result['category']}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error uploading file: {e}")

    # Fine-tune button
    st.write("---")
    st.subheader("Fine-Tune Model")
    if st.button("Fine-Tune Model"):
        try:
            response = requests.post(FINE_TUNE_URL)
            response.raise_for_status()
            st.success("Model fine-tuned successfully!")
        except requests.exceptions.RequestException as e:
            st.error(f"Error fine-tuning model: {e}")

if __name__ == "__main__":
    main()
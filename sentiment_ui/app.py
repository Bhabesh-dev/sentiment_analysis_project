import streamlit as st
import requests

# API endpoints
API_URL = "http://127.0.0.1:8000/analyze"
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

if __name__ == "__main__":
    main()
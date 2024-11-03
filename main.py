# Import necessary libraries
import streamlit as st
from textblob import TextBlob

# Title and Description
st.title("Sentiment Analysis Interactive GUI")
st.write("Enter text below to analyze its sentiment:")


user_input = st.text_area("Enter text here:", "")

if st.button("Analyze Sentiment"):
   
    if user_input:
        blob = TextBlob(user_input)
        sentiment_score = blob.sentiment.polarity

        # Display results
        st.write("Sentiment Score:", sentiment_score)
        if sentiment_score > 0:
            st.write("Sentiment: Positive 😊")
        elif sentiment_score < 0:
            st.write("Sentiment: Negative 😞")
        else:
            st.write("Sentiment: Neutral 😐")
    else:
        st.write("Please enter text to analyze.")


if "history" not in st.session_state:
    st.session_state.history = []

if user_input:
    st.session_state.history.append((user_input, sentiment_score))

st.write("History:")
for idx, (text, score) in enumerate(st.session_state.history):
    st.write(f"{idx+1}. Text: {text} | Sentiment Score: {score}")

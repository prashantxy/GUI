import streamlit as st
from textblob import TextBlob

# Set a custom background color
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title with emoji
st.title("🌟 Sentiment Analysis Interactive GUI 🌟")
st.write("Analyze the sentiment of any text below:")

# Text input area in a column layout
col1, col2 = st.columns(2)
with col1:
    user_input = st.text_area("📝 Enter text here:", "")

with col2:
    # Button for sentiment analysis
    if st.button("Analyze Sentiment"):
        if user_input:
            blob = TextBlob(user_input)
            sentiment_score = blob.sentiment.polarity
            
            # Display sentiment score and result
            st.write("**Sentiment Score:**", round(sentiment_score, 2))
            if sentiment_score > 0:
                st.success("Sentiment: Positive 😊")
            elif sentiment_score < 0:
                st.error("Sentiment: Negative 😞")
            else:
                st.info("Sentiment: Neutral 😐")
        else:
            st.warning("⚠️ Please enter text to analyze.")

# Store history in session state
if "history" not in st.session_state:
    st.session_state.history = []

if user_input:
    st.session_state.history.append((user_input, sentiment_score))

# Display analysis history with enhanced UI
st.subheader("🕒 Analysis History")
if st.session_state.history:
    for idx, (text, score) in enumerate(st.session_state.history, start=1):
        st.markdown(
            f"""
            <div style="background-color: #e8f5e9; padding: 10px; margin-bottom: 10px; border-radius: 5px;">
                <b>#{idx}</b> - <i>{text}</i> <br> 
                <b>Score:</b> {round(score, 2)} 
                {"😊 Positive" if score > 0 else "😞 Negative" if score < 0 else "😐 Neutral"}
            </div>
            """, unsafe_allow_html=True
        )
else:
    st.write("No history available.")

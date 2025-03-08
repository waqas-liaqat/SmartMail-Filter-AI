import re
import dill as pickle
import pandas as pd
import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

# ✅ Fix: Move this to the top to prevent Streamlit error
st.set_page_config(page_title="Email Spam Filter", page_icon="📩", layout="centered")

# Download required NLTK resources
nltk.download("punkt")
nltk.download("stopwords")

# Initialize stemmer and stopwords
stemmer = SnowballStemmer("english")
stop_words = set(stopwords.words("english"))

# ✅ Define text_preprocessor manually instead of loading from pickle
def text_preprocessor(text):
    # Remove special characters
    text = re.sub(r"[^a-zA-Z0-9\s]|[^\w\s@#\$%\&\*\-]", " ", text)
    # Convert to lowercase
    text = text.lower()
    # Tokenize
    words = word_tokenize(text)
    # Remove stopwords and apply stemming
    words = [stemmer.stem(word) for word in words if word not in stop_words]
    return " ".join(words)

# ✅ Load Vectorizer and Model (No loading of preprocessor from pickle)
@st.cache_resource
def load_vectorizer():
    with open('Artifacts/vectorizer.pkl', 'rb') as f:  
        return pickle.load(f)

@st.cache_resource
def load_model():
    with open('Artifacts\Logistic Regression.pkl', 'rb') as f:  
        return pickle.load(f)

# Load components
vectorizer = load_vectorizer()
model = load_model()

# Streamlit App UI
st.markdown(
    """
    <h1 style="text-align: center; color: #FF4B4B;">📩 Email Spam Filter</h1>
    <p style="text-align: center; font-size: 18px;">Enter an email subject and content to check if it's <strong>Spam</strong> or <strong>Not Spam</strong>.</p>
    <hr>
    """,
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/281/281769.png", width=100)
st.sidebar.markdown("### 🔍 How It Works?")
st.sidebar.info(
    "- Enter **Subject** and **Content** of an email.\n"
    "- For Empty Subject write **No Subject**.\n"
    "- Click **Check Spam** to get the prediction.\n"
    "- Uses **Machine Learning** to classify emails."
)

# Input Fields
subject = st.text_input("📌 Email Subject", help="Enter the subject of the email")
content = st.text_area("📝 Email Content", help="Enter the main email body text", height=150)

# ✅ Predict Function with Probability
def predict_spam(subject, content):
    # Create DataFrame with two features
    input_data = pd.DataFrame([[subject, content]], columns=['Subject', 'Content'])
    
    # Apply text preprocessing
    input_data['Subject'] = input_data["Subject"].apply(text_preprocessor)
    input_data['Content'] = input_data["Content"].apply(text_preprocessor)
    
    # Vectorize the processed input
    input_vectorized = vectorizer.transform(input_data[['Subject','Content']])
    
    # Predict spam or not spam
    prediction = model.predict(input_vectorized)[0]
    
    return "Spam" if prediction == 1 else "Not Spam"

# Prediction Button
if st.button("Check Spam", use_container_width=True):
    if subject.strip() == "" or content.strip() == "":
        st.warning("⚠️ Please enter both Subject and Content!")
    else:
        result= predict_spam(subject, content)
        
        if result == "Spam":
            st.error(f"**Prediction: {result}**")
        else:
            st.success(f"**Prediction: {result}**")


# 📩 Email Spam Filter

## 📝 Project Overview
This project is an **AI-powered Email Spam Filter** that detects spam emails using **Natural Language Processing (NLP) and Machine Learning**. It follows an **end-to-end pipeline** from data ingestion to model training and deployment as a **Streamlit web app**.

## 🎯 Features
✅ **End-to-End Pipeline** – Data ingestion, preprocessing, model training, evaluation, and deployment  
✅ **TF-IDF Vectorization** – Converts text into numerical representations  
✅ **Machine Learning Models** – Trained on **Logistic Regression (98.90% accuracy)** and **Naïve Bayes**  
✅ **Web App UI** – Built with **Streamlit** for real-time spam classification  
✅ **Cross-Platform Compatibility** – Works on Windows, macOS, and Linux  

## 📂 Project Structure
```
SMARTMAIL FILTER AI
│── Artifacts              # Saved models, vectorizers, and datasets
│   ├── Logistic Regression.pkl  # Trained ML model
│   ├── vectorizer.pkl          # TF-IDF Vectorizer
│   ├── text_preprocessor.pkl   # Text preprocessor
│   ├── clean_data.csv          # Processed dataset
│   ├── raw_data.csv            # Raw dataset
│   ├── x_train.csv, y_train.csv, x_test.csv, y_test.csv  # Training & Testing Data
│
│── Assets                 # Additional files
│   ├── ham spam mails      # Email samples
│   ├── dataset_link.txt    # Link to dataset
│
│── Notebooks              # Jupyter Notebooks for each phase
│   ├── 01_Data_Ingestion.ipynb  # Data collection
│   ├── 02_EDA.ipynb            # Exploratory Data Analysis
│   ├── 03_Data_Preprocessing.ipynb  # Cleaning & Feature Engineering
│   ├── 04_Model_building.ipynb  # Model Training & Evaluation
│
│── app.py                 # Streamlit Web App
│── README.md              # Documentation
│── .gitignore             # Git Ignore
│── .gitattributes         # Git Attributes
|── requirements.txt       # Dependencies
```

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/waqas-liaqat/SmartMail-Filter-AI.git
cd email-spam-filter
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv  # Create virtual environment
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Running the Web App
Run the Streamlit app with:
```bash
streamlit run app.py
```
Then, open **http://localhost:8501/** in your browser.

## 🔍 How It Works
1️⃣ **Enter** the **Email Subject** and **Email Content** in the app.  
2️⃣ **Click** **Check Spam** to analyze the email.  
3️⃣ **View the Prediction** – The model classifies it as **Spam** or **Not Spam** along with a confidence score.  

## 📊 Model Details
- **Text Vectorization**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Algorithms Used**: Logistic Regression (98.90% accuracy) & Multinomial Naïve Bayes
- **Dataset**: Collected spam & ham emails (30K+ samples)
- **Hyperparameter Tuning**: GridSearchCV used for optimization

## 📦 Deployment
App is deployed on Streamlit Cloud and in future can be deployed on:

**Hugging Face Spaces**  
**AWS / GCP / Azure**   

## 🤖 Future Improvements
🔹 **Deep Learning Models** – Implement BERT, LSTMs, or Transformers for better accuracy  
🔹 **Email Attachments & Metadata** – Improve spam detection with additional features  
🔹 **Automated API Integration** – Build an API for seamless integration with email services  
🔹 **UI Enhancements** – Add a better user experience with improved design  

## 💡 Contribution
Contributions are welcome! If you’d like to improve this project, feel free to **fork the repository, create a branch, and submit a pull request**.  

## 📜 License
This project is licensed under the **MIT License** – feel free to use and modify it.  

---
### 🏆 Author: Muhammad Waqas
📧 **Contact:** waqasliaqat630@gmail.com  
🔗 **LinkedIn:** [Muhammad Waqas](https://www.linkedin.com/in/muhammad-waqas-liaqat/)  
🖥 **GitHub:** [Muhammad Waqas](https://github.com/waqas-liaqat)  


import streamlit as st
import joblib

# Load model and vectorizer
logreg = joblib.load("logistic_regression_model.pkl")
rf = joblib.load("random_forest_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

# App Title
st.title("📧 Email Spam Classifier")
st.write("Check whether an email is SPAM or HAM (not spam).")

# Email text input
email_text = st.text_area("Enter email text here:")

# Prediction button
if st.button("Predict"):
    if email_text.strip() == "":
        st.warning("Email text cannot be empty.")
    else:
        # Vectorize input
        vec = tfidf.transform([email_text])

        # Make predictions
        pred_lr = logreg.predict(vec)[0]
        pred_rf = rf.predict(vec)[0]

        label_map = {0: "HAM", 1: "SPAM"}

        # Display prediction results
        st.subheader("Prediction Results:")
        st.write(f"**Logistic Regression**: `{label_map[pred_lr]}`")
        st.write(f"**Random Forest**: `{label_map[pred_rf]}`")

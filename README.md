
# 📊 Machine Learning Project Report: Email Spam Classification - Adityo Pangestu

## 🌐 Project Domain

Email remains one of the most widely used communication channels in the digital era. However, misuse in the form of **spam**—unwanted, often fraudulent or aggressively promotional messages—poses a significant threat. According to **Statista (2024)**, over 45% of global email traffic consists of spam messages. Spam can lead to distractions, financial losses, and security risks such as phishing and malware attacks ([Statista, 2024](https://www.statista.com/statistics/420391/spam-email-traffic-share/)). Hence, an automated system is necessary to detect and filter spam efficiently.

## 🎯 Business Understanding

### ❓ Problem Statement

How can we build a machine learning model that accurately classifies email messages as spam or ham (non-spam)?

### 🎯 Project Goals

To develop a robust classification model capable of separating spam emails from ham emails with high accuracy and strong generalization performance.

### 💡 Solution Statements

1. Develop a baseline classification model using **Logistic Regression**.
2. Implement a more complex and potentially higher-performing model using **Random Forest**.
3. Create a prediction function to perform inference on new, unseen email text.
4. Compare the performance of both models to determine the optimal solution.

## 🧠 Data Understanding

([Dataset](https://kaggle.com/datasets/9a10fb9db1dd5ef7575d32e1e53fa64b62b5ab080234eb1f76c6d1e8086ae832))
The dataset used for this project includes two main columns:
- `text`: The content of the email.
- `label`: The category of the email, either `spam` or `ham`.

### Data Preparation Steps:

1. **Label Encoding**: Converted textual labels ('spam', 'ham') into numerical values (1 for spam, 0 for ham).
2. **Missing Value Check**: Ensured the dataset contained no null values.
3. **Text Length Analysis**: Added a `length` column to analyze the distribution of email lengths.
4. **WordCloud & Histogram Visualization**: Used to explore keyword frequency and message structure for each class.
5. **Downsampling**: Since the dataset was imbalanced (ham outnumbered spam), downsampling was performed on the majority class to create a balanced dataset for fair model training.

## 🤖 Modelling

### Model 1: Logistic Regression
- ✅ **Pros**: Simple, fast to train, easy to interpret.
- ❌ **Cons**: May underperform on complex or non-linear feature relationships.
- 🔧 **Key Parameters**: `solver=lbfgs`, `random_state=42` (default settings).

### Model 2: Random Forest
- ✅ **Pros**: High accuracy, robust to overfitting, handles non-linear relationships well.
- ❌ **Cons**: Slower training time, less interpretable.
- 🔧 **Key Parameters**: `n_estimators=100`, `random_state=42`.

### 🏆 Model Performance Results

| Model              | Accuracy |
|-------------------|----------|
| Random Forest      | 95%      |
| Logistic Regression| 94%      |

### ✅ Best Model: Random Forest

**Random Forest** was selected as the best-performing model. Despite slightly longer training times, it achieved the highest accuracy and demonstrated stable performance in identifying spam emails effectively.

## 📏 Evaluation

### 📐 Evaluation Metrics Used

1. **Accuracy**  
\[
Accuracy = \frac{TP + TN}{TP + TN + FP + FN}
\]  
Measures the overall correctness of the model.

2. **Confusion Matrix**  
Provides a breakdown of correct and incorrect predictions per class (Spam = 1, Ham = 0).

3. **Classification Report**  
Includes:
   - **Precision**: Proportion of positive identifications that were actually correct.
   - **Recall**: Proportion of actual positives that were correctly identified.
   - **F1-Score**: Harmonic mean of precision and recall.

These metrics ensure that the model not only achieves high accuracy but is also reliable in detecting spam with minimal false positives.

---

## Web Interactive

[Streamlit](https://spam-email-using-rf-and-logreg.streamlit.app/)

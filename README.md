Spam Mail Prediction System

Overview

This project is a machine learning-based spam mail prediction system. It uses natural language processing (NLP) techniques to classify email messages as either "spam" or "ham" (non-spam). The model is trained using logistic regression and utilizes TF-IDF (Term Frequency-Inverse Document Frequency) vectorization to convert text data into numerical features.


Features

Load and preprocess email dataset
Convert text data into feature vectors using TF-IDF
Train a Logistic Regression model to classify emails
Evaluate the model's accuracy on training and test data
Predict whether a given email is spam or ham


#Technologies Used

Python
Pandas
NumPy
Scikit-learn (sklearn)


#Dataset

The dataset used for training and testing the model is stored in a CSV file (Kaggle). It contains two columns:
Category: Specifies whether the email is spam or ham.
Message: The content of the email.


#Installation

Clone this repository:
git clone https://github.com/yourusername/spam-mail-prediction.git
cd spam-mail-prediction
Install the required dependencies:
pip install numpy pandas scikit-learn
Ensure the dataset (mail_data.csv) is placed in the correct directory.


#Usage

Run the script to train the model and make predictions:
python spam_mail_prediction.py
To test the model with a custom email message, modify the input_mail variable in the script:
input_mail = ["Your custom message here"]
The model will output whether the message is classified as "Spam" or "Ham."


#Model Performance

Training Accuracy: 96.76%
Test Accuracy: 96.68%


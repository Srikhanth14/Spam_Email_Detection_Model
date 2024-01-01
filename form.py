# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:27:28 2024

@author: ELCOT
"""

import streamlit as st
import pickle
from PIL import Image


def spam_form():

    # Load the TF-IDF vectorizer
    tfidf_vectorizer=pickle.load(open('tfidfvectorizer.sav','rb'))
    # Load the trained model
    loaded_model = pickle.load(open('spam_email_trained_model.sav', 'rb'))
    
    def spam_email_prediction(message):
        # Convert text to feature vectors using the same TF-IDF vectorizer
        input_mail = [message]
        input_data_features = tfidf_vectorizer.transform(input_mail)
    
        # Making a prediction
        prediction = loaded_model.predict(input_data_features)
    
        # Display the prediction result
        if prediction[0] == 1:
            st.write("Predicted Label: Spam mail")
            st.image(Image.open('Spam.jpg'), use_column_width=True)
            
        else:
            st.write("Predicted Label: Ham mail")
            st.image(Image.open('Good.jpg'), use_column_width=True)
            
    
    def main():
        st.title('Spam Email Prediction Web App')
        st.write("Enter the Email Details: ")
    
        # Input component for the message
        message = st.text_area("Message", "Type your email message here.")
    
        if st.button('Spam Prediction Result'):
            # Pass the input value to the spam_email_prediction function
            spam_email_prediction(message)
    
    main()

# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:27:27 2024

@author: ELCOT
"""

import streamlit as st
import pandas as pd

def spam_data():
    # Dataset Information
    st.header("Dataset Information:")
    st.write("The predictive model is trained on a dataset containing various email messages labeled as spam or legitimate. The dataset is carefully curated to ensure accurate predictions.")

    # Sample Data
    st.header("Sample Data:")
    st.write("Here's a glimpse of the dataset:")
    data = pd.read_csv("Spam_Email_Detection.csv") # Replace with your actual dataset file
    data = data.drop(columns=['Unnamed: 2','Unnamed: 3','Unnamed: 4'],axis=1,inplace=True)
    st.dataframe(data.head())

    # Download Dataset
    st.subheader("Download Dataset")
    st.write("You can download the full Spam Email dataset for further exploration:")

    def data_read(data):
        return data.to_csv().encode('utf-8')

    csv = data_read(data)
    
    st.download_button(
                            label='Download Sample Data',
                            data=csv,
                            file_name='spam_email_dataset.csv',
                            mime='text/csv'
                      )

    # Input Your Data
    st.header("Input Your Data:")
    st.write("Want predictions for your specific email messages? Enter your email text in the input form and discover the spam classification.")

    # Guidance on Data Format
    st.header("Guidance on Data Format:")
    st.write("To ensure successful predictions, enter your email text in the same format as the sample data. The model analyzes the content of the email to make predictions.")

    # GitHub Link
    st.header("GitHub Repository:")
    st.write("Explore the code and details of this project on my GitHub repository:")
    st.write("[Spam Email Prediction GitHub Repository](link-to-your-github-repository)")

    # Conclusion
    st.write("Ready to get predictions for your emails? Input your email text in the input form, and let the Spam Email Prediction app work its magic!")


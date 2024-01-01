# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:27:24 2024

@author: ELCOT
"""

import streamlit as st
from PIL import Image

def spam_home():
    
    st.image(Image.open('home_img.jpg'),use_column_width=True)
    # Introduction
    st.subheader("Welcome to the Spam Email Prediction App!")
    st.write("Uncover the secrets of spam detection with advanced machine learning. This web app showcases the power of predictive analytics, providing accurate predictions to identify whether an email is spam or not.")

    # Key Features
    st.subheader("Key Features:")
    
    st.write("1.**Spam Detection:**")
    st.write("   Explore the capabilities of our spam detection model. It analyzes the content of emails to accurately predict whether they are spam or legitimate.")

    st.write("2.**User-Friendly Interface:**")
    st.write("   Navigate effortlessly through our user-friendly interface. No expertise required – simply input your email message and witness the magic.")

    st.write("3.**Predictive Insights:**")
    st.write("   Visualize the model's predictions and gain insights into the factors contributing to the classification of emails.")

    # About Me
    st.subheader("About Me:")
    st.write("Curious about the mind behind the model? I'm SRIKHANTH R, a passionate data analyst dedicated to the world of machine learning and spam detection.")
    st.write("Feel free to reach out for any questions, collaborations, or discussions about data science and analyst.")
    st.write("Explore more of my projects on [GitHub](https://github.com/Srikhanth14) and connect with me on [LinkedIn](linkedin.com/in/srikhanth-r).")

    # Call to Action
    st.write("Ready to test the spam detection model? Head over to the **Input Form** page to enter your email message and see the prediction results in action!")

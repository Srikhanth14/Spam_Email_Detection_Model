# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:27:28 2024
@author: ELCOT
"""

import streamlit as st
from PIL import Image

def spam_email_visualization():
    # Page Title
    st.title("Visualization")

    # Introduction
    st.write("Explore a visualization highlighting patterns and insights from the Spam Email dataset.")

    # Image 1: Count Plot - Distribution of Spam and Ham Emails
    st.header("Count Plot - Distribution of Spam and Ham Emails")
    image1 = Image.open("Distribution.png")  # Replace with your image file
    st.image(image1, caption="Count Plot - Spam and Ham Emails", use_column_width=True)

    # Visualization Explanation
    st.subheader("Understanding the Visualization:")
    st.write("The count plot illustrates the distribution of spam and ham emails in the dataset. Each bar represents the count of spam or ham emails.")

    # Interpretation
    st.subheader("Interpretation:")
    st.write("Observing the count plot allows us to understand the balance between spam and ham emails. This insight is crucial for evaluating the model's performance.")

    # Call to Action
    st.write("Ready to dive deeper into the dataset? Head to the **Dataset** and **Input Form** pages for a more comprehensive analysis of Spam Email data.")

# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:26:00 2024

@author: ELCOT
"""

import streamlit as st
from streamlit_option_menu import option_menu
import home,Dataset,Visualization,form

st.set_page_config(page_title="Spam Email Prediction", page_icon="✉️", layout="wide")

selected = option_menu(
    menu_title="Spam Email Prediction",
    options=["Home", "Dataset", "Insights", "Input Form"],
    icons=["house-fill", "book", "bar-chart-fill", "card-list"],
    menu_icon="menu-up",
    default_index=0,
    orientation="horizontal"
)

if selected == "Home":
    home.spam_home()
elif selected == "Dataset":
    Dataset.spam_data()
elif selected == "Insights":
    Visualization.spam_email_visualization()
elif selected == "Input Form":
    form.spam_form()
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import nltk
import pickle as pk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
import warnings
warnings.simplefilter(action='ignore',category=FutureWarning)
from keras.models import load_model

import streamlit as st

st.markdown(
    """
    <style>
    .header-style{
        font-size:25px;
        font-family:sans-serif;
        position:absolute;
        text-align:center;
        color:@032131;
        top:0px;
    }
    .font-style{
        font-size:20px;
        font-family:sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def

if "page" not in st.session_state:
    st.session_state.page = "home"
    
if st.session_state.page == "home":
    st.title("WELCOME TO STUDENT MENTAL HEALTH PREDICTION")
    st.image("depress.jpg",width=700)
    st.write("""
             This ia a Web Application that helps in detecting whether a Student is in depression based on the 
             user sentence they will enter.
             """)
    if st.button("Go To Analysis"):
        st.session_state.page = "analyze"
        
if st.session_state.page == "analyze":
    st.header("Depression Detection")
    st.text("Input a Sentence for analysis:")
    
    user_sentence = st.text_input("Enter a Sentence...")
    if user_sentence:
        clean_sentence = clean_input(user_sentence)
        if st.button("Analyze"):
            detect_depression(clean_sentence)
            
    if st.button("Go Back To Home"):
        st.session_state.page = "home"
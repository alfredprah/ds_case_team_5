import streamlit as st
import numpy as np
import pandas as pd

# Pages
import dashboard
import tweet_review


st.title('Main Page')

PAGES = {
    "Dashboard": dashboard,
    "Review Tweets": tweet_review
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]

page.app()
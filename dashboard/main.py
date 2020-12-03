import streamlit as st
import numpy as np
import pandas as pd


st.set_page_config(
	page_title = 'Twitter | Content Moderation',
	page_icon = 'assets/favicon_twitter.ico',
	initial_sidebar_state = 'expanded'

)

# Pages
import dashboard
import tweet_review

st.title('Twitter Content Moderation')

PAGES = {
	"Review Tweets": tweet_review,
  "Dashboard": dashboard    
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]

page.app()
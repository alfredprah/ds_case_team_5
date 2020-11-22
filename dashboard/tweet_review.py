import streamlit as st
import numpy as np
import pandas as pd
import base64
import random

import datetime as dt

import io
from typing import List, Optional

from random_username.generate import generate_username
from streamlit.hashing import _CodeHasher



file_ = open("assets/twitter_photo.jpg", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()


def html_body(**kwargs):
	## CSS for Tweet Review
	inline_css = """
	<style>
		.tweet-container {
			min-width: 250px;
			max-width: 550px;
			min-height: 150px;
			overflow: hidden;
			border-width: 1px;
			border-radius: 15px;
			border-color: rgb(204, 214, 221);
			border: 1px solid black;
			box-sizing: border-box;
			margin-bottom: 10px;
		}

		.tweet-interior {
			padding: 10px 15px 5px;
			background-color: rgb(255, 255, 255);
			padding-right: 15px;
			padding-left: 15px;
			padding-bottom: 5px;
			box-sizing: border-box;
			border: 0px solid black;
			position: relative;
		}

		.tweet-header {
			padding-bottom: 10px;
			align-items: stretch;
			margin: 0px;
			display: flex;
			# box-sizing: border-box;
		}

		#logo {
			width: 46px;
			height: 46px;
			border-radius: 9999px;
			overflow: hidden;
		}

		.tweeter {
			max-width: calc(100% - 84px);
			justify-content: center;
			margin-left: 5px;
			margin-right: 5px;
		} 

	</style>
	"""

	html = f"""
	<div style="margin-bottom:15px;">
		<div class="tweet-container">
			<div class="tweet-interior">
				<div class="tweet-header">
					<div id="logo">
						<img style="height:100%; width:100%;" src="data:image;base64,{kwargs['data_url']}" alt="twitter logo">
					</div>
					<div class="tweeter">
						<span style="line-height: 1.3125; overflow-wrap: break-word; font-size: 15px; font-weight: bold;">
							Twitter Content Moderation
						</span>
						<div style="font-weight:400; font-size: 14px;">
							@{kwargs['user'][0]}
						</div>
					</div>
				</div>
				{kwargs['tweet_body']}
			</div>
		</div>
	</div>
	"""
	return inline_css + html


# Load CSV of Predictions
def load_predictions():
	return pd.read_csv('../data/case2/dashboard_predictions.csv', index_col='id')

def get_tweet(df):
	"""
	Randomly pick one tweet that needs to be reviewed
	"""
	df_tweets = df.loc[df['flag'] == 1 & df['reviewed_target'].isna()]
	# tweet_id = '2018'
	tweet_id = random.sample([*df_tweets.index], k = 1)[0]

	return df_tweets.iloc[df_tweets.index == tweet_id]

def update_predictions(df, tweet_info, label):
	df_tweets = df.copy()
	df_tweets.loc[df_tweets.index.isin(tweet_info.index), ['reviewed_target', 'datetime_review']] = \
		[label, dt.datetime.now()]

	df_tweets.to_csv('../data/case2/dashboard_predictions.csv')

	return load_predictions()


# app1
def app():
	# Create random username
	user = generate_username(1)

	# st.title('APP1')
	st.write('Is the following Tweet related to a real diaster?')
	st.write('')
	
	# Get tweet info
	df_tweets = load_predictions()
	tweet_info = get_tweet(df_tweets)
	tweet_body = tweet_info['text'].values[0].replace("\n", "<br>")

	counter = df_tweets.loc[df_tweets['flag'] == 1 & df_tweets['reviewed_target'].isna()].shape[0]

	test_html = html_body(user = generate_username(1),
												tweet_body = tweet_body,
												tweet_prob = tweet_info['probability'],
												counter = counter,
												data_url = data_url
	)

	# Tweet Container + Styling
	st.markdown(test_html, unsafe_allow_html=True) #Title rendering

	c1, c2 = st.beta_columns(2)

	if c1.button(label="No, not a disaster", key="btn-not-disaster"):
		update_predictions(df_tweets, tweet_info, label = 0)
	
	if c2.button(label="Yes, its a disaster", key = 'btn-disaster'):
		update_predictions(df_tweets, tweet_info, label = 1)

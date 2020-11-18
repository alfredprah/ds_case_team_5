import streamlit as st
import numpy as np
import pandas as pd

# app1
def app():
	st.title('APP1')
	st.write('Welcome to app1')

	# Similar to an accordian
	my_expander = st.beta_expander('test')
	my_expander.write('Hello there!')
	clicked = my_expander.button('Click me!')

	my_expander2 = st.beta_expander('test2')
	with my_expander2:
		'Hello there!'
		clicked2 = st.button('Click me!', key='clicked')
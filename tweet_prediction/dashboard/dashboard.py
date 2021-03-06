import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# app2.py
def app():
    st.title('APP2')
    st.write('Dashboard for Review')
  
def load_predictions():
	return pd.read_csv('../data/dashboard_predictions.csv', index_col='id')
st.set_option('deprecation.showPyplotGlobalUse', False)

def app():
    data = load_predictions()

    #histogram
    df = pd.DataFrame(data, columns = ['flag'])
    df.hist()
    plt.xticks(range(len((0,1))),["Automated","Needs Review"])
    plt.show()
    st.pyplot()
    
    df=data[data['flag']==1]
    df["reviewed_target"].fillna(2, inplace=True)
    df["reviewed_target"].hist()
    plt.xticks(range(3),["Positive","Negative","Needs Review"])
    plt.show()
    st.pyplot()

    
    
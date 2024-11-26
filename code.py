import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st
from io import BytesIO
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv('sleep.csv')

st.title('Sleep Data')

tab1, tab2 = st.tabs(['Age','Gender'])
with tab1:
    input_age = st.slider('Age', min_value=27, max_value=59, value=40)
    df1 = df[df['Age'] == input_age].copy()
    fig1 = px.line(df1, x='Age', y='MMRCurrentRetailCleanPriceSleep Duration')
    st.plotly_chart(fig1)

with tab2:
    st.text('Hello')
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st
from io import BytesIO
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv('auctioncars.csv')

st.title('Auctioned Cars Data')

tab1, tab2, tab3 = st.tabs(['Make','Model','Color'])
with tab1:
    input_make = st.text_input('Enter a make (ALL CAPS):', value='CHEVROLET')
    input_model = st.text_input('Enter a model (ALL CAPS):', value='IMPALA')
    df1 = df[df['Make'] == input_make & df['Model'] == input_model].copy()
    fig1 = px.line(df1, x='VehYear', y='MMRCurrentRetailCleanPrice')
    st.plotly_chart(fig1)

with tab2:
    input_model = st.text_input('Enter a model:', value='IMPALA')

with tab3:
    input_color = st.text_input('Enter a color(ALL CAPS):', value='RED')
    df3 = df[df['Color'] == input_color].copy()
    fig3 = px.line(df1, x='VehYear', y='MMRCurrentRetailCleanPrice')
    st.plotly_chart(fig3)
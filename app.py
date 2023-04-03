import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv("India.csv")

list_of_states = list(df['State'].unique())
list_of_states.insert(0,"Overall India")



st.sidebar.title("India Ka Data")
select_State  = st.sidebar.selectbox("Select State",list_of_states)
primary = st.sidebar.selectbox("Select Primary Value",sorted(list(df.columns[5:])))
secondary = st.sidebar.selectbox("Select Secondary Value",sorted(list(df.columns[5:])))

plot = st.sidebar.button("Plot Graph")
if plot:

    st.header("Size Represents Primary Value")
    st.header("Color Represents Secondary Value")
    if select_State == "Overall India":
        #plot for india
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", mapbox_style="carto-positron",size=primary,
                                color=secondary,size_max=30, zoom=3.5,height=700,width=1200,hover_name='District',color_continuous_scale='agsunset')
        st.plotly_chart(fig,use_container_width=True)
    else:
        #plot for state
        state_df = df[df['State'] == select_State]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", mapbox_style="carto-positron", size=primary,
                                color=secondary, size_max=30, zoom=6, height=700, width=1200, hover_name='District',color_continuous_scale='agsunset')

        st.plotly_chart(fig, use_container_width=True)


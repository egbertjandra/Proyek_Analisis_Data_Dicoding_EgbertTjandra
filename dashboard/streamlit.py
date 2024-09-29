# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:24:46 2024

@author: LENOVO
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Import data
bike_hour = pd.read_csv("dashboard/bike_hour.csv")

#Judul dashboard
st.title("Bike Sharing Data Analysis")
#Sidebar
st.sidebar.title("Bike Sharing Dashboard")
st.sidebar.text("Use this dashboard to explore bike sharing data.")
year = st.sidebar.slider("Select Year:", min_value=2011, max_value=2012, value=2011)

#Menunjukan data
with st.container():
    st.write("### Bike Sharing Data Preview:")
    st.write(bike_hour.head())

#Membuat visualisasi dalam bentuk kolom
col1, col2 = st.columns(2)

with col1:
    st.write("### Total Rentals by Season:")
    plt.figure(figsize=(10, 5))
    sns.countplot(data=bike_hour, x='season', palette='viridis')
    plt.title("Total Rentals by Season")
    plt.xlabel("Season")
    plt.ylabel("Total Rentals")
    st.pyplot(plt)  
    
with col2:
    st.write("### Total Rentals by Weather:")
    plt.figure(figsize=(10, 5))
    sns.countplot(data=bike_hour, x='weathersit', palette='magma')
    plt.title("Total Rentals by Weather Condition")
    plt.xlabel("Weather Condition")
    plt.ylabel("Total Rentals")
    st.pyplot(plt)

#Memfilter data
filter_data = bike_hour[(bike_hour['yr'] == (year - 2011))]

#Membuat Tab
tab1, tab2 = st.tabs(["Monthly Rentals", "Yearly Overview"])

with tab1:
    st.write(f"### Monthly Rentals for Year {year}:")
    filtered_data = bike_hour[bike_hour['yr'] == (year - 2011)]
    plt.figure(figsize=(10, 5))
    sns.countplot(data=filtered_data, x='mnth', palette='coolwarm')
    plt.title(f"Total Rentals by Month in {year}")
    plt.xlabel("Month")
    plt.ylabel("Total Rentals")
    st.pyplot(plt)

with tab2:
    st.write("### Yearly Overview:")
    plt.figure(figsize=(10, 5))
    sns.countplot(data=bike_hour, x='yr', palette='Set1')
    plt.title("Total Rentals by Year")
    plt.xlabel("Year")
    plt.ylabel("Total Rentals")
    st.pyplot(plt)

#Expander
with st.expander("Tentang Data dan Insight Visualisasi"):
    st.write(
        """Dataset ini berisi informasi tentang penyewaan sepeda, 
        yang dikategorikan berdasarkan berbagai fitur seperti 
        musim, kondisi cuaca, dan waktu dalam setahun. Dari visualisasi yang 
        tersedia, kita dapat melihat bahwa penyewaan sepeda sangat dipengaruhi 
        oleh cuaca dan musim. Misalnya, penyewaan cenderung lebih tinggi 
        selama musim panas dan pada saat cuacanya baik. 
        Insight ini dapat membantu dalam perencanaan pengelolaan sepeda 
        sewa."""
    )

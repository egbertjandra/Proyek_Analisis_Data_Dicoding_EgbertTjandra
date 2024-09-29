# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:24:46 2024

@author: LENOVO
"""

import os 
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

current_directory = os.path.dirname(__file__)
csv_file_path = os.path.join(current_directory, 'bike_hour.csv')

# Import data
bike_hour = pd.read_csv(csv_file_path)

# Judul dashboard
st.title("Bike Sharing Data Analysis")

# Sidebar
st.sidebar.title("Bike Sharing Dashboard")
st.sidebar.text("Use this dashboard to explore bike sharing data.")
year = st.sidebar.slider("Select Year:", min_value=2011, max_value=2012, value=2011)

# Menunjukan data
with st.container():
    st.write("### Bike Sharing Data Preview:")
    st.write(bike_hour.head())

# Membuat visualisasi dalam bentuk kolom
col1, col2 = st.columns(2)

with col1:
    st.write("### Average Bike Rentals by Season:")
    plt.figure(figsize=(10, 5))
    average_season = bike_hour.groupby('season')['cnt'].mean().reset_index()
    sns.barplot(data=average_season, x='season', y='cnt', palette='viridis')  # Perbaiki 'count' menjadi 'cnt'
    plt.title("Average Bike Rentals by Season")
    plt.xlabel("Season")
    plt.ylabel("Average Rentals")
    st.pyplot(plt)  
    
with col2:
    st.write("### Average Bike Rentals by Season and Year:")
    average_season_year = bike_hour.groupby(['season', 'yr'])['cnt'].mean().unstack().fillna(0)
    plt.figure(figsize=(10, 5))
    average_season_year.plot(kind='bar', stacked=True, ax=plt.gca(), colormap='orange')
    plt.title("Average Bike Rentals by Season and Year (Stacked)")
    plt.xlabel("Season")
    plt.ylabel("Average Rentals")
    plt.legend(title='Year', labels=['2011', '2012'])
    st.pyplot(plt)

# Memfilter data
filter_data = bike_hour[(bike_hour['yr'] == (year - 2011))]

# Membuat Tab
tab1, tab2 = st.tabs(["Monthly Rentals", "Yearly Overview"])

with tab1:
    st.write(f"### Average Rentals for Year {year}:")
    filtered_data = bike_hour[bike_hour['yr'] == (year - 2011)]
    plt.figure(figsize=(10, 5))
    average_monthly = filtered_data.groupby('mnth')['cnt'].mean().reset_index()
    sns.barplot(data=average_monthly, x='mnth', y='cnt', palette='coolwarm')  # Menggunakan rata-rata
    plt.title(f"Average Rentals by Month in {year}")
    plt.xlabel("Month")
    plt.ylabel("Average Rentals")
    st.pyplot(plt)

with tab2:
    st.write("### Average Rentals by Year:")
    plt.figure(figsize=(10, 5))
    average_yearly = bike_hour.groupby('yr')['cnt'].mean().reset_index()
    sns.barplot(data=average_yearly, x='yr', y='cnt', palette='Set1')  # Menggunakan rata-rata
    plt.title("Average Rentals by Year")
    plt.xlabel("Year")
    plt.ylabel("Average Rentals")
    st.pyplot(plt)

# Expander
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


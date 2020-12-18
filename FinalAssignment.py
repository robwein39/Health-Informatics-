# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#I was getting "runfile" followed by path name for every output I did
#in the console, this code below found on stackoverflow gets rid of that. 
cls = lambda: print("\033[2J\033[;H", end='')
cls()

import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import time



@st.cache
def load_hospitals():
    df_hospital_2 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_hospital_2.csv')
    return df_hospital_2

@st.cache
def load_inatpatient():
    df_inpatient_2 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_inpatient_2.csv')
    return df_inpatient_2

@st.cache
def load_outpatient():
    df_outpatient_2 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_outpatient_2.csv')
    return df_outpatient_2

st.title('Final Assignment, Informatics')
st.subheader('By Rob Weinstein')

# FAKE LOADER BAR TO STIMULATE LOADING    
my_bar = st.progress(0)
for percent_complete in range(100):
     time.sleep(0.01)
     my_bar.progress(percent_complete + 1)

import streamlit.components.v1 as stc

# uploading an image of my dog to the web app
from PIL import Image 


@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img 

#creating a home page and a Data page//code complements of a github user
def main():
	st.title(" 'Hello, World! This is my dog, Dakota")

	menu = ["Home"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
		image_file = st.file_uploader("Upload Image",type=['png','jpeg','jpg'])
		if image_file is not None:
		
			# To See Details
			# st.write(type(image_file))
			# st.write(dir(image_file))
			

			img = load_image(image_file)
			st.image(img,width=250,height=250)

if __name__ == '__main__':
	main()
    
    
   
# Load the data from the medicare dataset: 
df_hospital_2 = load_hospitals()
df_inpatient_2 = load_inatpatient()
df_outpatient_2 = load_outpatient()
hospitals_ny = df_hospital_2[df_hospital_2['state'] == 'NY']

#mapping hospitals 
st.title('A map of hospitals in NY:')
hospitals_ny_gps = hospitals_ny['location'].str.strip('()').str.split(' ', expand=True).rename(columns={0: 'Point', 1:'lon', 2:'lat'}) 	
hospitals_ny_gps['lon'] = hospitals_ny_gps['lon'].str.strip('(')
hospitals_ny_gps = hospitals_ny_gps.dropna()
hospitals_ny_gps['lon'] = pd.to_numeric(hospitals_ny_gps['lon'])
hospitals_ny_gps['lat'] = pd.to_numeric(hospitals_ny_gps['lat'])
st.map(hospitals_ny_gps)




#Hospital Ownership in NY Comparison
st.subheader('Hospital Ownership - NY')
bar1 = hospitals_ny['hospital_ownership'].value_counts().reset_index()
st.dataframe(bar1)

fig = px.pie(bar1, values='hospital_ownership', names='index')
st.plotly_chart(fig)
st.markdown('Majority of Hospitals in NY are Private and Non-profit')







#Hospital Overall Rating in NY Comparison
st.subheader('Overall Rating Comparison in NY')
bar3= hospitals_ny['hospital_overall_rating'].value_counts().reset_index()
st.dataframe(bar3) 
st.markdown('') 

fig = px.pie(bar3, values='hospital_overall_rating', names='index')
st.plotly_chart(fig)
st.markdown('Majority of ratings are N/A, but very few are in the 4/5 category')



# Stony Brook overview of features
st.subheader('Overview of Stony Brook Hospital')    
sb = hospitals_ny[hospitals_ny.city == "STONY BROOK"].T.reset_index()
sb.columns = ["Key", "Value"]
st.write(sb)
st.markdown('You can see they are below the national average in Patient Experience and Timeliness of Care')










            











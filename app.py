import streamlit as st
import plotly.express as px
import pandas as pd

vehicles = pd.read_csv('vehicles_us.csv')

st.header('Basic EDA on Vehicles Dataset')

cyl_8 = ['truck', 'pickup', 'coupe']
cyl_6 = ['SUV', 'mini-van']
cyl_4 = ['sedan', 'wagon', 'hatchback']

#Cleaning up missing values
vehicles['model_year'] = vehicles['model_year'].fillna(0).astype('int')
vehicles.loc[vehicles['type'].isin(cyl_4), 'cylinders'] = vehicles.loc[vehicles['type'].isin(cyl_4), 'cylinders'].fillna(4)
vehicles.loc[vehicles['type'].isin(cyl_6), 'cylinders'] = vehicles.loc[vehicles['type'].isin(cyl_6), 'cylinders'].fillna(6)
vehicles.loc[vehicles['type'].isin(cyl_8), 'cylinders'] = vehicles.loc[vehicles['type'].isin(cyl_8), 'cylinders'].fillna(8)
vehicles['cylinders'] = vehicles['cylinders'].fillna(6)
vehicles['odometer'] = vehicles['odometer'].fillna(0).astype('int')
vehicles['paint_color'] = vehicles['paint_color'].fillna('no_color')
vehicles['is_4wd'] = vehicles['is_4wd'].fillna(0).astype('int')


#Checkbox for toggling 4 wheel drive
is_4wd = st.checkbox(label='Is_4wd')


#Filtering out outliers
vehicles = vehicles.query('price <= 100000')
vehicles = vehicles.query('odometer <= 350000 and odometer > 0')


# Creating the charts with toggle
if is_4wd:
    price_fig = px.histogram(vehicles.query('is_4wd == 1'), x='price', title='Distribution of Prices of Cars', nbins=50)
    st.plotly_chart(price_fig)

    odo_corr = px.scatter(vehicles.query('is_4wd == 1'), x='odometer', y='price', title='Correlation of Odometer vs. Price')
    st.plotly_chart(odo_corr)
else:
    price_fig = px.histogram(vehicles.query('is_4wd == 0'), x='price', title='Distribution of Prices of Cars', nbins=50)
    st.plotly_chart(price_fig)

    odo_corr = px.scatter(vehicles.query('is_4wd == 0'), x='odometer', y='price', title='Correlation of Odometer vs. Price')
    st.plotly_chart(odo_corr)

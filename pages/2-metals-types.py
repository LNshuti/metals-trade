import pandas as pd
import streamlit as st
from streamlit_vizzu import Config, Data, Style, VizzuChart

# Load the dataset
df = pd.read_csv("data/Africa_export_Metals_2021_.csv")

# Rename Name to Country
df.rename(columns={'Name': 'Country'}, inplace=True)

# List of African countries as of my last training data in April 2023
african_countries_list = [
    'Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde',
    'Cameroon', 'Central African Republic', 'Chad', 'Comoros', 'Congo', 'Djibouti', 'Egypt',
    'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana',
    'Guinea', 'Guinea-Bissau', 'Ivory Coast', 'Kenya', 'Lesotho', 'Liberia', 'Libya',
    'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique',
    'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Sao Tome and Principe', 'Senegal', 'Seychelles',
    'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo',
    'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe'
]

# # Add a column to the dataframe to indicate if the country is African.
df['IsAfrican'] = [country_name in african_countries_list for country_name in df['Country']]

# Create a Color column defined as follows: 
african_color = "#1c9761FF" # Green for African countries
non_african_color = "#875792FF" # Purple for non-African countries

# Add a column to the dataframe to indicate the color based on whether the country is African or not
df['Color'] = df['IsAfrican'].map({True: african_color, False: non_african_color})

# Keep the top 20 by export
df = df.nlargest(20, 'Gross Export')
print(df.head(20))

data = Data()
data.add_df(df)

chart = VizzuChart(key="vizzu", height=800)
chart.animate(data)
chart.feature("tooltip", True)

# Define contrasting colors for African and non-African countries

# Configure the chart to display Gross Export by country with different colors
chart.animate(
    Config(
        {
            "x": "Gross Export",
            "y": "Country",
            #"color": "Color",
            "title": "Africa's Metal Exports in 2021",
            "sort": "byValue",
        }
    ),
    Style(
        {
            "plot": {
                "xAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                "marker": {
                    "label": {
                        "numberFormat": "prefixed",
                        "maxFractionDigits": "1",
                        "numberScale": "shortScaleSymbolUS",
                    },
                },
                "paddingLeft": "12em",
            },
         
        }
    ),
    delay="0", x={"easing": "linear"},
)

chart.show()
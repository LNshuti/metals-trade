import pandas as pd
import streamlit as st
from streamlit_vizzu import Config, Data, Style, VizzuChart

# Load the dataset
df = pd.read_csv("data/Where did Africa export Metals to in 2021_.csv")

# Keep the top 20 by export
df = df.nlargest(20, 'Gross Export')

data = Data()
data.add_df(df)

chart = VizzuChart(key="vizzu", height=600)
chart.animate(data)
chart.feature("tooltip", True)

# Since the dataset does not contain a time series, we'll not use a slider for year selection
# Instead, we can focus on visualizing the Gross Export and Share data

# Configure the chart to display Gross Export by country
chart.animate(
    Config(
        {
            "x": "Gross Export",
            "y": "Name",
            "title": "Africa's Metal Exports in 2021",
            "sort": "byValue",
        }
    ),
    Style(
        {
            "plot": {
                "xAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                "marker": {
                    "colorPalette": (
                        "#b74c20FF #c47f58FF #1c9761FF #ea4549FF #875792FF #3562b6FF "
                        "#ee7c34FF #efae3aFF"
                    ),
                    "label": {
                        "numberFormat": "prefixed",
                        "maxFractionDigits": "1",
                        "numberScale": "shortScaleSymbolUS",
                    },
                },
                "paddingLeft": "8em",
            }
        }
    ),
    delay="0", x={"easing": "linear"},
)

chart.show()
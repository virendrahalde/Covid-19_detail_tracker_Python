import pandas as pd
import plotly.express as px import plotly.io as pio
pio.templates.default = "plotly_dark"
covid_data= pd.read_csv('covid_19_data.csv')
grouped = covid_data.groupby('Last Update')[['Last Update', 'Confirmed', 'Deaths']].sum().reset_index()
fig = px.line(grouped, x="Last Update", y="Confirmed",
title="Worldwide Confirmed Novel Coronavirus(COVID-19) Cases Over Time") fig.show()
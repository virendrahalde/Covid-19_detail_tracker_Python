import pandas as pd
import plotly.express as px
covid_data= pd.read_csv('covid_19_data.csv')
covid_data['Active'] = covid_data['Confirmed'] - covid_data['Deaths'] - covid_data['Recovered'] combine_us_data = covid_data[covid_data['Country/Region']=='US'].drop(['Country/Region'], axis=1) combine_us_data = combine_us_data[combine_us_data.sum(axis = 1) > 0]
combine_us_data = combine_us_data.groupby(['Province/State'])[['Confirmed', 'Deaths', 'Recovered', 'Active']].sum().reset_index()
combine_us_data = pd.melt(combine_us_data, id_vars='Province/State', value_vars=['Confirmed', 'Deaths', 'Recovered', 'Active'], value_name='Count', var_name='Case')
fig = px.bar(combine_us_data, x='Province/State', y='Count', text='Count', barmode='group', color='Case', title='USA State wise combine number of confirmed, deaths, recovered, active COVID-19 cases')
fig.show()
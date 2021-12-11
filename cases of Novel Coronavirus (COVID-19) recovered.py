import pandas as pd
covid_data= pd.read_csv('covid_19_data.csv')
data = covid_data.groupby('Country/Region')[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index() result = data[data['Recovered']==0][['Country/Region', 'Confirmed', 'Deaths', 'Recovered']]
 print(result)
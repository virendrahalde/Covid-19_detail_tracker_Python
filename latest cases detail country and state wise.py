import pandas as pd
covid_data= pd.read_csv('covid_19_data.csv')
data = covid_data.groupby(['Country/Region', 'Province/State'])[['Confirmed', 'Deaths', 'Recovered']].max()
pd.set_option('display.max_rows', None)
print(data)

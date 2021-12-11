import pandas as pd
covid_data= pd.read_csv('covid_19_data.csv', usecols = ['Last Update', 'Country/Region', 'Confirmed', 'Deaths', 'Recovered'])
result = covid_data.groupby('Country/Region').max().sort_values(by='Confirmed', ascending=False)[:10]
pd.set_option('display.max_column', None)
print(result)
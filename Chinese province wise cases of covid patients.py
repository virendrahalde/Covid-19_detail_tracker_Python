import pandas as pd
covid_data= pd.read_csv('covid_19_data.csv')
c_data = covid_data[covid_data['Country/Region']=='Mainland China'] c_data = c_data[['Province/State', 'Confirmed', 'Deaths', 'Recovered']] result = c_data.sort_values(by='Confirmed', ascending=False)
result = result.reset_index(drop=True) 
print(result)

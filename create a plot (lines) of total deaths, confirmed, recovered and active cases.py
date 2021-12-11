import pandas as pd
import matplotlib.pyplot as plt
covid_data= pd.read_csv('covid_19_data.csv', usecols = ['Last Update', 'Country/Region', 'Confirmed', 'Deaths', 'Recovered'])
covid_data['Active'] = covid_data['Confirmed'] - covid_data['Deaths'] - covid_data['Recovered']
r_data = covid_data.groupby(["Country/Region"])[["Deaths", "Confirmed", "Recovered", "Active"]].sum().reset_index()
r_data = r_data.sort_values(by='Deaths', ascending=False) r_data = r_data[r_data['Deaths']>50]
plt.figure(figsize=(15, 5))
plt.plot(r_data['Country/Region'], r_data['Deaths'],color='red') plt.plot(r_data['Country/Region'], r_data['Confirmed'],color='green') plt.plot(r_data['Country/Region'], r_data['Recovered'], color='blue') plt.plot(r_data['Country/Region'], r_data['Active'], color='black')
plt.title('Total Deaths(>150), Confirmed, Recovered and Active Cases by Country') plt.show()
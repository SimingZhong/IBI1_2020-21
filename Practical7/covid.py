import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:\\Users\嘤嘤怪的一朵玫瑰花\IBI1_2020-21\Practical7")
covid_data = pd.read_csv("full_data.csv")
print(covid_data.iloc[1:11:2, :]) #show all columns and every second row between 0 and 10

total_cases_Boolean = [False, False, False, False, True, False]
total_cases_Afghanistan = covid_data.loc[0:81, total_cases_Boolean]
print(total_cases_Afghanistan)


world_new_cases = covid_data.iloc[7880:7972, 2]
world_new_deaths = covid_data.iloc[7880:7972, 3]

world_mean = np.mean(world_new_cases) #np.mean后面的括号里data type是什么
print('world_mean =',world_mean)

world_median = np.median(world_new_cases)
print('world median =',world_median)

plt.figure()
plt.boxplot(world_new_cases,
            vert=True,
            whis=1.5,
            patch_artist=True,
            showmeans=True,
            meanprops={'marker': 'v', 'color':'green'},
            medianprops={'lw': 1, 'ls':'-','color':'orange'} ,
            showbox=True,
            showcaps=True,
            showfliers=True,
            labels=['World'])
plt.title('New cases of COVID-19')
plt.show()

world_dates = covid_data.iloc[7880:7972, 0]

plt.figure()
plt.title('New cases and new deaths worldwide')
p_new_deaths, = plt.plot(world_dates, world_new_deaths, 'g.')
p_new_cases, = plt.plot(world_dates, world_new_cases, 'm.')
plt.xlabel("date")
plt.ylabel("number")
plt.xticks(rotation=90)
plt.legend([p_new_cases, p_new_deaths], ["new cases", "new deaths"],
           loc='best',
           frameon=False)




#Ask one other question

total_cases_South_Korea = covid_data.iloc[6627:6719, 4]
South_Korea_dates = covid_data.iloc[6627:6719, 0]
total_cases_Kenya = covid_data.iloc[4050:4068, 4]
Kenya_dates = covid_data.iloc[4050:4068, 0]
total_cases_Colombia = covid_data.iloc[1546:1567, 4]
Colombia_dates = covid_data.iloc[1546:1567, 0]

plt.figure()
plt.title('Total cases in three countries with similar populations')
p_South_Korea, = plt.plot(South_Korea_dates, total_cases_South_Korea, 'r.')
p_Kenya, = plt.plot(Kenya_dates, total_cases_Kenya, 'b.')
p_Colombia, = plt.plot(Colombia_dates, total_cases_Colombia,'g.')
plt.xlabel("date")
plt.ylabel("number")
plt.xticks(rotation=90)
plt.legend([p_South_Korea, p_Kenya, p_Colombia], ["South Korea", "Kenya", "Colombia"],
           loc='best',
           frameon=False)





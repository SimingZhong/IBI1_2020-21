
#Use dictionary to store data as key. The total number of cases for countries is associated with the names of countries.

countries = {'USA': 29862124, 'India': 11285561, 'Brazil': 11205972, 'Russia': 4360823, 'UK': 4234924}


#Draw a pie chart.

import matplotlib.pyplot as plt #Import matplotlib
labels = 'USA', 'India', 'Brazil', 'Russia', 'UK' #What the labels are
sizes = [29862124, 11285561, 11205972, 4360823, 4234924] #What are the corresponding numbers
explode = (0.1, 0.1, 0.1, 0.1, 0.1) #Decide which part should split apart.
plt.pie(sizes,explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal') #Design the axes.
plt.show() #Show the pie chart.

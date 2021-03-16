
countries = {'USA': 29862124, 'India': 11285561, 'Brazil': 11205972, 'Russia': 4360823, 'UK': 4234924}
print(countries['USA'])


import matplotlib.pyplot as plt
labels = 'USA', 'India', 'Brazil', 'Russia', 'UK'
sizes = [29862124, 11285561, 11205972, 4360823, 4234924]
explode = (0.1, 0.1, 0.1, 0.1, 0.1)
plt.pie(sizes,explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.show()

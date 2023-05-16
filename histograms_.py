import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ------------------------------
file = open("OS.txt", "r")
data = file.read()
list_OS = data.split("\n")
file.close()
# ------------------------------
file = open("WEB.txt", "r")
data = file.read()
list_WEB = data.split("\n")
file.close()
# ------------------------------
file = open("COUNTRY.txt", "r")
data = file.read()
list_COUNT = data.split("\n")
file.close()
# ------------------------------
country_ids = np.array(list_OS)
# country_ids = np.array(list_WEB)
# country_ids = np.array(list_COUNT)

# Operating_System
# Web_Server_Type
# Country
df = pd.ExcelFile('Hacker_Data_Base.xlsx').parse('Patterns1')
countries = df['Operating_System'].tolist()
countries = [str(c).upper() for c in countries]

countries_ = {i: countries.count(i) for i in countries}
print(countries_)
id_countries = [country for country in countries_.keys()]
plt.bar(range(len(countries_)), list(countries_.values()), align='center')
plt.xticks(range(len(countries_)), list(range(len(id_countries))))
plt.show()

print(len(country_ids))

for i in range(len(id_countries)):
    country = np.where(country_ids == id_countries[i])[0]
    if country.size == 0:
        print(id_countries[i])
        country_ids = np.append(country_ids, np.array(id_countries[i]))

print(len(country_ids))

# Save Operating systems
with open("OS.txt", "w") as file:
    for element in id_countries:
        file.write(element + "\n")
print('----->>> Save successfully !!')

'''
# Save Web_Server_Type
with open("WEB.txt", "w") as file:
    for element in id_countries:
        file.write(element + "\n")
print('----->>> Save successfully !!')

# Save Country
with open("COUNTRY.txt", "w") as file:
    for element in id_countries:
        file.write(element + "\n")
print('----->>> Save successfully !!')
'''
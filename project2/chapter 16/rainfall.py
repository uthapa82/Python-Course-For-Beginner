import csv
from matplotlib import pyplot as plt 
from datetime import datetime

filename = '../sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates = []
    rainfalls = []
    for row in reader:
        try:
            
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            rainfall = float(row[19])
            
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            rainfalls.append(rainfall)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, rainfalls, c='red', alpha=0.9)

plt.fill_between(dates, rainfalls, facecolor='blue', alpha=0.1)
 
title = 'Daily rainfall amount, July 2014'
title += '\n sitka, AK'
plt.title(title, fontsize=21)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()
plt.ylabel("Rainfall(RF)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()    
import csv
from matplotlib import pyplot as plt

from datetime import datetime

filename = '../sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    highs = []
    dates = []
    for row in reader:
        try:
            
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = float(row[1])
            
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.9)

plt.fill_between(dates, highs, facecolor='blue', alpha=0.1)
 
plt.title('Daily Rainfall, July 2014', fontsize=24)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()
plt.ylabel("Rainfall(R)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()    
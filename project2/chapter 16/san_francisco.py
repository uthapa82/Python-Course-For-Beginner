import csv
from matplotlib import pyplot as plt 
from datetime import datetime

filename = '../dataset/sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    highs = []
    lows = []
    for row in reader:
        try:
            high = int(row[1])
            low = int(row[3])
            
        except ValueError:
            print('missing data')
        else:
            highs.append(high)
            lows.append(low)
    
   
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red', alpha=0.9)
plt.plot(lows, c='blue', alpha=0.9)

plt.fill_between(highs, lows, facecolor='blue', alpha=0.1)

plt.title('Daily high & low temperatures, July 2014', fontsize=24)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()    
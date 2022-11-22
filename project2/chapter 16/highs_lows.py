import csv
from matplotlib import pyplot as plt 
from datetime import datetime

filename = '../dataset/death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    highs = []
    dates = []
    lows = []
    for row in reader:
        try:
            
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
            
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    
   
# plotting part 
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.9)
plt.plot(dates, lows, c='blue', alpha=0.9)

#shadding
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# format plot 
plt.title('Daily high & low temperatures, July 2014', fontsize=24)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)


plt.show()    
import csv
from matplotlib import pyplot as plt 
from datetime import datetime

def get_weather_data(filename, dates, highs, lows):
    """get dates, hoghs and lows from file."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

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

dates, highs, lows = [], [], []
get_weather_data('../dataset/sitka_weather_2014.csv', dates, highs, lows)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.9)
plt.plot(dates, lows, c='blue', alpha=0.9)

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# For Death valley.
dates, highs, lows = [], [], []
get_weather_data('../dataset/death_valley_2014.csv', dates, highs, lows)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.9)
plt.plot(dates, lows, c='blue', alpha=0.9)

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

title = "Daily high & low temperatures, July 2014"
title += "\n sitka, AK & Death Valley."
plt.title(title, fontsize=22)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 120)

plt.show()    
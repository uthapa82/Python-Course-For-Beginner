import csv

filename = '../dataset/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    
    temp_high = []
    for temperature in reader:
        temp_high.append(temperature[1])
    
    highs = [int(i) for i in temp_high]
    
    print(highs)
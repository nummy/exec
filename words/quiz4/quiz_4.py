# Uses data available at http://data.worldbank.org/indicator
# on Forest area (sq. km) and Agricultural land area (sq. km).
# Prompts the user for two distinct years between 1990 and 2004
# as well as for a strictly positive integer N,
# and outputs the top N countries where:
# - agricultural land area has increased from oldest input year to most recent input year;
# - forest area has increased from oldest input year to most recent input year;
# - the ratio of increase in agricultural land area to increase in forest area determines
#   output order.
# Countries are output from those whose ratio is largest to those whose ratio is smallest.
# In the unlikely case where many countries share the same ratio, countries are output in
# lexicographic order.
# In case fewer than N countries are found, only that number of countries is output.


# Written by *** and Eric Martin for COMP9021


import sys
import os
import csv
from collections import defaultdict


agricultural_land_filename = 'API_AG.LND.AGRI.K2_DS2_en_csv_v2.csv'
if not os.path.exists(agricultural_land_filename):
    print(f'No file named {agricultural_land_filename} in working directory, giving up...')
    sys.exit()
forest_filename = 'API_AG.LND.FRST.K2_DS2_en_csv_v2.csv'
if not os.path.exists(forest_filename):
    print(f'No file named {forest_filename} in working directory, giving up...')
    sys.exit()
try:
    years = {int(year) for year in
                           input('Input two distinct years in the range 1990 -- 2014: ').split('--')
            }
    if len(years) != 2 or any(year < 1990 or year > 2014 for year in years):
        raise ValueError
except ValueError:
    print('Not a valid range of years, giving up...')
    sys.exit()
try:
    top_n = int(input('Input a strictly positive integer: '))
    if top_n < 0:
        raise ValueError
except ValueError:
    print('Not a valid number, giving up...')
    sys.exit()


countries = []
year_1, year_2 = None, None

# Insert your code here
year_1, year_2 = sorted(list(years))


agricultural_land_fp = open(agricultural_land_filename, "r", encoding="utf8")
forest_fp = open(forest_filename, "r", encoding="utf8")

def read_file(fp):
    data = {}
    reader = csv.reader(fp, delimiter=",")
    count = 0
    for row in reader:
        count += 1
        if count <= 4:
            continue
        if count == 5:
            start_index = row.index(str(year_1))
            end_index = row.index(str(year_2))
        else:
            country = row[0]
            start_data = row[start_index].strip()
            end_data = row[end_index].strip()
            if start_data == "":
                continue
            else:
                try:
                    start_data = float(start_data)
                except ValueError:
                    start_data = int(start_data)
            if end_data != "":
                try:
                    end_data = float(end_data)
                except ValueError:
                    end_data = int(end_data)
            else:
                continue
            if end_data - start_data > 0:
                data[country] = end_data - start_data
    return data

data1 = read_file(agricultural_land_fp)
data2 =read_file(forest_fp)

keys1 = set(data1.keys())
keys2 = set(data2.keys())
keys = keys1.intersection(keys2)


data = []
for key in keys:
    data.append([key, data1[key]/data2[key]])

data  = sorted(data, key=lambda x:x[1], reverse=True)

for country, value in data[:top_n]:
    countries.append("%s (%.2f)" % (country, value))


print(f'Here are the top {top_n} countries or categories where, between {year_1} and {year_2},\n'
      '  agricultural land and forest land areas have both strictly increased,\n'
      '  listed from the countries where the ratio of agricultural land area increase\n'
      '  to forest area increase is largest, to those where that ratio is smallest:')

print('\n'.join(country for country in countries))
    

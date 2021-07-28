import csv
filename="data/death_valley_2018_simple.csv"
with open(filename) as f:
    reader=csv.reader()
    header_row=next(reader)

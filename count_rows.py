import csv
count = 0
with open('data.csv', 'r') as file:
 reader = csv.reader(file)
# Count rows
 for row in reader:
   count += 1
print("Total number of rows in the CSV file:", count)
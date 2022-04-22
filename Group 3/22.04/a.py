import csv

with open("exampleCsvFile.csv", "r", encoding="utf8") as f:
    data = csv.reader(f, delimiter=',')
    line_count = 0
    for row in data:
        if line_count == 0:
            print("The key values are:", *row)
        else:
            print(row)
        line_count += 1

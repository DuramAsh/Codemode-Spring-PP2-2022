import csv

with open("exampleCsvFile.csv", "a", newline="") as f:
    writer = csv.writer(f)
    n = int(input("How many rows do you want to add?\n"))
    for _ in range(n):
        id = input("Enter the id:")
        name = input("Enter the name:")
        age = input("Enter the age:")
        gender = input("Enter the gender:")
        writer.writerow([id, name, age, gender])
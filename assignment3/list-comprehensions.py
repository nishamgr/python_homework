# # Task 3: List Comprehensions Practice

import csv

with open("../csv/employees.csv", newline="") as file:
    # converts to list to slice
    reader = list(csv.reader(file))
    # skips header
    list_of_names = [item[0] + " " + item[1] for item in reader[1:]]
    # to get the names with 'e'
    list_of_e = [item for item in list_of_names if 'e' in item]


    print(list_of_names)
    print(list_of_e)
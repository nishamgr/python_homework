# # Task 3: List Comprehensions Practice

import csv
try:
    with open("../csv/employees.csv", newline="") as file:
    # converts to list to slice
        reader = list(csv.reader(file))
    # skips header
        list_of_names = [f"{item[1].strip()} {item[2].strip()}" for item in reader[1:]]    
    # to get the names with 'e'
        list_of_e = [name for name in list_of_names if 'e' in name.lower()]


        print("Full Names (col 1 + col 2):")
        print(list_of_names)
    
        print("\List containing 'e':")
        print(list_of_e)
except FileNotFoundError:
    print("Error couldn't find '/..csv/employee.csv'.")
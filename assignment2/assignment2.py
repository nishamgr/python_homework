### -------Task:2 Read a CSV File------- ###
import assignment2 as a2
import csv 
import traceback
import sys
import os
import custom_module
from datetime import datetime

def read_employees():
    new_dict = {}
    empty_list = []

    try:
        # open csv file for reading
        with open("../csv/employees.csv", "r", newline="") as file:
            reader = csv.reader(file)
            counter = 0 
            # loop thru the rows
            for row in reader:
                if counter == 0:
                    new_dict["fields"] = row
                else:
                    empty_list.append(row)

                counter +=1

            new_dict["rows"] = empty_list
    # exception handler
    except Exception as e:
        print("An exception occured", type(e).__name__)
        traceback.print_exc()
        sys.exit()

    return new_dict

employees = read_employees()
print(employees)


### -------Task:3: Find the Column Index------- ###

def column_index(col_name):
    # index method
    return employees["fields"].index(col_name) 

employee_id_column = column_index("employee_id")
print(employee_id_column)


### ------Task 4: Find the Employee First Name------ ###

def first_name(row_int):
    # finds col index
    first_name_column_index = column_index("first_name")
    # get the vale in row
    row = employees["rows"][row_int]

    return row[first_name_column_index]

print(first_name(3))


### ------ Task 5: Find the Employee: a Function in a Function ------ ###

def employee_find(employee_id):
    #  checks if a row matches the employee_id
    def employee_match(row):
           return int(row[employee_id_column]) == employee_id
    # filters func to match and return as a list
    matches = list(filter(employee_match, employees["rows"]))
    matches = list(matches)
    return matches

matches = employee_find(3)
print(matches)

### ------ Task 6: Find the Employee with a Lambda ------ ###

def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

matches = employee_find_2(3)
print(matches)

### ------ Task 7: Sort the Rows by last_name Using a Lambda ------ ###

def sort_by_last_name():
    # finds last name clo index
    last_name_column = column_index("last_name")
    # sorts lits of rows in place
    employees["rows"].sort(key=lambda row: row[last_name_column])

    return employees["rows"]

sorted_rows = sort_by_last_name()
print(sorted_rows)

### ------ Task 8: Create a dict for an Employee ------ ###

def employee_dict(row):
    empty_dict = {}
    # loop thru both the header and values using enumerate
    for i, header in enumerate(employees["fields"]):
        if header != "employee_id":
            empty_dict[header] = row[i]
    return empty_dict

employee_info = employee_dict(employees["rows"][0])
print(employee_info)

### ------ Task 9: A dict of dicts, for All Employees ------ ###

def all_employees_dict():
    empty_dict1 = {}
    employee_id_column = column_index("employee_id")

    for row in employees["rows"]:
            employee_id = row[employee_id_column]
            info = employee_dict(row)
            empty_dict1[employee_id] = info

    return empty_dict1

print(all_employees_dict())

### ------ Task 10: Use the os Module ------ ###

def get_this_value():

    return os.getenv("THISVALUE", "ABC")

value = get_this_value
print(value)   


### ------ Task 11: Creating Your Own Module ------ ###

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("swordfish")

print(custom_module.secret)


### ------ Task 12: Read minutes1.csv and minutes2.csv ------ ###

def read_minutes():
    with open("../csv/minutes1.csv", "r", newline="") as file1:
        reader = csv.reader(file1)

        fields1 = next(reader)                #first row = header(column names)
        rows1 = []                            #rows1 list
        # Loop thru rows and append tuples
        for row in reader:
            rows1.append(tuple(row))


    with open("../csv/minutes2.csv", "r", newline="") as file2:
        reader = csv.reader(file2)

        fields2 = next(reader)
        rows2 = []                              #rows2 list 
        # Loop thru rows and append tuples
        for row in reader:
            rows2.append(tuple(row))
    #final dictionaries
    minutes1_dict = {"fields": fields1, "rows": rows1}
    minutes2_dict = {"fields": fields2, "rows": rows2}


    return minutes1_dict, minutes2_dict
minutes1, minutes2 = read_minutes()         #stored returned dict in global variables

print(minutes1)
print(minutes2)

### ------ Task 13: Create minutes_set ------ ###

def create_minutes_set():
    #convert rows lists to set
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])

    #combine the two sets(union)
    minutes_set = set1.union(set2)

    return minutes_set
minutes_set = create_minutes_set()

### ------ Task 14: Convert to datetime ------ ###

def create_minutes_list():
    #conversion to a list
    minutes_list = list(minutes_set)
    #map() func and lambda
    minutes_list = list(map(lambda row : (row[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))

    return minutes_list

minutes_list = create_minutes_list()
print(minutes_list)

### ------ Task 15: Write Out Sorted List ------ ###

def write_sorted_list():
    sorted_list = sorted(minutes_list, key = lambda x: x[1])
    #datetime to str
    converted_list = list(map(lambda x : (x[0], x[1].strptime("%B %d, %Y")), sorted_list))
    #opens the file
    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)                 #csv writer
        writer.writerow(minutes1["fields"])           #header row
        #loop over converted and sorted list
        for row in converted_list:
            writer.writerow(row)

    return converted_list

converted_minutes_list = write_sorted_list()
print(converted_minutes_list)






















### -------Task:2 Read a CSV File------- ###

import csv 
import traceback
import sys

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
# print(employees)


### -------Task:3: Find the Column Index------- ###

def column_index(col_name):
    # index method
    return employees["fields"].index(col_name) 

employee_id_column = column_index("employee_id")
# print(employee_id_column)


### ------Task 4: Find the Employee First Name------ ###

def first_name(row_int):
    # finds col index
    first_name_column_index = column_index("first_name")
    # get the vale in row
    row = employees["rows"][row_int]

    return row[first_name_column_index]

# print(first_name(3))


### ------ Task 5: Find the Employee: a Function in a Function ------ ###

def employee_find(employee_id):
    #  checks if a row matches the employee_id
    def employee_match(row):
           return int(row[employee_id_column]) == employee_id
    # filters func to match and return as a list
    matches = list(filter(employee_match, employees["rows"]))
    matches = list(matches)
    return matches

# matches = employee_find(3)
# print(matches)

### ------ Task 6: Find the Employee with a Lambda ------ ###

def employee_find2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

# matches = employee_find2(3)
# print(matches)

### ------ Task 7: Sort the Rows by last_name Using a Lambda ------ ###

def sort_by_last_name():
    # finds last name clo index
    last_name_column = column_index("last_name")
    # sorts lits of rows in place
    employees["rows"].sort(key=lambda row: row[last_name_column])

    return employees["rows"]

# sorted_rows = sort_by_last_name()
# print(sorted_rows)

### ------ Task 8: Create a dict for an Employee ------ ###

def employee_dict(row):
    empty_dict = {}
    # loop thru both the header and values using enumerate
    for i, header in enumerate(employees["fields"]):
        if header != "employee_id":
            empty_dict[header] = row[i]
    return empty_dict

# employee_info = employee_dict(employees["rows"][0])
# print(employee_info)






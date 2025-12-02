def employee_details(name,emp_id,department,salary):
    result=(
        f"Employee Name: {name}, "
        f"Employee ID: {emp_id}, "
        f"Department: {department}, "
        f"Salary: {salary}"
    )
    return result
if __name__=="__main__":
    name="alice"
    emp_id="ed101"
    department="IT"
    salary=55000 
    print(employee_details(name,emp_id,department,salary))


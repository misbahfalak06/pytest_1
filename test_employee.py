from employee import employee_details
def test_employee_details():
    expected_output=(
        "Employee Name: Alice \n"
        "Employee ID: ED101 \n"
        "Department: IT \n"
        "Salary: 55000"
    )
    assert employee_details("Alice","ED101","IT",55000)==expected_output

first_name = input("Enter employee's first name: ")
last_name = input("Enter employee's last name: ")
full_name = first_name + ' ' + last_name
address = input("Enter employee's full address: ")
employee_age = int(input("Enter employee's age: "))
employee_info = full_name + ' is ' + str(employee_age)
print(employee_info)
years_experience = int(input("Enter years of experience: "))
experience_info = 'Experience: ' + str(years_experience) + ' years'
print(experience_info)
position = input("Enter employee's position: ")
salary = int(input("Enter employee's salary: "))
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)
employee_code = input("Enter employee code (e.g., DEV-2026-JD-001): ")
department = employee_code[0:3]
print(department)
year_code = employee_code[4:8]
print(year_code)
initials = employee_code[9:11]
print(initials)
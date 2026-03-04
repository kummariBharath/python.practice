def get_valid_number(prompt):
    """Helper function to ensure user enters a valid number."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_profile():
    print("\n--- New Employee Entry ---")
    first_name = input("Enter employee's first name: ").strip().capitalize() #strip() to remove extra spaces, capitalize() to format name
    last_name = input("Enter employee's last name: ").strip().capitalize()
    full_name = f"{first_name} {last_name}"
    
    address = input("Enter employee's full address: ")
    
    # Using the helper function for validation
    employee_age = get_valid_number("Enter employee's age: ")
    years_experience = get_valid_number("Enter years of experience: ")
    
    position = input("Enter employee's position: ")
    salary = get_valid_number("Enter employee's salary: ")
    
    # Logic: Calculate a performance bonus (e.g., $1,500 per year of experience)
    performance_bonus = years_experience * 1500
    total_compensation = salary + performance_bonus

    employee_code = input("Enter employee code (e.g., DEV-2026-JD-001): ")
    
    # Safe slicing with defaults if code is too short
    department = employee_code[0:3].upper() if len(employee_code) >= 3 else "N/A"
    year_code = employee_code[4:8] if len(employee_code) >= 8 else "N/A"

    # Professional Output Card
    print("\n" + "="*50)
    print(f"       EMPLOYEE PROFILE: {full_name.upper()}") 
    print("="*50)
    print(f"Position:      {position}")
    print(f"Department:    {department} (Hired: {year_code})")
    print(f"Age:           {employee_age}")
    print(f"Address:       {address}")
    print("-" * 50)
    print(f"Base Salary:   ${salary:,}")
    print(f"Experience:    {years_experience} years")
    print(f"Annual Bonus:  ${performance_bonus:,}")
    print(f"Total Comp:    ${total_compensation:,}")
    print("="*50 + "\n")

# Main loop to keep the program running
while True:
    generate_profile()
    repeat = input("Do you want to generate another profile? (yes/no): ").lower()
    if repeat != 'yes':
        print("Exiting program. Goodbye!")
        break
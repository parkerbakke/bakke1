# Parker Bakke
# CBIS 4210
# 8/28/24
# Assignment 1.2

# 2: Employee Payroll Calculation

def main():
    # Sample employee data
    employees = [
        {"employee_id": "E001", "name": "Alice", "hours_worked": 40, "hourly_rate": 25.00, "tax_rate": 0.20},
        {"employee_id": "E002", "name": "Bob", "hours_worked": 35, "hourly_rate": 30.00, "tax_rate": 0.22},
        {"employee_id": "E003", "name": "Charlie", "hours_worked": 45, "hourly_rate": 20.00, "tax_rate": 0.18},
    ]

    # Sample bonus data
    bonuses = [
        {"employee_id": "E001", "bonus_amount": 500.00},
        {"employee_id": "E003", "bonus_amount": 300.00},
    ]

    # Task 1: Calculate Gross Pay
    employee_gross_pay = {}
    for employee in employees:
        gross_pay = employee["hours_worked"] * employee["hourly_rate"]

        # Check if the employee has a bonus
        for bonus in bonuses:
            if bonus["employee_id"] == employee["employee_id"]:
                gross_pay += bonus["bonus_amount"]
                break

        employee_gross_pay[employee["name"]] = gross_pay

    print("Gross Pay for Each Employee:")
    print(employee_gross_pay)

    # Task 2: Calculate Net Pay
    employee_net_pay = {}
    for employee in employees:
        gross_pay = employee_gross_pay[employee["name"]]
        tax = gross_pay * employee["tax_rate"]
        net_pay = gross_pay - tax
        employee_net_pay[employee["name"]] = net_pay

    print("Net Pay for Each Employee:")
    print(employee_net_pay)

    # Task 3: Generate Payroll Report
    print("Payroll Report:")
    for employee in employees:
        gross_pay = employee_gross_pay[employee["name"]]
        tax = gross_pay * employee["tax_rate"]
        net_pay = employee_net_pay[employee["name"]]
        print(f"Employee: {employee['name']}")
        print(f"  Gross Pay: ${gross_pay:.2f}")
        print(f"  Tax Deducted: ${tax:.2f}")
        print(f"  Net Pay: ${net_pay:.2f}")
        print("--------------------------")


if __name__ == "__main__":
    main()
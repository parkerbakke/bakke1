# Parker Bakke
# CBIS 4210
# 8/28/24
# Assignment 1.1

# 1: Inventory Management System

def main():
    # Sample inventory data
    inventory = [
        {"product": "Laptop", "quantity_in_stock": 10, "restock_level": 5, "restock_amount": 10},
        {"product": "Phone", "quantity_in_stock": 15, "restock_level": 10, "restock_amount": 20},
        {"product": "Monitor", "quantity_in_stock": 8, "restock_level": 3, "restock_amount": 5},
    ]

    # Sample sales data
    sales = [
        {"product": "Laptop", "quantity_sold": 3},
        {"product": "Phone", "quantity_sold": 7},
        {"product": "Monitor", "quantity_sold": 4},
    ]

    # Task 1: Update Inventory Based on Sales
    for sale in sales:
        for item in inventory:
            if item["product"] == sale["product"]:
                item["quantity_in_stock"] -= sale["quantity_sold"]
                break

    print("Updated Inventory After Sales:")
    for item in inventory:
        print(f"{item['product']}: {item['quantity_in_stock']} units in stock")

    # Task 2: Check for Products That Need Restocking
    products_to_restock = []
    for item in inventory:
        if item["quantity_in_stock"] <= item["restock_level"]:
            products_to_restock.append(item["product"])

    print("Products That Need Restocking:")
    print(products_to_restock)

    # Task 3: Generate a Restocking Order
    restocking_order = []
    for item in inventory:
        if item["product"] in products_to_restock:
            restocking_order.append({
                "product": item["product"],
                "quantity_to_order": item["restock_amount"]
            })

    print("Restocking Order:")
    for order in restocking_order:
        print(f"{order['product']}: Order {order['quantity_to_order']} units")


if __name__ == "__main__":
    main()


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


# 3: Customer Segmentation and Discount Allocation

from datetime import datetime


def main():
    # Sample customer data
    customers = [
        {"customer_id": "C001", "name": "Alice", "total_spent": 1200.00,
         "purchase_history": [{"purchase_date": "2024-02-01", "amount": 500.00},
                              {"purchase_date": "2024-05-01", "amount": 700.00}]},

        {"customer_id": "C002", "name": "Bob", "total_spent": 750.00,
         "purchase_history": [{"purchase_date": "2023-12-15", "amount": 300.00},
                              {"purchase_date": "2024-04-10", "amount": 450.00}]},

        {"customer_id": "C003", "name": "Charlie", "total_spent": 300.00,
         "purchase_history": [{"purchase_date": "2023-01-10", "amount": 200.00},
                              {"purchase_date": "2023-03-15", "amount": 100.00}]}
    ]

    # Task 1: Segment Customers
    segments = {}
    for customer in customers:
        if customer["total_spent"] > 1000:
            segments[customer["customer_id"]] = "Gold"
        elif customer["total_spent"] >= 500:
            segments[customer["customer_id"]] = "Silver"
        else:
            segments[customer["customer_id"]] = "Bronze"

    # Task 2: Allocate Discounts
    discounts = {}
    for customer_id, segment in segments.items():
        if segment == "Gold":
            discounts[customer_id] = 0.20
        elif segment == "Silver":
            discounts[customer_id] = 0.10
        else:
            discounts[customer_id] = 0.05

    # Task 3: Identify Inactive Customers
    inactive_customers = []
    current_date = datetime.strptime("2024-08-26", "%Y-%m-%d")
    for customer in customers:
        last_purchase_date = max(datetime.strptime(purchase["purchase_date"], "%Y-%m-%d")
                                 for purchase in customer["purchase_history"])
        if (current_date - last_purchase_date).days > 180:
            inactive_customers.append(customer["customer_id"])

    # Task 4: Generate Report
    print("Customer Segmentation and Discount Report")
    for customer in customers:
        customer_id = customer["customer_id"]
        segment = segments[customer_id]
        discount = discounts[customer_id] * 100  # Convert to percentage
        inactive_status = "Yes" if customer_id in inactive_customers else "No"

        print(f"Name: {customer['name']}")
        print(f"  Total Spent: ${customer['total_spent']:.2f}")
        print(f"  Segment: {segment}")
        print(f"  Discount: {discount:.0f}%")
        print(f"  Inactive (Re-engagement Needed): {inactive_status}")
        print("--------------------------")


if __name__ == "__main__":
    main()


# 4: Project Management and Employee Assignment

def main():
    # Sample project data
    projects = [
        {"project_id": "P001", "name": "Project Alpha", "required_skills": ["Python", "SQL"], "budget": 10000},
        {"project_id": "P002", "name": "Project Beta", "required_skills": ["Java", "AWS"], "budget": 15000},
        {"project_id": "P003", "name": "Project Gamma", "required_skills": ["JavaScript", "React"], "budget": 8000},
    ]

    # Sample employee data
    employees = [
        {"employee_id": "E001", "name": "Alice", "skills": ["Python", "SQL"], "hourly_rate": 50, "available_hours": 100},
        {"employee_id": "E002", "name": "Bob", "skills": ["Java", "AWS"], "hourly_rate": 60, "available_hours": 80},
        {"employee_id": "E003", "name": "Charlie", "skills": ["JavaScript", "React"], "hourly_rate": 55, "available_hours": 90},
    ]

    # Task 1: Assign Employees to Projects
    project_assignments = {}
    for project in projects:
        assigned_employees = []
        for employee in employees:
            if all(skill in employee["skills"] for skill in project["required_skills"]):
                assigned_employees.append(employee)
        project_assignments[project["project_id"]] = assigned_employees

    # Task 2: Calculate Total Cost for Each Project
    project_costs = {}
    for project in projects:
        total_cost = 0
        for employee in project_assignments[project["project_id"]]:
            total_cost += employee["hourly_rate"] * employee["available_hours"]
        project_costs[project["project_id"]] = total_cost

    # Task 3: Generate Project Report
    print("Project Report:")
    for project in projects:
        project_id = project["project_id"]
        assigned_employees = project_assignments[project_id]
        total_cost = project_costs[project_id]

        print(f"Project: {project['name']}")
        print(f"  Budget: ${project['budget']:.2f}")
        print(f"  Total Cost: ${total_cost:.2f}")
        print("  Assigned Employees:")
        for employee in assigned_employees:
            print(f"    {employee['name']} (Rate: ${employee['hourly_rate']}/hr, Available Hours: {employee['available_hours']})")
            print(f"    Skills: {', '.join(employee['skills'])}")
        print("--------------------------")

if __name__ == "__main__":
    main()
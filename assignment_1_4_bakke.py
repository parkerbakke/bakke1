# Parker Bakke
# CBIS 4210
# 8/28/24
# Assignment 1.4

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
# Parker Bakke
# CBIS 4210
# 8/28/24
# Assignment 1.3

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
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
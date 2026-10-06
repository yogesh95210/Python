# write function to calculate item total item cost

def calculate_total_cost(items_list):
    total_cost = 0
    for item in items_list:
        # Multiply price by quantity for each item and add to total
        total_cost += item["price"] * item["quantity"]
    return total_cost

# --- TEST INPUT (Array of Objects / List of Dicts) ---
cart = [
    {"name": "Laptop", "price": 55000, "quantity": 1},
    {"name": "Wireless Mouse", "price": 1200, "quantity": 2},
    {"name": "HDMI Cable", "price": 350, "quantity": 3},
    {"name": "Keyboard", "price": 2500, "quantity": 1}
]

# Execution
grand_total = calculate_total_cost(cart)
print(grand_total)


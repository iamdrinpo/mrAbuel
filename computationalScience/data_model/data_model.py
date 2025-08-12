class Order:
    def __init__(self, item_name, quantity, price):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price
        self.total = quantity * price

orders = []

menus = {
    'Burger': 80,
    'Fries': 50,
    'Spaghetti': 100,
    'Halo-Halo': 70
}

choice = input("Would you like to order something? (yes/no): ").lower()

if choice == "yes":
    print("\nAvailable menus with prices:")
    for item, price in menus.items():
        print(f"- {item}: ₱{price}")

    while True:
        item = input("\nEnter an item to order (or type 'done' to finish): ").title()
        if item.lower() == "done":
            break
        if item not in menus:
            print("That item is not on the menu.")
            continue

        quantity = input("Enter the quantity: ")
        if not quantity.isdigit():
            print("Please enter a valid number.")
            continue

        quantity = int(quantity)
        price = menus[item]
        orders.append(Order(item, quantity, price))


    print("\n Your Orders:")
    grand_total = 0
    for order in orders:
        print(f"- {order.item_name} x{order.quantity} = ₱{order.total}")
        grand_total += order.total

    print(f"\n Total Amount: ₱{grand_total}")
else:
    print("No order placed.")
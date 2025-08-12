 # Ordering System (Data Model)

This Python program implements a simple ordering system using a **data model** to represent customer orders.
It demonstrates basic class-based programming in Python to store order details, calculate totals, and display a receipt.

## Data Model

### `Order` Class

Represents a single order entry with:

* **Attributes**:

  * `item_name` (string) — the name of the menu item ordered.
  * `quantity` (int) — the number of units ordered.
  * `price` (float/int) — the price per unit of the item.
  * `total` (float/int) — the computed total cost for this order (`quantity × price`).

* **Constructor**:

  * Automatically calculates `total` upon object creation.

Example:

```python
order1 = Order("Burger", 2, 80)
print(order1.total)  # 160
```

## Features

* Predefined menu stored in a dictionary for easy modification.
* Interactive ordering process:

  * Displays menu with prices.
  * Validates item selection against the menu.
  * Ensures quantity input is numeric.
* Uses the `Order` class to store orders in a list.
* Calculates and displays:

  * Total for each ordered item.
  * Grand total for all items.

## How It Works

1. The program asks if the user wants to place an order.
2. If **yes**, it displays the menu and starts the ordering loop.
3. The user enters an item name and quantity.
4. An `Order` object is created and stored in a list.
5. When the user types `done`, the program:

   * Iterates over the list of `Order` objects.
   * Prints each item, quantity, and total cost.
   * Calculates and displays the grand total.

## Example

```
Would you like to order something? (yes/no): yes

Available menus with prices:
- Burger: ₱80
- Fries: ₱50
- Spaghetti: ₱100
- Halo-Halo: ₱70

Enter an item to order (or type 'done' to finish): burger
Enter the quantity: 2

Enter an item to order (or type 'done' to finish): fries
Enter the quantity: 1

Enter an item to order (or type 'done' to finish): done

 Your Orders:
- Burger x2 = ₱160
- Fries x1 = ₱50

 Total Amount: ₱210
```
---

## Full Source Code

```python
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
```

## **Requirements**

* Python **3.6+** installed on your system.
* A code editor or IDE (e.g., VS Code, PyCharm, Sublime Text) or simply the Python IDLE.
* No external libraries required — uses only Python built-ins.
* Basic understanding of how to run Python scripts from terminal/command prompt.

import json
import os

FILE = "mart_data.json"

# ---------------------- Load / Save Data ----------------------
def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---------------------- Mart Functions ----------------------
def add_item(data):
    item = input("Enter item name: ").lower()
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))

    data[item] = {"price": price, "qty": qty}
    save_data(data)
    print("Item added successfully!")

def view_items(data):
    if not data:
        print("No items available!")
        return

    print("\n---- Item List ----")
    for item, details in data.items():
        print(f"{item.title()} - Rs.{details['price']}  | Qty: {details['qty']}")
    print("--------------------")

def update_quantity(data):
    item = input("Enter item name to update: ").lower()
    if item in data:
        new_qty = int(input("Enter new quantity: "))
        data[item]["qty"] = new_qty
        save_data(data)
        print("Quantity updated!")
    else:
        print("Item not found!")

def delete_item(data):
    item = input("Enter item name to delete: ").lower()
    if item in data:
        del data[item]
        save_data(data)
        print("Item deleted!")
    else:
        print("Item not found!")

def generate_bill(data):
    cart_total = 0
    while True:
        item = input("Enter item to buy (or 'stop' to finish): ").lower()
        if item == "stop":
            break

        if item not in data:
            print("Item not found!")
            continue

        qty = int(input("Enter quantity: "))
         # Convert JSON values to numeric
        unit_price = float(data[item]["price"])
        available_qty = int(data[item]["qty"])

        if qty > data[item]["qty"]:
            print("Not enough stock!")
            continue

        price = unit_price * qty
        cart_total = cart_total + price

        # Reduce the store quantity
        data[item]["qty"] = available_qty - qty
        save_data(data)

        print(f"Added to bill: Rs. {price}")

    print("\n------ FINAL BILL ------")
    print(f"Total Amount: Rs. {cart_total}")
    print("-------------------------")

# ---------------------- Main Program Loop ----------------------
def main():
    data = load_data()

    while True:
        print("\n=== Mart Management System ===")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Quantity")
        print("4. Delete Item")
        print("5. Generate Bill")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_item(data)
        elif choice == "2":
            view_items(data)
        elif choice == "3":
            update_quantity(data)
        elif choice == "4":
            delete_item(data)
        elif choice == "5":
            generate_bill(data)
        elif choice == "6":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
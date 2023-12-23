class Item:
    def __init__(self, item_id, name, price):
        self.id = item_id
        self.name = name
        self.price = price

class Supermarket:
    def __init__(self):
        self.items = []

    def add_item(self):
        item_id = int(input("\nEnter Item ID: "))
        name = input("Enter Item Name: ")
        price = float(input("Enter Item Price: $"))
        new_item = Item(item_id, name, price)
        self.items.append(new_item)
        print("\nItem added successfully!")

    def edit_item(self):
        item_id = int(input("\nEnter Item ID to Edit: "))

        for item in self.items:
            if item.id == item_id:
                item.name = input("Enter New Item Name: ")
                item.price = float(input("Enter New Item Price: $"))
                print("\nItem edited successfully!")
                return

        print("\nItem not found!")

    def remove_item(self):
        item_id = int(input("\nEnter Item ID to Remove: "))

        for item in self.items:
            if item.id == item_id:
                self.items.remove(item)
                print("\nItem removed successfully!")
                return

        print("\nItem not found!")

    def show_item_details(self):
        print("\nItem Details:")
        print("{:<5} {:<20} {:<10}".format("ID", "Name", "Price"))
        print("-" * 35)

        for item in self.items:
            print("{:<5} {:<20} {:<10.2f}".format(item.id, item.name, item.price))

    def generate_bill(self):
        total = 0

        print("\nGenerate Bill:")
        while True:
            item_id = int(input("Enter Item ID (0 to end): "))

            if item_id == 0:
                break

            item = next((item for item in self.items if item.id == item_id), None)
            if item:
                quantity = int(input("Enter Quantity: "))
                total += item.price * quantity
            else:
                print("\nItem not found!")

        print("\nTotal Bill: ${:.2f}".format(total))

def main():
    print(" \n")
    print("                ' W  E  L     C  O  M  E '\n")
    print("                ``````````````````````````\n")

    print("---------------------------------------------------------\n")
    print("  Program  Devolper:    MOHAMMAD  HASSAN  RAZA \n")
    print("---------------------------------------------------------\n")

    supermarket = Supermarket()
    choice = 0

    while choice != 6:
        print("** Super Market Billing System **")
        print("---------------------------------------------------------")
        print("1. Add Item")
        print("2. Edit Item")
        print("3. Remove Item")
        print("4. Show Item Details")
        print("5. Generate Bill")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            supermarket.add_item()
        elif choice == 2:
            supermarket.edit_item()
        elif choice == 3:
            supermarket.remove_item()
        elif choice == 4:
            supermarket.show_item_details()
        elif choice == 5:
            supermarket.generate_bill()
        elif choice == 6:
            print("\nExiting Super Market Billing System. Goodbye!")
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()

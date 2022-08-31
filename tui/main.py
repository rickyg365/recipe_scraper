import os

# API
from utils.api import Api, ShoppingApi, PeopleApi



class ShoppingLogger:
    def __init__(self):
        self.client = None

    def __str__(self) -> str:
        txt = ""
        return txt
    
    def log_trip(self):
        # Trip Details
        store = input("Store: ")
        date = input("Todays Date: ")
        
        # Check dir for store
        store_dir = f"data/shopping_data/{store}"
        if not os.path.exists(store_dir):
            os.mkdir(store_dir)

        # Start Client
        self.client = ShoppingApi(f"{store_dir}/{date}.json")

        # Display Data
        self.client.show_all()

        # Choose






if __name__ == '__main__':
    # Log Shopping Trips
    # Input Trip Details
    current_store = "target"
    current_date = "2022_08_03"

    client = ShoppingApi(f"data/shopping_data/{current_store}/{current_date}.json")

    # Load Entries
    client.load()

    # See All Entries
    client.show_all()

    # Choose Action
    # - Add Entries
    # - Update Entries
    # - Search Entries
    # - Delete Entries
    print("""
[A]: Add
[U]: Update
[S]: Search
[D]: Delete
""")
    u_action = input("Choose Action: ")

    match u_action:
        case _:
            pass

    # Add Entries
    print("\nAdd Entries: ")
    while True:
        print()
        # Input Data
        input_data = {
            "name": input("Item Name: "),
            "quantity": int(input("Quantity: ")),
            "price": float(input("Price: ")),
            "store": current_store
        }
        # Create Entry
        client.create(**input_data)

        again = input("\nInsert another entry?: ")

        if again == 'q':
            break

    # Update Entries
    # Search Entries
    # Delete Entries

    # Save Data
    client.save()

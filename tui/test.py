import os
from typing import Dict, Any

# Models
from models.person import Person
from models.shopping_item import ShoppingItem

# Save, Load Utils
from utils.files import save, load, FILE_TYPE


def main():
    return

if __name__ == "__main__":
    # Save Json
    # save(test_data, "test.json", FILE_TYPE.JSON)
    
    # Save Pickle
    # save(test_object, "test.pickle", FILE_TYPE.PICKLE)

    # Load Json
    # loaded_data = load_json("test.json")
    # loaded_data = load("test.json", FILE_TYPE.JSON)


    # Load Pickle
    # loaded_obj = load_pickle("test.pickle")
    # loaded_obj = load("test.pickle", FILE_TYPE.PICKLE)
    ...

    # Raw Data
    # sample_data = {
    #     "name": "Test Name",
    #     "age": 1
    # }

    # Load Data
    # sample_data = load("data/raw_data.json", FILE_TYPE.JSON)
    # sample_obj = load("data/raw_object.pickle", FILE_TYPE.PICKLE)

    # Create Object
    # character = Person(**sample_data)

    # Display Object
    # print(character)
    # print(f"clone: {sample_obj}")

    # Save Data
    # save(sample_data, "data/raw_data.json", FILE_TYPE.JSON)

    # save(character, "data/raw_object.pickle", FILE_TYPE.PICKLE)

    ...

    # Start App
    # my_app = Api("app_data.json", ShoppingItem)
    # my_app = ShoppingApi("data/test/app_data.json")

    # Person Data
    # new_data = {
    #     "name": "You Thought",
    #     "age": 22
    # }

    # ShoppingItem Data
    # shopping_data = {
    #     "name": "Yerba Mate - Tropical Uprising",
    #     "quantity": 1,
    #     "price": 2.99,
    #     "total_price": 2.99,
    #     "store": "Target"
    # }

    # Create
    # my_app.create(shopping_data)

    # Read
    # entry = my_app.read(0)

    # Update
    # update_data = {
    #     "quantity": 32
    # }
    # updated_entry = my_app.update(0, update_data)

    # Display
    # print(entry)
    # print(updated_entry)
    # print(my_app)

    # Save
    # my_app.save()

    # Delete
    # my_app.delete(0)

    # print(my_app)
    ...

    # current_store = "target"
    # current_date = "2022_08_03"
    
    # new_api = Api(f"data/shopping_data/{current_date}_{current_store}.json", ShoppingItem)
    # new_api = ShoppingApi(f"data/shopping_data/{current_store}/{current_date}.json")

    # Load
    # new_api.load()

    # new_api.show_all()

    # Create
    # item1 = {
    #     "name": "Sprite",
    #     "quantity": 2,
    #     "price": 1.29,
    #     "store": current_store
    # }
    
    # item2 = {
    #     "name": "Takis",
    #     "quantity": 1,
    #     "price": 1.89,
    #     "store": current_store
    # }
    

    # new_api.create(**item1)
    # new_api.create(**item2)


    # Read
#     i1 = new_api.read(0)
#     i2 = new_api.read(1)

#     ri1 = new_api.read(0, True)
#     ri2 = new_api.read(1, True)
    
#     print(f"""
# Item 1:  {i1}
# Item 2:  {i2}

# Raw Item 1: {ri1}
# Raw Item 2: {ri2}
# """)

    # Update
    # new_api.update(0, {"price": 1.99})  # 0: Sprite
    # new_api.update(1, {"price": 2.99})  # 1: Takis

    # Delete

    # Save
    # new_api.save()



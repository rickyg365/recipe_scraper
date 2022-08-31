from typing import Dict, Any

# Models
from models.person import Person
from models.shopping_item import ShoppingItem

# Save, Load Utils
from utils.files import save, load, FILE_TYPE

"""  
------------------------------------------
CRUD API
------------------------------------------
Create
Read
Update
Delete
"""

#  Raw Data -> dict  |  Data -> Model/Object

class Api:
    def __init__(self, path: str, model_type: Any):
        # Meta Data
        self.path = path
        self.model = model_type

        # Data
        self.data = []  # Raw Data -> Dicts
        self.working_data = []  # Working Data -> Models

        # Initial Load
        # self.load()
  
    def show_all(self):
        print("All Entries: ")
        for e in self.working_data:
            print(e) 

    def load(self):
        # Load Raw Data
        self.data = load(self.path, FILE_TYPE.JSON)

        # Create Working Data(Models), or load from pickle
        for entry in self.data:
            self.working_data.append(self.model(**entry))
        
        # self.working_data = load(f"{self.path}.pickle", FILE_TYPE.PICKLE)

    def save(self):        
        # save(self.working_data, f"{self.path}.pickle", FILE_TYPE.PICKLE)
        return save(self.data, self.path, FILE_TYPE.JSON)

    def create(self, raw_data: Dict[str, Any]):
        """ Needs Custom implementation """
        # Add Raw Data
        self.data.append(raw_data)

        # Create and Add Model Instance
        self.working_data.append(self.model(**raw_data))
        return
    
    def read(self, key: int, return_raw_data: bool=False):
        """ select entry by index """
        # Raw Data
        if return_raw_data:
            return self.data[key]
        
        # Working Data
        return self.working_data[key]
    
    def update(self, key: int, new_data: Dict[str, Any]):
        """ Needs Custom implementation """
        # Update raw data
        for dk, dv in new_data.items():
            if dk in self.data[key]:
                self.data[key][dk] = dv
        
        # Create new model from updated data
        updated_data = {**self.data[key], **new_data}
        self.working_data[key] = self.model(**updated_data)

        return self.data[key]

    def delete(self, key: int):
        # Remove Raw Data
        self.data.pop(key)
        
        # Remove Working Data
        self.working_data.pop(key)
        return


# Inherited
class PeopleApi(Api):
    def __init__(self, path: str):
        super().__init__(path, Person)

    def create(self, name: str, age: int):
        raw_person_data = {
            "name": name,
            "age": age
        }
        return super().create(raw_person_data)


class ShoppingApi(Api):
    def __init__(self, path: str):
        super().__init__(path, ShoppingItem)
    
    def create(self, name: str, quantity: int, price: float, store: str):
        raw_shopping_data = {
            "name": name,
            "quantity": quantity,
            "price": price,
            "store": store,
        }
        return super().create(raw_shopping_data)



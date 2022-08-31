import json
import pickle

from enum import Enum
from typing import Any, Dict


"""
Handle saving and loading data in various formats
- json
- pickle
- csv
"""

# Types - Custom
class FILE_TYPE(Enum):
    JSON = "json"
    PICKLE = "pickle"
    CSV = "csv"


# JSON - Dict[str, any]
def save_json(data: Dict[str, Any], filepath: str):
    with open(filepath, 'w') as out_file:
        json.dump(data, out_file, indent=4)

def load_json(filepath: str) -> Dict[str, Any]:
    with open(filepath, 'r') as in_file:
        new_data = json.load(in_file)
    return new_data

# PICKLE - Any
def save_pickle(object: Any, filepath: str):
    with open(filepath, 'wb') as out_file:
        pickle.dump(object, out_file)

def load_pickle(filepath: str) -> Any:
    with open(filepath, 'rb') as in_file:
        new_data = pickle.load(in_file)
    return new_data

# CSV - pd.dataframe? or Dict[str, List[Any]] (key: [*data])
def save_csv(data: Any, filepath: str):
    return

def load_csv(filepath: str) -> Any:
    return


# Functions - Utility
def save(data: any, filepath: str, file_type: FILE_TYPE=FILE_TYPE.JSON):
    """ Save a object using pickle or a dict using json or csv file formats
        data: obj | dict, 
        filepath: str, 
        file_type: FILE_TYPE 
    """
    match file_type:
        case FILE_TYPE.JSON:
            save_json(data, filepath)
        case FILE_TYPE.PICKLE:
            save_pickle(data, filepath)
        # case FILE_TYPE.CSV:
        #     save_csv(data, filepath)
        case _:
            print("Unable to Save: Unrecognized file type...")
            return False
    return True

def load(filepath: str, file_type: FILE_TYPE=FILE_TYPE.JSON):
    """ Load a file """
    new_data = None
    match file_type:
        case FILE_TYPE.JSON:
            new_data = load_json(filepath)
        case FILE_TYPE.PICKLE:
            new_data = load_pickle(filepath)
        # case FILE_TYPE.CSV:
        #     new_data = load_csv(filepath)
        case _:
            print("Unable to Load: Unrecognized file type...")            
    return new_data



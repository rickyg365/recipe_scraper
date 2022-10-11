import os
import json

from typing import List, Dict


def save_txt(data: str, filepath: str):
    """ Save txt into a .txt file """
    # Is try the best way to handle errors here?
    try:
        with open(filepath, 'w') as out_txt:
            out_txt.write(data)
        return True
    except Exception as e:
        return False

def save_json(data: Dict[any, any], filepath: str):
    """ Save dict into json file """
    try:
        with open(filepath, 'w') as out_json:
            json.dump(data, out_json, indent=4)
        return True
    except Exception as e:
        return False


def load_txt(filepath: str) -> str:
    """ Load String from text file """
    try:
        with open(filepath, 'r') as in_txt:
            new_data = in_txt.read()
        return new_data
    except FileNotFoundError:
        return False
    
def load_json(filepath: str) -> Dict[any, any]:
    """ Load dict from json file """
    try:
        with open(filepath, 'r') as in_json:
            new_data = json.load(in_json)
        return new_data
    except FileNotFoundError:
        return False
    

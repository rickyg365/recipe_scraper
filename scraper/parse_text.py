import os
import json

from enum import Enum
from typing import List, Dict


class LineType(Enum):
    HEADING: str = "H"
    PARAGRAPH: str = "P"
    LIST: List[str] = "Li"

# Im probably gonna remove the str | List[str] and just commit to one or the other
def assign_line_data(data_type: LineType, data: str | List[str]):
    return {
        "data-type": data_type,
        "data": data
    }

def recipe_txt_parser(filepath: str) -> Dict[str, str | List[str]]:
    # "data/funnel_cake_fries_recipe.txt"
    with open(filepath, 'r') as in_file:
        # Default Variables
        line_symbol = ""  # Keeps track of current lines type

        new_line_count = 0  # Count of lines that have been new lines
        line_count = 0  # Consecutive non newline count
        
        # Storage Variables
        complete_data = []  # Stores complete data 
        debug_data = []  # Stores Debug Data

        # Iteration Variables
        blank_list = []

        for _, line in enumerate(in_file):
            # New Object/Data
            new_line = {}
            is_newline = line == '\n'

            if is_newline:
                # Reset Variables
                line_symbol = ""  # Symbol for newline
                new_line_count += 1  # Increase Count
                
                line_count = 0  # Reset consecutive non newline
                
                # if not empty list
                if len(blank_list) > 0:
                    # Create object
                    new_line = assign_line_data(LineType.LIST, blank_list)
                    # Add list to complete data
                    complete_data.append(new_line)
                    
                    # Reset List
                    blank_list = []
            else:
                line_count += 1  # Increase consecutive non newline Count

                # On second non newline char
                if line_count > 1:
                    line_symbol = "L"  # Symbol for LIST
                    # Add line(cleaned) to iterable list that gets reset on newline
                    blank_list.append(line.strip().replace("- ", ""))
                # One preceding newline
                elif new_line_count == 1:
                    line_symbol = "p"  # Symbol for PARAGRAPH
                    # Create and append data
                    new_line = assign_line_data(LineType.PARAGRAPH, line.strip())
                    complete_data.append(new_line)
                # Two preceding newlines
                elif new_line_count == 2:
                    line_symbol = "h"  # Symbol for HEADING
                    # Create new object/data/dict
                    new_line = assign_line_data(LineType.HEADING, line.strip())
                    # Add object to complete data
                    complete_data.append(new_line)
                # Reset New Line Count
                new_line_count = 0
            
            # Debug
            print(f"{_}| <{line_symbol}> {line.strip()}")
            debug_data.append(f"{_}| <{line_symbol}> {line.strip()}")

    return complete_data

# Delete
# def main():
#     with open("data/funnel_cake_fries_recipe.txt", 'r') as in_file:
#         # Defaults 
#         symbol = ""
#         new_line_count = 0
        
#         list_count = 0
        
#         complete_data = []
#         debug_data = []
        
#         raw_data = []
#         blank_list = []

#         for _, line in enumerate(in_file):
#             # New Object/Data
#             new_line = {}
#             is_newline = line == '\n'

#             if is_newline:
#                 symbol = ""
#                 new_line_count += 1
                
#                 # Reset List
#                 list_count = 0
                
#                 # if not empty list
#                 if len(blank_list) > 0:
#                     # Add list to raw data
#                     raw_data.append(blank_list)

#                     # Create object
#                     new_line = assign_line_data("list", blank_list)
                    
#                     # Add list to complete data
#                     complete_data.append(new_line)
                    
#                     # Reset List
#                     blank_list = []
            
#             else:
#                 # Start List Count
#                 list_count += 1

#                 if list_count > 1:
#                     # On second non newline char
#                     symbol = "L"
#                     # Add line(cleaned) to iterable list that gets reset on newline
#                     blank_list.append(line.strip().replace("- ", ""))
#                 elif new_line_count == 1:

#                     symbol = "p"
#                     # Add line to Raw data
#                     raw_data.append(line)
#                     new_line = assign_line_data("paragraph", line.strip())
#                     complete_data.append(new_line)
#                 elif new_line_count == 2:
#                     symbol = "h"
#                     # Add line to Raw data
#                     raw_data.append(line)
#                     # Create new object/data
#                     new_line = assign_line_data("header", line.strip())
#                     # Add object to complete data
#                     complete_data.append(new_line)
#                 # Reset new_line_count to 0
#                 new_line_count = 0
                
#             print(f"{_}| <{symbol}> {line.strip()}")
#             debug_data.append(f"{_}| <{symbol}> {line.strip()}")

#         # print(raw_data)
#         # print(debug_data)
#         # print(complete_data)
#     return complete_data
    

if __name__ == '__main__':
    full_data = recipe_txt_parser("data/funnel_cake_fries_recipe.txt")
    print(full_data)
    
    # Save parsed Data
    with open("test_model_data.json", 'w') as out_json:
        json.dump(full_data, out_json, indent=4)

import os
import time
import requests

import json

from bs4 import BeautifulSoup
from typing import Dict, List

from enum import Enum

from single_page_scraper import scrape_recipe_article, scrape_recipe_card, scrape_recipe_card
from load_save import load_json, load_txt, save_json, save_txt

"""
Future :
    - Create dir of category and save scraped articles there!

Build_url = "https://copykat.com/category/{category}/page/{page_num}"

Scrape categories page of choice for recipes names and links!
    returns a list of dictionaries { name: str, links: str }

Example:
    new_data = get_category_recipe_page("appetizers", 2)
    built_url = "https://copykat.com/category/appetizers/page/2"
"""


class RecipeCategory(Enum):
    FAVORITE: str = "most-favorite"
    FAST_FOOD: str = "copycat-restaurant-recipes"
    CHINESE: str = "chinese-food"
    MEXICAN: str = "mexican-food"
    ITALIAN: str = "italian-recipes"
    DESSERT: str = "dessert"
    APPETIZER: str = "appetizers"

def load_seen_cache(override_filepath: str=None):
    # Set Default Path
    default_filepath = "data/cache/seen_scraped.json"
    
    if override_filepath is not None:
        default_filepath = override_filepath

    # Load Data
    new_seen_data = load_json(default_filepath)
    
    # In Case of error return empty array
    if not new_seen_data:
        new_seen_data = []
    
    return new_seen_data


def get_category_recipe_page(category: str, page_num: int=1) -> List[Dict[str, str]]:
    """  
    Scrape categories page of choice for recipes names and links!

    returns a list of dictionaries { name: str, links: str }
    """
    # Build full url based on page
    base_url = "https://copykat.com/category"
    full_url = f"{base_url}/{category}/page/{page_num}"
    
    # Submit Request
    response = requests.get(full_url)

    # Check Status of Response
    if response.status_code != 200:
        return None

    # Get Soup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all Cards
    results = soup.find_all('a', class_="entry-title-link")

    # Extract Data
    
    new_data = []
    for entry in results:
        new_data.append({
            "name": entry.get_text(),
            "link": entry.get("href")
        })

    # List Comprehension Version
    # new_d = [{ "name": item.get_text(), "link": item.get('href') } for item in results]

    return new_data



def main():
    """  
    Idea behind this is we a list of just the name and links, 
    then when we finally choose a recipe...

    we just load it into a python object for fast 
    reference, and we keep it until we end session. 
    
    same with other recipes, only load them as we 
    need them.
    """

    # Sample Use Case

    # Extract Appetizers, pg. 1
    list_of_data = get_category_recipe_page(RecipeCategory.DESSERT.value) 
    
    # Load already seen
    # already_saved = []
    # with open("saved_recipes.json", 'r') as in_json:
    #     already_saved = json.load(in_json)
    
    already_saved = load_seen_cache()

    # Iterate through data, if name in already seen skip
    for entry in list_of_data:    
        name = entry['name']
        url = entry['link']

        # Skip Condition
        if name in already_saved:
            continue
        
        # Add to saved name list
        already_saved.append(name)

        # Scrape Data
        print(f"{name} - Scraping in progress...")
        time.sleep(5)  # Delay

        new_data = scrape_recipe_article(url)
        
        # Save Data
        # Fix url name to fit filename standards
        fixed_name = url.split("/")[-2].replace("-", "_")
        save_txt(new_data, f"data/articles/{fixed_name}_recipe.txt")
        print(f"{name} - Scraping Done!")

    # Save list of already seen
    with open("data/cache/saved_recipes.json", 'w') as out_json:
        json.dump(already_saved, out_json)

if __name__ == '__main__':
    main()
    # list_of_data = get_category_recipe_page("appetizers")
    # print(len(list_of_data))

    # new_data = load_seen_cache()
    # print(new_data)

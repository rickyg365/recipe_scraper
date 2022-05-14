import os
import time
import requests

import json

from bs4 import BeautifulSoup
from typing import Dict, List

from load_save import load_json, load_txt, save_json, save_txt

"""
base_url = https://copykat.com/
test_url = https://copykat.com/mcdonalds-egg-mcmuffin/

Method #1
    Extracts Data from article into a raw text file 
    - h2: 2 new lines prefix 
    - p: 1 new line prefix
    - list_item: - as first char

Method #2
    Get from Recipe Card at the bottom of page
"""

def get_name_of_files_from_dir():
    return

# Scrape Recipe Article
def scrape_recipe_article(url: str) -> str:
    """ 
    Method #1
        Extracts Data from article into a raw text file 
        - h2: 2 new lines prefix 
        - p: 1 new line prefix
        - list_item: - as first char

    """
    # Submit Request
    response = requests.get(url)

    # Check Status of Response
    if response.status_code != 200:
        return None

    # Get Soup
    soup = BeautifulSoup(response.content, "html.parser")

    # Get main container
    results = soup.find('div', class_="entry-content")

    # Iterate through children and extract article headings, paragraphs and lists
    new_raw_text = f""
    for entry in results.children:
        tag_type = entry.name
        
        # Do something based on tag, ["h2", "p", "ul", "ol"]
        match tag_type:  
            case "h2":
                # Heading
                new_raw_text += f"\n\n\n{entry.text}"
            case "p":
                # Paragraph
                new_raw_text += f"\n\n{entry.text}"
            case "ul" | "ol":
                # List
                fixed_text = entry.find_all("li")
                for each_ele in fixed_text:
                    new_raw_text += f"\n- {each_ele.text}"
                continue
            case _:
                # Every Other Case
                pass
    return new_raw_text



# Scrape Recipe Card
def scrape_recipe_card(url: str) -> Dict[str, any]:
    return


def main():
    # test_url = "https://copykat.com/category/appetizers/"
    # new_data = get_category_recipe_page(test_url)
    # print(new_data)

    # other_url = "https://copykat.com/chick-fil-a-chicken-nuggets/"
    # data = scrape_page_for_recipe(other_url)
    # print(data)


    list_of_data = get_category_recipe_page("appetizers")
    print(len(list_of_data))

    # Load already seen
    """  
    idea behind this is we jsut use this list and when we finally choose a recipe 
    we just load it into a python object for fast reference, and we keep it until 
    we end session. same with other recipes, only load them as we need them, also 
    work on converting from text to json
    """
    already_saved = []
    with open("saved_recipes.json", 'r') as in_json:
        already_saved = json.load(in_json)
    
    for entry in list_of_data:    
        name = entry['name']
        url = entry['link']

        # if name already in list of scraped skip!
        if name in already_saved:
            continue

        already_saved.append(name)

        print(f"{name} - Scraping in progress...")
        time.sleep(5)
        # new_data = scrape_page_for_recipe(url)
        # Save txt
        # fixed_name = url.split("/")[-2].replace("-", "_")
        # save_txt(new_data, f"data/{fixed_name}_recipe.txt")
        print(f"{name} - Scraping Done!")

    # Save list of already seen
    with open("saved_recipes.json", 'w') as out_json:
        json.dump(already_saved, out_json)

if __name__ == '__main__':
    # main()

    url = "https://copykat.com/mcdonalds-egg-mcmuffin/"
    raw_article_data = scrape_recipe_article(url)
    print(raw_article_data)

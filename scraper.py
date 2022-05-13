import os
import time
import requests

import json

from bs4 import BeautifulSoup
from typing import Dict, List

"""
https://copykat.com/

https://copykat.com/#search/q=chick

# Grid Container
id="itemCollection"
div id="Container"

# Card Container
div id="slickTemplateCellContainer"

# Name, Url
<a id="name" href="https://copykat.com/chick-fil-a-chicken-nuggets/">
    <span data-title-html="">
        <mark>Chick</mark> 
        Fil A Chicken Nuggets</span>
</a>


# Likes
<div id="favCount"><!-- ... -->404</div>

# Max 14?


# By category

Page 1
https://copykat.com/category/appetizers/
Page 2
https://copykat.com/category/appetizers/page/2/


<a 
    class="entry-title-link" 
    rel="bookmark" 
    href="https://copykat.com/cheesecake-factory-loaded-baked-potato-tots/">
    Cheesecake Factory Loaded Baked Potato Tots
</a>

"""

def get_category_recipe_page(category: str, page_num: int=1) -> List[Dict[str, str]]:
    """
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
            "link": entry["href"]
        })
    return new_data


def scrape_page_for_recipe(url: str):
    """ 
    Extracts Data into a raw text file, h2 have 2 new lines and p have 1,
    list items have a - before them.

    https://copykat.com/cheesecake-factory-loaded-baked-potato-tots/

    div class="entry-content"


    # Sections we care about
    h2, p, ol, ul, li

    h2 id="h-ingredients"
        > ul
            > li

    h2 id="h-how-to-make-loaded-baked-potato-tots"


    h2 id=""
    h2 id=""
    h2 id=""
    h2 id=""
    
    """
    # Submit Request
    response = requests.get(url)

    # Check Status of Response
    if response.status_code != 200:
        return None

    # Get Soup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all Cards
    results = soup.find('div', class_="entry-content")
    
    # Print Data
    """
    Data we want to Save
    - Complete Raw text
    - Ingredients
    - Instructions

    """
    new_raw_text = f""
    for entry in results.children:
        tag_type = entry.name

        # Check to see if this works
        # match tag_type:  # ["h2", "p", "ul", "ol"]:
        #     case "h2":
        #         new_raw_text += "\n\n"
        #     case "p":
        #         new_raw_text += "\n"
        #     case "ul" | "ol":
        #         fixed_text = entry.find_all("li")
        #         for each_ele in fixed_text:
        #             new_raw_text += f"\n- {each_ele.text}"
        #         continue
        #     case _:
        #         new_raw_text += f"\n{entry.text}"

        if tag_type in ["h2", "p", "ul", "ol"]:
            if tag_type == "h2":
                new_raw_text += "\n\n"
            if tag_type == "p":
                new_raw_text += "\n"
            if tag_type in ["ul", "ol"]:
                fixed_text = entry.find_all("li")
                for each_ele in fixed_text:
                    new_raw_text += f"\n- {each_ele.text}"
                continue
            new_raw_text += f"\n{entry.text}"

    return new_raw_text



def save_txt(data: str, filepath: str):
    with open(filepath, 'w') as out_file:
        out_file.write(data)


def get_name_of_files_from_dir():
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
    t = input("Continue to download? ")
    if t == 'q':
        return

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
    main()

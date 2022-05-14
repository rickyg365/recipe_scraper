# Web Scraper - Site Layout Notes

a small study to get an idea of `copykat.com/` 's layout

# Method #1 - Scrape Page Text

This method extracts data from the article section of the page!

# Method #2 - Scrape Recipe Container

[recipe container]: div.wprm-recipe-template-copykat-cutout-container

This section extracts data from the recipe section at the end of the page, it has more data on the recipe but contains none of the articles paragraphs.

## Header

[header container]: div.wprm-recipe-template-copykat-cutout-header

-   **Name**: _h2.wprm-recipe-name_
-   **Summary**: _div.wprm-recipe-summary_
-   **Rating**: _div#wprm-recipe-user-rating-0_
    -   **_data-average_**, Average Rating, _data attribute_
    -   **_data-count_**, Total Reviews, _data attribute_
    -   **_data-recipe_**, Recipe ID, _data attribute_
-   **Meta_data**: _div.wprm-recipe-meta-container.wprm-recipe-tags-container.wprm-recipe-details-container_
    -   **_Course_**: _div.wprm-recipe-course-container or span.wprm-recipe-course_
    -   **_Cuisine_**: _div.wprm-recipe-cuisine-container or span.wprm-recipe-cuisine_
    -   **_Keyword_**: _div.wprm-recipe-keyword-container or span.wprm-recipe-keyword_
-   **Time**: _div.wprm-recipe-times-container_
    -   **_prep_time_**: _div.wprm-recipe-prep-time-container or span.wprm-recipe-prep_time wprm-recipe-prep_time-minutes_
    -   **_cook_time_**: _div.wprm-recipe-cook-time-container or span.wprm-recipe-cook_time wprm-recipe-cook_time-minutes_
-   **Servings**: _span.wprm-recipe-servings.wprm-recipe-servings-45869_
-   **Calories**: _span.wprm-recipe-nutrition-with-unit_
    -   **_amount_**: _span.wprm-recipe-nutrition.wprm-recipe-calories_
    -   **_unit_**: _span.wprm-recipe-nutrition-unit.wprm-recipe-calories-unit_
-   **Author**: _span.wprm-recipe-author_

## Ingredients

[ingredients container]: div.wprm-recipe-ingredients-container.wprm-recipe-45869-ingredients-container

Can sometimes have multiple groups of Ingredients! so must search for all in parent container

-   **List of Ingredient Groups**: _div.wprm-recipe-ingredient-group_ [^select all]
    [^For Each Group] - **Group_name**: _h4.wprm-recipe-group-name wprm-recipe-ingredient-group-name_ - **Group_data**: _ul.wprm-recipe-ingredients > li.wprm-recipe-ingredient_ [^select all] - **_amount_**: _span.wprm-recipe-ingredient-amount_ - **_unit_**: _span.wprm-recipe-ingredient-unit_ - **_name_**: _span.wprm-recipe-ingredient-name_ - **_notes_**: _span.wprm-recipe-ingredient-notes_, possibly ommited

## Instructions

[instruction container]: div.wprm-recipe-instructions-container.wprm-recipe-45869-instructions-container

Can also sometimes have multiple groups! so must search for all instruction groups inside of parent container.

-   ### **List of Instruction Groups**:
    -   _div.wprm-recipe-instruction-group_ [^select all]
        [^For Each Group] - **Group_name**: _h4.wprm-recipe-group-name wprm-recipe-instruction-group-name_ - **Group_data**: _ul.wprm-recipe-instructions > li.wprm-recipe-instruction_ [^select all] - **_text_**: _div.wprm-recipe-instruction-text > span_ - **_Extra Data_**: id= _wprm-recipe-{recipe_id}-step-{group_num}-{step_num}_ [^0-indexed] - **Example**: **_li#wprm-recipe-24474-step-1-0_** - _recipe_id_: 24474 - _group_num_: 1 - _step_num_: 0

## Notes

[notes container]: div.wprm-recipe-notes-container

-   Doesn't Always have data!

## Nutrition

[nutrition container]: div.wprm-nutrition-label-container.wprm-nutrition-label-container-simple

-   **Calories**: _span.wprm-nutrition-label-text-nutrition-container-calories_
    -   **_Amount_**: _span.wprm-nutrition-label-text-nutrition-value_
    -   **_Unit_**: _span.wprm-nutrition-label-text-nutrition-unit_
-   **Carbohydrates**: _span.wprm-nutrition-label-text-nutrition-container-carbohydrates_
    -   **_Amount_**: _span.wprm-nutrition-label-text-nutrition-value_
    -   **_Unit_**: _span.wprm-nutrition-label-text-nutrition-unit_
-   **Protein**: _span.wprm-nutrition-label-text-nutrition-container-protein_
    -   **_Amount_**: _span_
    -   **_Unit_**: _span_
-   **Fat**: _span.wprm-nutrition-label-text-nutrition-container-fat_
    -   **_Amount_**: _span_
    -   **_Unit_**: _span_
-   **Saturated Fat**: _span.wprm-nutrition-label-text-nutrition-container-saturated_fat_
    -   **_Amount_**: _span_
    -   **_Unit_**: _span_
-   **Cholesterol**: _span.wprm-nutrition-label-text-nutrition-container-cholesterol_
    -   **_Amount_**: _span_
    -   **_Unit_**: _span_
-   **Sodium**: _span.wprm-nutrition-label-text-nutrition-container-sodium_
    -   **_Amount_**: _span_
    -   **_Unit_**: _span_
-   **Potassium**: _span.wprm-nutrition-label-text-nutrition-container-potassium_
    -   **_Amount_**: _span_
    -   **_Unit_**: _span_
-   **Fiber**: _span.wprm-nutrition-label-text-nutrition-container-fiber_
    -   **_Amount_**: _span_
    -   **_Unit_**: _span_
-   **Sugar**: _span.wprm-nutrition-label-text-nutrition-container-sugar_
    -   **_Amount_**: _span_
    -   **_Unit_**: _span_
-   **Vitamin A**: _span.wprm-nutrition-label-text-nutrition-container-vitamin_a_
    -   **_Amount_**: _span_
    -   **_Unit_**: _span_
-   **Vitamin C**: _span.wprm-nutrition-label-text-nutrition-container-vitamin_c_
    -   **_Amount_**: _span_
    -   **_Unit_**: _span_
-   **Calcium**: _span.wprm-nutrition-label-text-nutrition-container-calcium_
    -   **_Amount_**: _span_
    -   **_Unit_**: _span_
-   **Iron**: _span.wprm-nutrition-label-text-nutrition-container-iron_
    -   **_Amount_**: _span_
    -   **_Unit_**: _span_

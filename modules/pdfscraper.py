### PDF Data ###
# region Imports & Data
import pandas as pd
import numpy as np
import PyPDF2

# endregion

# region Data Prep

pdf_obj = open(
    "/Users/spelkofer/Desktop/Desktop/GitHub/BeerClustering/data/MolsonCoors_Nutritional_Information.pdf",
    mode="rb",
)
pdfReader = PyPDF2.PdfFileReader(pdf_obj)

cols = [
    "Brand",
    "Brand_Style",
    "ABV",
    "Calories",
    "Fat_grams",
    "Calories_from_fat",
    "Saturated_fat_grams",
    "Trans_fat_grams",
    "Cholesterol_mg",
    "Sodium_mg",
    "Carbs_mg",
    "Fiber_grams",
    "Sugars_grams",
    "Protein_grams",
    "Ingredients",
]
beer_df = pd.DataFrame(columns=cols)
# Page 1 parsing
page_text = pdfReader.getPage(0).extractText()
page_text_split = page_text.split("\n")[93:]  # excludes junk and columns
del page_text_split[199]  # delete incorrect new line character
new_split = []
pass_list = []
temp_string = ""

for i, v in enumerate(page_text_split):
    try:  # works until last index
        next_val = page_text_split[i + 1]
    except IndexError:
        next_val = ""
    if i in pass_list:
        pass
    else:
        if next_val in [" ", ""]:
            if len(temp_string) == 0:  # only need regular v
                new_split.append(v)
                pass_list.append(i + 1)
            else:  # append to the temp string and use that
                temp_string += str(v)
                new_split.append(temp_string)
                temp_string = ""
                pass_list.append(i + 1)
        else:
            temp_string += v

# Split into chunks of 15
n = 15
list_rows = [
    new_split[i * n : (i + 1) * n] for i in range((len(new_split) + n - 1) // n)
]
del list_rows[9]

# Append each chunk to the dataframe
for row in list_rows:
    row_df = pd.DataFrame([row], columns=beer_df.columns.to_list())
    beer_df = beer_df.append(row_df, ignore_index=True)

# Page 2+ parsing
n = 24
for i in range(n, n + 1):
    page_text = pdfReader.getPage(i).extractText()
    page_text_split = page_text.split("\n")[59:]  # excludes junk and columns

    new_split = []
    pass_list = []
    temp_string = ""

    for i, v in enumerate(page_text_split):
        try:  # works until last index
            next_val = page_text_split[i + 1]
        except IndexError:
            next_val = ""
        if i in pass_list:
            pass
        else:
            if next_val in [" ", ""]:
                if len(temp_string) == 0:  # only need regular v
                    new_split.append(v)
                    pass_list.append(i + 1)
                else:  # append to the temp string and use that
                    temp_string += str(v)
                    new_split.append(temp_string)
                    temp_string = ""
                    pass_list.append(i + 1)
            else:
                temp_string += v

    # Split into chunks of 15
    n = 15
    list_rows = [
        new_split[i * n : (i + 1) * n] for i in range((len(new_split) + n - 1) // n)
    ]

    del list_rows[-1]

# Append each chunk to the dataframe
for row in list_rows:
    row_df = pd.DataFrame([row], columns=beer_df.columns.to_list())
    beer_df = beer_df.append(row_df, ignore_index=True)


# endregion

# region Export
beer_df.to_csv("BeerIngredients_draft.csv", index=False)
# endregion

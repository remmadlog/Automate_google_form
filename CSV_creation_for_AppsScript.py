"""
This file is used to create the raw csv for the survey
The look of the survey
- description part
- - is done by hand in the form -- was not doing what I wanted
- - that's fine, the main idea is so automates the reoccurring parts
- page where you enter your name
- one page per shows/anime_id
- - title with link to MAL
- - image of the show
- - Rating 0 to 10
- - Collage image
- - - MUST be added BY HAND
- - - - I have no idea how to tell the api to take my files or the files in my drive
- - Favorites characters
- - - wanted to add image url here fore each character name but the api does not support add.image for checkbox item
- - - - https://issuetracker.google.com/issues/135828271
- - - - https://issuetracker.google.com/issues/36765518
- - - Therefore the collage with the names

we use an apps script to go from Google sheets to Google forms
The API documentation is here
- https://developers.google.com/apps-script/reference/forms
"""

import csv
from Methods import *

# id we use
Anime_IDs = ["54724","55791","57181","41392"]


# head
# first page with your information
CSV = [
    ["Question", "Image", "Type", "Required", "Description", "Answer", "CharImage"],
    ["Your Information", "", "SECTION", "", "Please enter your name."],
    ["Name:", "", "TEXT", "Yes"]
]

# next pages
# # one page per entry/id
# # # as described above
for anime_id  in Anime_IDs:
    with open("data_json/" + anime_id + "_AnimeData" + '.json',
              encoding="utf8") as f:
        data_anime = json.load(f)
    with open("data_json/" + anime_id + "_CharacterData" + '.json',
              encoding="utf8") as f:
        data_character = json.load(f)

    # ge the anime name - no need to remove odd symbols
    try:
        anime_name = data_anime["data"]["title_english"]
        if not anime_name:
            anime_name = data_anime["data"]["title"]
    except:
        anime_name = data_anime["data"]["title_japanese"]
    anime_image_url = data_anime["data"]["images"]["jpg"]["image_url"]


    # new section: Anime Title + MAl Link | Anime Image | Rating
    CSV.append([anime_name, "","SECTION", "", "https://myanimelist.net/anime/"+ anime_id] )
    CSV.append([anime_name, anime_image_url,"IMAGE" ] )
    CSV.append(["Rating:", "", "SCALE", "Yes", "0 = Not Seen"])


    # get character names and image urls | create two lists
    # # we take the images url in case the api changes at one point
    # # atm this is redundant
    anime_character_name_image = get_anime_char(data_character)
    character_name = anime_character_name_image[0]
    # atm no need for this
    character_image_url = anime_character_name_image[1]

    # create the rows for fav and hated characters
    # # Title, "", type, required, description, "question"
    Fav_Char = ["Favorite Character", "", "CHECKBOX", "", "Pick 3 (No Order)", "|".join(character_name), "|".join(character_image_url)]
    Hated_Char = ["Hated Character", "", "CHECKBOX", "", "Pick 3 (No Order)", "|".join(character_name), "|".join(character_image_url)]


    CSV.append(Fav_Char)
    CSV.append(Hated_Char)

    # add a text field so if a character is missing, a person can add them here
    CSV.append(["Additional Remarks:", "", "TEXT", "", "Missing favorite or hated character or other important remarks go here. Please use the full name similar to above."])


# save the csv
with open("Anime_Survey_for_sheets.csv", "w", newline='') as file:
    csv_writer = csv.writer(file, delimiter=';')
    csv_writer.writerows(CSV)
"""
Main collection of methods!
This "project" is a cleaner version of a things I have done a few week ago.
The Problem:
    Creating a survey using google forms for questions with a returning pattern.
    Here on the example of anime rating and picking favorite/hated characters
    Done for shows that are usually not older than 1 year (some are though)
The solution:
    Automatisation!
    get the data from MAL -- for more details consider my MAL_Data_ESA project
    prepare the data
    create a CSV
    CSV to google sheets (by hand)
    google sheets to google forms (using apps script)
"""

import requests
import time
import shutil
from pathlib import Path
import json



"""
function to get the most favorite characters from the MLA dataset
- get most favored (like they were important so good for favorites and hated in survey) 
- no more than 20 characters
- at least 10
- get the names and the image url
- return([character_name,character_image_url])
"""
def get_anime_char(data_character):
    character_name = []
    character_image_url = []


    # Count the amount of favorite characters with <4, =4, =3, =2, =1
    # the general number of favorites for characters is not so high.
    # Considering older (more than 1 year ago) and very popular shows, this might change
    count_4 = 0
    count_3 = 0
    count_2 = 0
    count_1 = 0
    count = 0
    # count the amount of characters with more >4,=4,... favorites
    for CHAR in data_character["data"]:
        if CHAR["favorites"] > 4:
            count = count + 1
        if CHAR["favorites"] == 4:
            count_4 = count_4 + 1
        if CHAR["favorites"] == 3:
            count_3 = count_3 + 1
        if CHAR["favorites"] == 2:
            count_2 = count_2 + 1
        if CHAR["favorites"] == 1:
            count_1 = count_1 + 1


    Char_limit = 0  # going for less than 20

    # check how many characters we are going to consider
    if count >= 10:
        number_of_faves = 5
    elif count + count_4 >= 10:
        number_of_faves = 4
    elif count + count_4 + count_3 >=10:
        number_of_faves = 3
    elif count + count_4 + count_3 + count_2 >=10:
        number_of_faves = 2
    elif count + count_4 + count_3 + count_2 + count_1 >=10:
        number_of_faves = 1
    else:
        number_of_faves = 0
        Char_limit = 10

    # bias for the order of characters // should resolve: char_fave = 3 is added but char_fave = 50 isn't due to order in source
    # # picking them in order of favorite amount
    # # still a problem if more than 20 characters have more than 5 favs
    # # # usually not a problem
    # # # we do not want to add more than 20, therefore we will let it be
    # Adding characters (names,img_url) based on favorite amount
    for CHAR in data_character["data"]:
        if number_of_faves <= 5:
            if CHAR["favorites"] >= 5:
                Char_limit = Char_limit + 1
                character_name.append(CHAR["character"]["name"])
                character_image_url.append(CHAR["character"]["images"]["jpg"]["image_url"])
                if Char_limit == 20:
                    break
    for CHAR in data_character["data"]:
        if Char_limit == 20:
            break
        if number_of_faves <= 4:
            if CHAR["favorites"] == 4:
                Char_limit = Char_limit + 1
                character_name.append(CHAR["character"]["name"])
                character_image_url.append(CHAR["character"]["images"]["jpg"]["image_url"])
    for CHAR in data_character["data"]:
        if Char_limit == 20:
            break
        if number_of_faves <= 3:
            if CHAR["favorites"] == 3:
                Char_limit = Char_limit + 1
                character_name.append(CHAR["character"]["name"])
                character_image_url.append(CHAR["character"]["images"]["jpg"]["image_url"])
    for CHAR in data_character["data"]:
        if Char_limit == 20:
            break
        if number_of_faves <= 2:
            if CHAR["favorites"] == 2:
                Char_limit = Char_limit + 1
                character_name.append(CHAR["character"]["name"])
                character_image_url.append(CHAR["character"]["images"]["jpg"]["image_url"])
    for CHAR in data_character["data"]:
        if Char_limit == 20:
            break
        if number_of_faves <= 1:
            if CHAR["favorites"] == 1:
                Char_limit = Char_limit + 1
                character_name.append(CHAR["character"]["name"])
                character_image_url.append(CHAR["character"]["images"]["jpg"]["image_url"])
    for CHAR in data_character["data"]:
        if Char_limit == 20:
            break
        if number_of_faves == 0:
            if CHAR["favorites"] == 0:
                Char_limit = Char_limit + 1
                character_name.append(CHAR["character"]["name"])
                character_image_url.append(CHAR["character"]["images"]["jpg"]["image_url"])
    return([character_name,character_image_url])




"""
Function to downloading the images corresponding to the character list
- creates a folder
- saves images named 1-20(at most)
- order is character name order by popularity
"""
def download_images(url_list, anime_name):
    count = 0

    # bad symbols for paths and names "<", ">", ":", '"', "/", "\\", "|", "?", "*"
    # # remove them
    for sym in ["<", ">", ":", '"', "/", "\\", "|", "?", "*"]:
        anime_name = anime_name.replace(sym,  "")

    for url in url_list:
        count = count + 1
        # we could use my request(download) checks done in MAL_Data_ESA but this works fine and is ment for a smaller amount of requests
        res = requests.get(url, stream=True, timeout=10)

        if res.status_code == 200:
            Path("Images/by_number/" + anime_name).mkdir(parents=True, exist_ok=True)
            with open("Images/by_number/" + anime_name + "/" + str(count) + ".jpg",
                      'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded:')
        else:
            print('Image Could not be retrieved')
            print(count, url)
        time.sleep(1)
    return()

"""
Function to downloading the images corresponding to the character list -- image name is based on character name
- creates a folder
- saves images named by the character representing
"""
def download_images_named(url_list, char_name, anime_name):
    count = 0
    i = 0

    # bad symbols for paths and names "<", ">", ":", '"', "/", "\\", "|", "?", "*"
    # # remove them
    for sym in ["<", ">", ":", '"', "/", "\\", "|", "?", "*"]:
        anime_name = anime_name.replace(sym,  "")

    for url in url_list:
        count = count + 1
        # we could use my request(download) checks done in MAL_Data_ESA but this works fine and is ment for a smaller amount of requests
        res = requests.get(url, stream=True, timeout=10)

        if res.status_code == 200:

            Path("Images/by_name/" + anime_name).mkdir(parents=True, exist_ok=True)
            with open("Images/by_name/" + anime_name + "/" + char_name[i] + ".jpg",
                      'wb') as f:
                shutil.copyfileobj(res.raw, f)
            i += 1
            print('Image sucessfully Downloaded:',char_name[i])
        else:
            print('Image Could not be downloaded:', char_name[i])
            print(count)

        time.sleep(1)
    return()


"""
We want to keep this here very very simple, therefore the download function below is very rough 
and not prepared for every little hiccup that could occur
- do not use if
- - you want to download a large number 30+ (see MAL_Data_ESL for this purpose)
- No safeguarding 
- No nothing just a lot of trust
!!! use the supply_module in MAL_Data_ESL if troubles occur 
"""
def download_json(anime_id):
    # get anime main data
    url_anime = "https://api.jikan.moe/v4/anime/" + str(anime_id)
    response = requests.get(url_anime, timeout=10)
    data_anime = response.json()

    time.sleep(2)

    # get anime character data
    url_char = "https://api.jikan.moe/v4/anime/" + str(anime_id) + "/characters"
    response = requests.get(url_char, timeout=10)
    data_character = response.json()


    # save everything
    Path("data_json").mkdir(parents=True, exist_ok=True)
    with open("data_json/" + anime_id + "_AnimeData" + '.json', 'w', encoding='utf-8') as f:
        json.dump(data_anime, f, ensure_ascii=False, indent=4)

    with open("data_json/" + anime_id + "_CharacterData" + '.json', 'w', encoding='utf-8') as f:
        json.dump(data_character, f, ensure_ascii=False, indent=4)

    time.sleep(2)

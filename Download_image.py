"""
Here we download the images named after the characters
- at most 20
- depending on the amount of favorites
- instead of anime_name, the folder is named after anime_id
- - Images/by_name/[anime_id] contains images
"""

from Methods import *

# list of IDs
Anime_IDs = ["54724","55791","57181","41392"]


for anime_id in Anime_IDs:
    # to see where we are -- can be removed if not wanted
    print("woring on:",anime_id)

    """Can be used if you want to save the images in a folder named by the anime name -- then changed in Image_collage files needed"""
    # # to get the anime name
    # with open("data_json/" + anime_id + "_AnimeData" + '.json',
    #           encoding="utf8") as f:
    #     data_anime = json.load(f)
    # try:
    #     anime_name = data_anime["data"]["title_english"]
    #     if not anime_name:
    #         anime_name = data_anime["data"]["title"]
    # except:
    #     anime_name = data_anime["data"]["title_japanese"]
    # # bad symbols for paths and names "<", ">", ":", '"', "/", "\\", "|", "?", "*"
    # # # remove them
    # for sym in ["<", ">", ":", '"', "/", "\\", "|", "?", "*"]:
    #     anime_name = anime_name.replace(sym,  "")


    #open the character dataset
    with open("data_json/" + anime_id + "_CharacterData" + '.json', encoding="utf8") as f:
        data_character = json.load(f)

        # get character names and image urls
        [char_names_list,character_image_url] = get_anime_char(data_character)
        # downloading images and saving them named after the character
        # # anime_id used instead of anime_name -- it is unique so why bother
        download_images_named(character_image_url, char_names_list, anime_id)
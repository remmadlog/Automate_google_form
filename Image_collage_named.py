"""
This is used to create a collage of the images provided
- images are glued to a collage
- names are added to the collage
- final image is saved
Remarks
- font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 30)
- - if this makes problems consider a different font
"""
from PIL import Image, ImageDraw, ImageFont
import os, os.path
import math
from Methods import *


Anime_IDs = ["54724","55791","57181","41392"]

# for each id we are creating a collage
for anime_id in Anime_IDs:
    # pathe for images
    path = 'Images/by_name/' + str(anime_id)

    name_list =[]
    name_list_short = []

    # we need names so get the names
    with open("data_json/" + str(anime_id) + "_CharacterData" + '.json', encoding="utf8") as f:
        data_character = json.load(f)
    [char_names_list, character_image_url] = get_anime_char(data_character)

    # get the amount of images so we know how many rows we have
    # # one row will have 5 columns
    img_count = 0
    for name in os.listdir(path):
        if "jpg" in name: # and [NAME] not in name-- used for nare nare and Dan Da Dan (no image available ior image way to small)
            img_count = img_count + 1
            # we get problems when using the FULL name, so we reduce that and only use the first name
            name_list_short.append(name.split(",")[-1].split(".")[0])
            name_list.append(name)
    # one row will have 5 columns
    rows = math.ceil(img_count/5)


    #collage size
    # # 225*5 = 1275 x
    # # 350*1= 350      350*2= 700      350*3= 1050      350*4= 1400
    # you might have to change the font if you get problems
    font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 30)
    collage = Image.new("RGBA", (1275, 350 * rows))
    for i in range(0,img_count):
        img = Image.open(path + "/" + name_list[i])
        img.thumbnail((225, 350))

        # ad name as text
        draw = ImageDraw.Draw(img)
        # where goes the text
        position = (0,320)
        # what text
        text = name_list_short[i]
        # for BG: white box
        bbox = draw.textbbox(position, text, font=font)
        left, top, right, bottom = draw.textbbox(position, text, font=font)
        draw.rectangle((left - 5, top - 5, right + 5, bottom + 5), fill="white")
        # worte text in black
        draw.text(position, text, font=font, fill="black")

        # gluing
        collage.paste(img, (i%5 * 225,math.floor(i/5) * 350))



    # to get the anime name
    with open("data_json/" + anime_id + "_AnimeData" + '.json',
              encoding="utf8") as f:
        data_anime = json.load(f)

    try:
        anime_name = data_anime["data"]["title_english"]
        if not anime_name:
            anime_name = data_anime["data"]["title"]
    except:
        anime_name = data_anime["data"]["title_japanese"]

    # bad symbols for paths and names "<", ">", ":", '"', "/", "\\", "|", "?", "*"
    # # remove them
    for sym in ["<", ">", ":", '"', "/", "\\", "|", "?", "*"]:
        anime_name = anime_name.replace(sym,  "")

    # saving at
    save_path = 'collage_by_name/'
    # make sure location exists
    Path(save_path).mkdir(parents=True, exist_ok=True)
    # saving
    collage.save(save_path + anime_name + ".png")

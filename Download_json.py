"""
Here we download the jason filed needed
"""
from Methods import *

Anime_IDs = ["54724","55791","57181","41392"]
for anime_id in Anime_IDs:
    # to see where we are
    print(anime_id)
    download_json(anime_id)
# Automated G-form creation via G-sheets and Apps Script
This project is a cleaned version of an older attempt to create a Google form mostly autonom.
The essence of the project is [AppsScript.txt](AppsScript.txt). 
This file allows us to use a Google sheet to prepare data and execute it to obtain a 90% done Google form.

**This repository serves as a learning-by-doing project**


## Content
- [AppsScript.txt](AppsScript.txt) -- the apps script code (**this is the main file, the rest ist for the example**)
- example
- - file provided 
- - - [CSV_creation_for_AppsScript.py](CSV_creation_for_AppsScript.py) -- creating a cvs containing necessary information
- - - [Download_image.py](Download_image.py) -- use to download character images
- - - [Download_json.py](Download_json.py) -- use to download anime main dataset as well as the anime character data set
- - - [Image_collage_named.py](Image_collage_named.py) -- used to create a collage of the images obtained
- - - [Methods.py](Methods.py) -- several functions needed
- - tools uses
- - - working with json
- - - handling requests
- - - using Image, ImageDraw, ImageFont from PIL to create a collage
- - - Google sheets/forms as well as Google Apps Script (java based afaik)
- - - obtaining data from [MyAnimeList (MAL)](https://myanimelist.net/) using the [Jikan API](https://jikan.moe/#)

## Remarks
- the written code does not aim to be perfect, I try my best to keep it coherent, but I am still learning
- I haven't automated everything
- - form titel and description 
- - importing data to Google sheets
- - adding certain items to the form
- - - in the example given below: Collage images, because they are saved locally
- - - - there should be a way to do it either way, but I went for an 80/20 approach to save time

## Problem
- creating a Google form with a high amount of repetition
- reduce tasks that need to be done by hand
- - mostly focusing on repetitive tasks

## Solution
- creating a Google sheet document with needed information for the survey
- execute a Google apss script to create the form
- do necessary adjustments by hand
- - e.g. the title and description

# Example (proof of concept)
- create a survey to see how certain anime performed and what are liked and hated characters
- preparations
- - get the data
- - get images
- - create a file (csv) that can be easily imported in Google sheets
- - - one can probably automate that too, but I followed the 80/20 rule to not wast time on things one can do very fast by hand
- - use apps script to transfer information from Google sheets to Google forms

## How to use
1. get the mal_id of the shows you are interested in
2. add that list of IDs to Download_json.py, Download_image.py, Image_collage_named.py and CSV_creation_for_AppsScript.py
3. execute Download_json.py
4. execute Download_image.py
5. execute Image_collage_named.py (if you want a collage)
6. execute CSV_creation_for_AppsScript.py
7. open your Google sheet
   - copy the csv data to the sheet
   - go to "data"; "text to columns"; chose ";"
   - click on "add-on", "apps scrip"
   - copy AppsScript.txt to the empty (empty the file first) Code.gs file
   - follow instruction in file
   - execute the code (you may need to allow some accesses)
8. final touch es
   - add a tile and a description to cour Google form
   - add the collage images to the form

## Result
[Survey](https://docs.google.com/forms/d/e/1FAIpQLSeExq3nU0m4p4aGHf6eEXkSDqrFkUHnSmHlWwyYcnLKnW8rsQ/viewform?usp=dialog)
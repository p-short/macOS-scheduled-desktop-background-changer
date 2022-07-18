#this code originally imported the schedule and time modules to run code a set intervals however I got mixed results with this over longer time durations so I abandoned this approach, instead I made use of crontabs on my OS to run this script once a day.

#import relevant modules
import os
import pathlib
import random
import subprocess

#variable to hold paths to wallpaper backgrounds
WALLPAPPER_DIR = '/Users/phillipshort/Desktop/python/wallpaper_changer/wallpapers'

#variable that stores apple script code to select wallpaper file
SET_WALLPAPER_OSASCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "{}"
end tell
END"""
    
#function to select image and provide full file path
def change_wallpaper():
    #select a wallpaper at random from the wallpaper directory
    rand_wallpaper = random.choice(os.listdir(WALLPAPPER_DIR))
    #variable to hold weather file starts with a '.' or not, used to detect the randomly selected file is a hidden file or not
    hidden_file = rand_wallpaper.startswith('.')
    #check and proceed if file isnt hidden
    if hidden_file == False:
        #if so print create absolute path to file for apple script code
        full_image_path = os.path.join(
            pathlib.Path().absolute(), WALLPAPPER_DIR, rand_wallpaper
        )
        #pass full image path to subprocess so apple script code is formated and executed
        subprocess.Popen(SET_WALLPAPER_OSASCRIPT.format(full_image_path), shell=True)
    
#run change_wallpaper function
if __name__ == '__main__':
    change_wallpaper()

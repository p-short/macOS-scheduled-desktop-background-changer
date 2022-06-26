#import relevant modules
import time
import schedule
import os
import pathlib
import random
import subprocess

#variable to hold folder name, change this to the name of your local folder containing wallpaper backgrounds
WALLPAPPER_DIR = 'wallpapers'

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
    #check that file name is valid
    if (rand_wallpaper != '.DS_Store'):
        #if so print change to terminal & create absolute path to file for apple script code
        print(f"changing desktop wallpaper to: {rand_wallpaper}")
        full_image_path = os.path.join(
            pathlib.Path().absolute(), WALLPAPPER_DIR, rand_wallpaper
        )
        #pass full image path to subprocess so apple script code is formated and executed
        subprocess.Popen(SET_WALLPAPER_OSASCRIPT.format(full_image_path), shell=True)
    
#function go is called every x unit of time using the schedule module
def go():
    #call the change_wallpaper function ever 7 seconds
    schedule.every(7).seconds.do(change_wallpaper)
    #while script is running check if an event is pending, then sleep for 1 second
    while True:
        schedule.run_pending()
        time.sleep(1)

#once file is run call go function
if __name__ == '__main__':
    go()

import os
import time     
import shutil
import ctypes
import config
import urllib.request
from unsplash_search import UnsplashSearch


accessKey = config.apiKey

try:
    unsplash = UnsplashSearch(accessKey)
except:
    print("Unable to verify access key")

print("*"*30)
print("Enter d for a default wallpaper")
print("*"*30)
category = input("Hallo Samadhana, what are we feeling today?\n")

if category == "d":
    category = "wallpapers"

#Return random image
result = unsplash.search_photo(category)
print(result)
imageURL = result["img"]  
owner = result["credits"]
print(type(owner))


dirPath = config.dirPath
fileName = owner + ".jpg"
imgPath = os.path.join(dirPath, fileName)

#Download image and set as background  
r = urllib.request.urlretrieve(imageURL, fileName)
ctypes.windll.user32.SystemParametersInfoW(20, 0, imgPath, 0)
time.sleep(0.5)


delete = input("Do you want to save this image? y/n\n")
if delete == "n": 
    os.remove(fileName)
else: 
    savedPath = os.path.join(dirPath, "savedImages")
    os.rename(imgPath, os.path.join(savedPath, fileName))
    shutil.move(imgPath, savedPath)
    os.replace(imgPath, os.path.join(savedPath, fileName))


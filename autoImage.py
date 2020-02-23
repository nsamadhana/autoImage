import os
import ctypes
import urllib.request
from unsplash_search import UnsplashSearch
import time     

accessKey = "o7QajBCO4rG2PcSDCnC8-Q6VZokvDUDY2sb8-bvAcOI"

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


filePath = r"C:\Users\nevan\Documents\pythonProjects\autoImage"
fileName = owner + ".jpg"

#Download image and set as background  
r = urllib.request.urlretrieve(imageURL, fileName)
ctypes.windll.user32.SystemParametersInfoW(20, 0, filePath, 0)
time.sleep(2)

delete = input("Do you want to save this image? y/n\n")
if delete == "y": 
    os.remove(fileName)
else: 
    os.rename(filePath + + fileName, filePath + "savedImages"  + fileName)
    shutil.move(filePath + fileName, filePath + "savedImages")
    os.replace(filePath + fileName, filePath + "savedImages"  + fileName)

print("All done")

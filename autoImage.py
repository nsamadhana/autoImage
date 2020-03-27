import os
import time     
import shutil
import ctypes
import config
import urllib.request
from PIL import Image
from unsplash_search import UnsplashSearch

def queryImage(category):
    result = unsplash.search_photo(category) 
    details = []
    details.append(result["img"]) #imageURL (0)
    details.append(result["credits"]) #owner (1)
    details.append(config.dirPath) #directory path (2) 
    details.append(details[1] + ".jpg") #file name (3)
    details.append(os.path.join(details[2], details[3])) #img path (4)
    return details 


try:
    unsplash = UnsplashSearch(config.apiKey)
except:
    print("Unable to verify access key")

print("*"*30)
print("Enter 'd' for a default wallpaper")
print("*"*30)
category = input("Hallo Samadhana, what are we feeling today?\n")

if category == "d": category = "Wallpapers"
#result = unsplash.search_photo(category)
'''
imageURL = result["img"]  
owner = result["credits"]
dirPath = config.dirPath
fileName = owner + ".jpg"
imgPath = os.path.join(dirPath, fileName)
'''

details = queryImage(category)
imageURL = details[0] 
owner = details[1]
dirPath = details[2]
fileName = details[3]
imgPath = details[4]

#Display sample images 
urllib.request.urlretrieve(imageURL, fileName)
img = Image.open(imgPath)
img.show()

#Find suitable image 
keep = input("keep?").lower()
img.close()
while keep != "y":
    os.remove(fileName)
    details = queryImage(category)
    imageURL = details[0] 
    owner = details[1]
    dirPath = details[2]
    fileName = details[3]
    imgPath = details[4]
    urllib.request.urlretrieve(imageURL, fileName)
    img = Image.open(imgPath)
    img.show()
    keep = input("keep?").lower()
    img.close()

#Download image locally/Set as background 
urllib.request.urlretrieve(imageURL, fileName)
ctypes.windll.user32.SystemParametersInfoW(20, 0, imgPath, 0)

save = input("Do you want to save this image?").lower()
if save == "y":
    savedPath = os.path.join(dirPath, "savedImages")
    os.rename(imgPath, os.path.join(savedPath, fileName))
    shutil.move(imgPath, savedPath)
    os.replace(imgPath, os.path.join(savedPath, fileName))
else:
    print("bye bye")


'''
if keep == "y":
    img.close() 
    urllib.request.urlretrieve(imageURL, fileName)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, imgPath, 0)
else:  
    img.close()
    os.remove(fileName)

delete = input("Do you want to save this image? y/n\n")
if delete == "n": 
    os.remove(fileName)
else: 
    savedPath = os.path.join(dirPath, "savedImages")
    os.rename(imgPath, os.path.join(savedPath, fileName))
    shutil.move(imgPath, savedPath)
    os.replace(imgPath, os.path.join(savedPath, fileName))
'''


'''
#Download image/set as background    
r = urllib.request.urlretrieve(imageURL, fileName)
ctypes.windll.user32.SystemParametersInfoW(20, 0, imgPath, 0)
time.sleep(0.5)
'''

    
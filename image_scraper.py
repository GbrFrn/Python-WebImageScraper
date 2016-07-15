#Added support to filter by class name of html element
#Added destination folder support
#Updated code to work with urllib.request

from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request


def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "html.parser")

def get_images(url):
    soup = make_soup(url)
    #this makes a list of bs4 element tags
    images = [img for img in soup.findAll("type of html element", {"class":"name of the class"})]
    print (str(len(images)) + "images found")
    print ('Downloading images to directory')
    #compile our unicode list of image links
    image_links = [each.get('src') for each in images]
    for each in image_links:
        filename=each.split('/')[-1]
        urllib.request.urlretrieve(each, filename)
    return image_links


#Warning!! If your Path contains "\U" such as \Users it will not work properly
#To solve this you must double all the \ so that it looks like \\Users
#Do not put this .py file in a location(folder) where are other images from the format you choose
#The program will automatically transfer all the images on the folder of its location to the folder you chose
#Use with caution

entry = input("Paste the site URL:")

get_images(entry)

import os
import shutil
sourcepath="The path where this .py is located at"
source = os.listdir(sourcepath)

folder = input("Paste your desired custom path:")

destinationpath = folder
for files in source:
    if files.endswith('.jpg'):
        shutil.move(os.path.join(sourcepath,files), os.path.join(destinationpath,files))


k=input("Finished! Press any key to exit.")


#a standard call looks like this
#get_images('http://www.wookmark.com')

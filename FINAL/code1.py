#to search the web for the recipes of a particular dish, aa folder is send that contains text files with dishes names and inside this text file are 10 links where we can find the recipe of the dish







import string
import pandas as pd
from googlesearch import search
import os
import time

from bs4 import BeautifulSoup
import requests
import html2text

import shutil

#function for webscrapping
def WebScrapping(url):
    ## Data extraction in the text format
    try:
        r2 = requests.get(url).text
        h = html2text.HTML2Text()
    
        # Ignore converting links from HTML
        h.ignore_links = True
        h.ignore_images = True
        
        result = h.handle(r2)
        return(result)

    except:
        return("Not able to load HTML")

#function for getting a file for each link with entire HTML contents
def Get_HTML(c,link):

    c = str(c)

    f=open(c+".txt","x")     #creating files with link no.
    f.close()

    f=open(c+".txt","a")     
    f.write(link+"\n\n\n")      #writing link in the first line

    #extracting
    # html_content = requests.get(link).content
    # soup = BeautifulSoup(html_content, 'html.parser')    # Parsing the html content
    # f.write(soup.prettify())      

    f.write(WebScrapping(link))      
    f.close()


#to read all the links in the given file
def read_text_file(parent,file_path):

    parent = os.path.join(parent, "RECIPE")
    try:
        os.mkdir(parent)    #to overcome error due to already existing folder
    except:
        "" 

    c = 1

    with open(file_path, 'r') as f:
        new_list = f.read().split("\n")     #converting the links into a list

    # print(new_list) 

    path = os.path.splitext(file_path)[0]   #getting file name without txt to create folder
    try:
        os.mkdir(path)      #making a directory with dish name
        os.chdir(path)      #going inside directory with dish name
    except:
        return

    for link in new_list:
        if link == "":        #to control the end of list
            break
        Get_HTML(c,link)
        c = c+1                 #keeping count of link number

    shutil.move(path,parent)    #moving the new dish folder into the /FINAL/RECIPE folder


#to read .txt files from the CHINESE FOLDER
def read_file(str):

    parent = "/Users/raisaghosh/Desktop/PRAXIS INTERNSHIP/8 WEEKS/WEEK 3/FINAL"
    path = os.path.join(parent,str)
    os.chdir(path)
    c=0

    for file in os.listdir():
    # Check whether file is in text format or not
        if file.endswith(".txt"):
            if(c<20):
                file_path = f"{path}/{file}"
                c = c+1
                # call read text file function
                read_text_file(parent,file_path)
            else:
                time.sleep(1000)
                print("slept for 1000 s")
                c=0


#calling function for CHINESE folder
read_file("CHINESE")

#to extract menu items from .xlsx





import pandas as pd
from googlesearch import search
import os
import time

def Get_URL(dish, n=10, stop=10):
    f=open(dish+".txt","x")     #creating files with dish name
    f.close()
    f=open(dish+".txt","a")     #writing in the created file in append mode
    query = dish + ' recipe +"ingredients" -youtube'
    for i in search(query, tld = 'co.in', num = n, stop = stop, pause = 3):
        f.write(i+"\n")         #separating each link by a "\n"
    f.close()

def read_file(str,excel_file):

    parent_dir = "/Users/raisaghosh/Desktop/PRAXIS INTERNSHIP/8 WEEKS/WEEK 3/FINAL"
    path = os.path.join(parent_dir, str)
    # os.mkdir(path)      #making a directory with cuisine's name

    #create folder for each cuisine
    df = pd.read_excel(excel_file)          #reading the excel file

    #add validation in case menu column doesn't exist
    new_list = df["Menu"].tolist()          #converting excel file to list
    print(new_list) 

    os.chdir(path)     #going inside the newly created directory

    c=0
    
    for i in new_list:                      #traversing through the created list and creating a file and storing links for each item
        Get_URL(i)
        if(c == 40):
            time.sleep(100000)
            c=0
        c = c+1


excel_file = "chinese.xlsx"     


read_file("CHINESE",excel_file)
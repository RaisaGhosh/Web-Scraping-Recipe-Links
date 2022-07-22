import pandas as pd
from googlesearch import search


def Get_URL(dish, n=10, stop=10):
    f=open(dish+".txt","x")     #creating files with dish name
    f.close()
    f=open(dish+".txt","a")     #writing in the created file in append mode
    query = dish + ' recipe +"ingredients" -youtube'
    for i in search(query, tld = 'co.in', num = n, stop = stop, pause = 60):
        f.write(i+"\n")         #separating each link by a "\n"
    f.close()

excel_file = "bengali.xlsx"     
df = pd.read_excel(excel_file)          #reading the excel file
new_list = df["Menu"].tolist()          #converting excel file to list
print(new_list)                         
for i in new_list:                      #traversing through the created list and creating a file and storing links for each item
    Get_URL(i)
from cgitb import html
from bs4 import BeautifulSoup
import requests
import pandas as pd

#http://www.ssn.unam.mx/sismicidad/ultimos/

#Downloading contents from webpage :) 
data = requests.get('http://www.ssn.unam.mx/sismicidad/ultimos/').text
#Creating BeautifulSoupObject
soup = BeautifulSoup(data, 'lxml')

'''
#Veryfing tables and their clasess
print('Classes of each table')
for table in soup.find_all('table'):
    print(table.get('class'))
'''
'''
def main(soup):
    #Storing table in variable
    earthquake_table = soup.find('table', class_ = 'table-condensed')

    #Creating a list to store headers
    headers=[]

    #Iterating over earthquake_table to find all the headers 
    for i in earthquake_table.find_all('th'):
        title = i.text.strip()
        headers.append(title)
    print(headers)

    #Creating data frame where the headers are assigned as columns
    df = pd.DataFrame(columns = headers)
    print(df)

    for row in earthquake_table.find_all('tr')[1:]:
        data = row.find_all('td')
        row_data = [td.text.strip() for td in data]
        length = len(df)
        df.loc[length] = row_data
        print(df)

    return df.to_csv('terremoto.csv', encoding='utf-8')
'''

#Creating the data frame
def create_data_frame(soup,headers):
    earthquake_table = soup.find('table', class_ = 'table-condensed')
    #Creating listo for headers
    headers=[]
    
    #Iterating over earthquake_table to find all the headers
    for i in earthquake_table.find_all('th'):
        title = i.text.strip()
        headers.append(title)

    #Creating data frame where the headers are assigned as columns
    df = pd.DataFrame(columns = headers)
    print(df)

    for row in earthquake_table.find_all('tr')[1:]:
        data = row.find_all('td')
        row_data = [td.text.strip() for td in data]
        length = len(df)
        df.loc[length] = row_data
        print(df)


#Creating a file to write the data frame
def write_to_file(file_name):
    df.to_csv(file_name, encoding='utf-8')

#Assign target url to data variable
def data_target(data_url):
    data = requests.get(data_url).text
    return data

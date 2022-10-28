from bs4 import BeautifulSoup
import requests
import pandas as pd
url = "http://www.ssn.unam.mx/sismicidad/ultimos/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
soup


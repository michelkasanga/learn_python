import requests
from bs4 import BeautifulSoup   
# This script fetches the content of a web page and prints it.

#url = "https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7296776-extrayez-et-transformez-des-donnees-avec-lextraction-web"
#page = requests.get(url)
#print(page.content)

with open("Extra/index.html", "r") as file:
    soup = BeautifulSoup(file.read(), "html.parser")
    print(soup.prettify())
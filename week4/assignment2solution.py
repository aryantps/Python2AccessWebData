import urllib.request
from bs4 import BeautifulSoup

url = input("Enter URL: ")
position = int(input("Enter position : "))
count = int(input("Enter count : "))

for i in range(count):
        handler = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(handler, 'html.parser')
        tags = soup('a')
        url = tags[position-1].get('href', None)
        print((url[39 : ])[ : -5])

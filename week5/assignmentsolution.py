import xml.etree.ElementTree as ET
import urllib.request

tree = ET.fromstring(urllib.request.urlopen(input("Enter URL: ")).read())
lst = [int(i.find('count').text) for i in tree.findall('comments/comment')]
print(sum(lst))
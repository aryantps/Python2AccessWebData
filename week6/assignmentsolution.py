import json
import urllib.request
 
info = json.loads(urllib.request.urlopen(input("Enter URL : ")).read())

lst = [item['count'] for item in info['comments']]
print("sum is :",sum(lst))

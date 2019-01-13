import urllib.request
import urllib.parse

response = urllib.request.urlopen('http://www.17k.com/chapter/2933095/36699279.html')
print(response.read().decode('utf-8'))
from urllib.request import urlopen as url

page = url('http://127.0.0.1/')

print(page.read())
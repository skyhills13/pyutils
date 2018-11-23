import requests
from bs4 import BeautifulSoup

btsshop_url = "https://www.ibighit.com/goods/catalog?code=00140004"

# http://docs.python-requests.org/en/master/user/quickstart/
page = requests.get(btsshop_url)
contents = page.content
print(contents)

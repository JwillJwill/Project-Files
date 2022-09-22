from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/tools/custom-pc-builder/pl/ID-343?diywishlist=0&cm_sp=pc_builder-_-Under_Search_Bar-_-PC+Builder&icid=671801"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)

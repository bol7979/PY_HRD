import os
import requests
from bs4 import BeautifulSoup

query = "test"
g_url = f"https://www.google.com/search?q={query}"



download_folder = f"./{query}"

if not os.path.exists(download_folder):
    os.makedirs(download_folder)



g_r = requests.get(g_url)
g_r_s = BeautifulSoup(g_r.text, "html.parser")

g_uls = g_r_s.find("div", class_= "wIjY0d jFk0f")
divs = g_uls.find_all("div")

articles = []
downloaded = 0
for item in divs:
    title = item.find("div", class_="juwGPd BwPElf OCzgxd").text

    description = item.find("a")

    img_url = item.find("g-img").get("src")
    img_data = requests.get(f"https:{img_url}").content
    # ./태풍/image_1.jpg
    img_name = os.path.join(download_folder, f"image_{downloaded}.jpg")
    downloaded = downloaded + 1
    article = {
        "title": title, 
        "description": description
    }
    articles.append(article)

    with open(img_name, "wb") as img_file:
        img_file.write(img_data)

print(f"{downloaded}개의 이미지를 다운로드 했습니다")
print(articles) 

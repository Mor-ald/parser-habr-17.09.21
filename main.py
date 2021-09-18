import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup


with open("dataArticle.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ["title", "href", "annotation"]
    )

url = "https://habr.com/ru/search/page1/?q=jamstack&target_type=posts&order=relevance"
i = 1
while (i < 4):
    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser") 
    nameList = bs.findAll("h2", {"class": "tm-article-snippet__title"})
    hrefList = bs.findAll("a", {"class": "tm-article-snippet__title-link"})
    annotationList = bs.findAll("div", {"class": "article-formatted-body"})
    for j in range(len(nameList)):
        name = nameList[j]
        href = hrefList[j]
        ann = annotationList[j]
        with open("dataArticle.csv", "a") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
                [name.get_text(), "https://habr.com"+href.get("href"), ann.get_text()]
            )
    url = url.replace(str(i), str(i+1))
    i += 1

  

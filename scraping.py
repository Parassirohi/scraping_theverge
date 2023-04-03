import requests
import datetime
from bs4 import BeautifulSoup
from csv import writer

now = datetime.datetime.now()
date_string = now.strftime("%d-%m-%y")
file_name = "verge"

new_file_name = date_string + "_" + file_name + ".csv"


link = "https://www.theverge.com"

r = requests.get(link)
soup = BeautifulSoup(r.content, 'html.parser')

articles = soup.find_all("div", class_="relative border-b border-gray-31 pb-20 md:pl-80 lg:border-none lg:pl-[165px] "
                                       "-mt-20 sm:-mt-40")

header = ["Id", 'Headline', 'URL', 'Author', 'Date']


with open(new_file_name, "w", encoding="utf8", newline='') as f:
    thewriter = writer(f)
    thewriter.writerow(header)

    count = 1

    for article in articles:
        headline = article.find(class_="group-hover:shadow-highlight-blurple").text
        complete_link = article.find("a", class_="group-hover:shadow-highlight-blurple")["href"]
        url = link + complete_link
        author = article.find("a", class_="text-gray-31 hover:shadow-underline-inherit dark:text-franklin mr-8").text
        date = article.find("span", class_="text-gray-63 dark:text-gray-94").text

        info = [count, headline, url, author, date]
        thewriter.writerow(info)
        count += 1

topstoryarticles = soup.find_all("div", class_="max-w-content-block-standard md:w-content-block-compact "
                                               "md:max-w-content-block-compact lg:w-[240px] lg:max-w-[240px] lg:pr-10")

with open(new_file_name, 'a', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    for story in topstoryarticles:
        headline = story.find(class_="group-hover:shadow-underline-franklin").text
        complete_link = story.find("a", class_="group-hover:shadow-underline-franklin")["href"]
        url = link + complete_link
        author = story.find("a", class_="text-gray-31 hover:shadow-underline-inherit dark:text-franklin mr-8").text
        date = story.find("span", class_="text-gray-63 dark:text-gray-94").text

        info = [count, headline, url, author, date]
        thewriter.writerow(info)
        count += 1



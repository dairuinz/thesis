from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def reviewer(url):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    # url = 'https://www.skroutz.gr/s/28630974/Edifier-W800BT-Plus-%CE%91%CF%83%CF%8D%CF%81%CE%BC%CE%B1%CF%84%CE%B1-%CE%95%CE%BD%CF%83%CF%8D%CF%81%CE%BC%CE%B1%CF%84%CE%B1-Over-Ear-%CE%91%CE%BA%CE%BF%CF%85%CF%83%CF%84%CE%B9%CE%BA%CE%AC-%CE%BC%CE%B5-55-%CF%8E%CF%81%CE%B5%CF%82-%CE%9B%CE%B5%CE%B9%CF%84%CE%BF%CF%85%CF%81%CE%B3%CE%AF%CE%B1%CF%82-%CE%9C%CE%B1%CF%8D%CF%81%CE%B1.html?from=featured&product_id=77514992#reviews'
    driver.get(url)
    html_doc = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html_doc, 'html.parser')
    # print(html_doc)

    reviews = []
    for i in soup.find_all("div", {"class": "review-body"}):
        reviews.extend(i)

    j=0
    for i in reviews:
        j+=1
        print(j, ': ', i, sep='')

def collector():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    url = 'https://www.skroutz.gr/c/1863/headphones.html'
    driver.get(url)
    html_doc = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html_doc, 'html.parser')
    # print(html_doc)

    items = []
    for i in soup.find_all("a", {"class": "js-sku-link"}):
        items.append(i.get('href'))

    items = list(set(items))    #removes duplicates

    j = 0
    links = []
    for i in items:
        i = 'https://www.skroutz.gr' + i
        j += 1
        # print(j, ': ', i, sep='')
        links.append(i)

    return links
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


# def reviewer():
def reviewer(url):
    with open(r'reviews.txt', 'a') as fp:
        fp.write('\n\n~~~~~~~~~~~~~~~~~~')
        fp.write(url)
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    # url = 'https://www.skroutz.gr/s/28630974/Edifier-W800BT-Plus-%CE%91%CF%83%CF%8D%CF%81%CE%BC%CE%B1%CF%84%CE%B1-%CE%95%CE%BD%CF%83%CF%8D%CF%81%CE%BC%CE%B1%CF%84%CE%B1-Over-Ear-%CE%91%CE%BA%CE%BF%CF%85%CF%83%CF%84%CE%B9%CE%BA%CE%AC-%CE%BC%CE%B5-55-%CF%8E%CF%81%CE%B5%CF%82-%CE%9B%CE%B5%CE%B9%CF%84%CE%BF%CF%85%CF%81%CE%B3%CE%AF%CE%B1%CF%82-%CE%9C%CE%B1%CF%8D%CF%81%CE%B1.html?from=featured&product_id=77514992#reviews'
    # url = 'https://www.amazon.com/Sony-WH-1000XM4-Canceling-Headphones-phone-call/product-reviews/B0863TXGM3/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
    driver.get(url)
    html_doc = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html_doc, 'html.parser')
    # print(html_doc)

    reviews = []
    for i in soup.find_all("span", {"class": "a-size-base review-text review-text-content"}):
        i = str(i).replace('<span class="a-size-base review-text review-text-content" data-hook="review-body">', '----')
        i = str(i).replace('<span>', '')
        i = str(i).replace('</span>', '')
        i = i.strip()
        # print(i)
        reviews.append(str(i))

    with open(r'reviews.txt', 'a') as fp:
        fp.write('\n'.join(reviews))

    # j=0
    # for i in reviews:
    #     j+=1
    #     print(j, ': ', i, sep='')

# def stars():
def stars(url):
    with open(r'stars.txt', 'a') as fp:
        fp.write(url)
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    # url = 'https://www.skroutz.gr/s/28630974/Edifier-W800BT-Plus-%CE%91%CF%83%CF%8D%CF%81%CE%BC%CE%B1%CF%84%CE%B1-%CE%95%CE%BD%CF%83%CF%8D%CF%81%CE%BC%CE%B1%CF%84%CE%B1-Over-Ear-%CE%91%CE%BA%CE%BF%CF%85%CF%83%CF%84%CE%B9%CE%BA%CE%AC-%CE%BC%CE%B5-55-%CF%8E%CF%81%CE%B5%CF%82-%CE%9B%CE%B5%CE%B9%CF%84%CE%BF%CF%85%CF%81%CE%B3%CE%AF%CE%B1%CF%82-%CE%9C%CE%B1%CF%8D%CF%81%CE%B1.html?from=featured&product_id=77514992#reviews'
    # url = 'https://www.amazon.com/Sony-WH-1000XM4-Canceling-Headphones-phone-call/product-reviews/B0863TXGM3/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
    driver.get(url)
    html_doc = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html_doc, 'html.parser')
    # print(html_doc)

    stars = []
    for i in soup.find_all("span", {"class": "a-icon-alt"}):
        i = str(i).replace('<span class="a-icon-alt">', '')
        i = str(i).replace(' out of 5 stars', '')
        i = str(i).replace('</span>', '')
        # print(i)
        stars.append(str(i))

    stars = stars[3:]   #removes first 3
    stars = stars[:10]

    with open(r'stars.txt', 'a') as fp:
        fp.write('\n'.join(stars))


def collector():
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.headless = True
    driver = webdriver.Firefox(options=options)

    # url = 'https://www.skroutz.gr/c/1863/headphones.html'
    url = 'https://www.amazon.com/b/ref=s9_acss_bw_cg_HW14_1a1_w?node=12097479011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-6&pf_rd_r=1XCQQZDP4A1VNJBMVXT6&pf_rd_t=101&pf_rd_p=d198b49d-d5bb-42a4-9be1-d335ce534f2f&pf_rd_i=172541'
    driver.get(url)
    html_doc = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html_doc, 'html.parser')
    # print(html_doc)

    items = []
    j=0
    for i in soup.find_all("a", {"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"}):
        j+=1
        # print(j, ': ', i.get('href'), sep='')
        items.append(i.get('href'))

    items = list(set(items))    #removes duplicates

    substring = '/gp/slredirect/picassoRedirect.html'
    for it in items.copy():
        if substring in it:
            items.remove(it)

    substring2 = '/sspa/click?ie'
    for it in items.copy():
        if substring2 in it:
            items.remove(it)

    j = 0
    products = []
    for i in items:
        i = 'https://www.amazon.com' + i
        # j += 1
        # print(j, ': ', i, sep='')
        products.append(i)

    # print(products)

    links = []
    for url in products:
        print('~~~~')
        # print(url)

        options = Options()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.headless = True
        driver = webdriver.Firefox(options=options)

        driver.get(url)
        html_doc = driver.page_source
        driver.quit()
        soup = BeautifulSoup(html_doc, 'html.parser')
        # print(html_doc)

        for i in soup.find_all("a", {"class": "a-link-emphasis a-text-bold"}):
            print(i.get('href'))
            links.append(i.get('href'))

    links = list(set(links))  # removes duplicates

    urls = []
    for i in links:
        i = 'https://www.amazon.com' + i
        # j += 1
        # print(j, ': ', i, sep='')
        urls.append(i)

    with open(r'urls.txt', 'w') as fp:
        fp.write('\n'.join(urls))

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def reviewer(url):
    with open(r'reviews.txt', 'a') as fp:
        fp.write('\n' + url)
        fp.close()
    options = Options()
    # options.add_argument('--disable-blink-features=AutomationControlled')
    options.headless = True
    # driver = webdriver.Firefox(firefox_binary=r"/usr/bin/firefox", options=options)
    driver = webdriver.Firefox(firefox_binary=r"/home/maraziotis/Downloads/firefox/firefox/firefox", options=options)

    # url = 'https://www.amazon.com/Sennheiser-HD-450SE-Bluetooth-Headphone/product-reviews/B09325WTV5/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
    driver.get(url)
    html_doc = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html_doc, 'html.parser')

    results =  soup.find_all("div", {"class": "a-section review aok-relative"})

    reviews = []
    for i in results:
        # print(i.find('span', attrs={'class':'a-size-base review-text review-text-content'}).text)
        reviews.append(i.find('span', attrs={'class': 'a-size-base review-text review-text-content'}).text)

    with open(r'reviews.txt', 'a') as fp:
        fp.write(''.join(reviews))
        fp.close()

def stars(url):
    with open(r'stars.txt', 'a') as fp:
        fp.write('\n' + url)

    options = Options()
    # options.add_argument('--disable-blink-features=AutomationControlled')
    options.headless = True
    # driver = webdriver.Firefox(firefox_binary=r"/etc/firefox", options=options)
    driver = webdriver.Firefox(firefox_binary=r"/home/maraziotis/Downloads/firefox/firefox/firefox", options=options)

    # url = 'https://www.amazon.com/Sennheiser-HD-450SE-Bluetooth-Headphone/product-reviews/B09325WTV5/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
    driver.get(url)
    html_doc = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html_doc, 'html.parser')

    results =  soup.find_all("div", {"class": "a-section review aok-relative"})

    stars = []
    for i in results:
        stars.append(i.find('span', attrs={'class': 'a-icon-alt'}).text.replace('<span class="a-icon-alt">', '').replace(' out of 5 stars', '').replace('</span>', ''))
        # stars.append(i.find('span', attrs={'class': 'a-icon-alt'}).text)

    with open(r'stars.txt', 'a') as fp:
        fp.write('\n'.join(stars))


def collector(url):
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.headless = True
    driver = webdriver.Firefox(firefox_binary=r"/usr/bin/firefox", options=options)

    # url = 'https://www.amazon.com/b/ref=s9_acss_bw_cg_HW14_1a1_w?node=12097479011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-6&pf_rd_r=1XCQQZDP4A1VNJBMVXT6&pf_rd_t=101&pf_rd_p=d198b49d-d5bb-42a4-9be1-d335ce534f2f&pf_rd_i=172541'
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
        print(url)

        options = Options()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.headless = True
        driver = webdriver.Firefox(firefox_binary=r"/usr/bin/firefox", options=options)

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

    with open(r'urls.txt', 'a') as fp:
        fp.write('\n'.join(urls) + '\n')

def results(url):
    for k in range(1,10):
        options = Options()
        # options.add_argument('--disable-blink-features=AutomationControlled')
        options.headless = True
        driver = webdriver.Firefox(firefox_binary=r"/usr/bin/firefox", options=options)

        # url = 'https://www.amazon.com/b/ref=s9_acss_bw_cg_HW14_1a1_w?node=12097479011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-6&pf_rd_r=1XCQQZDP4A1VNJBMVXT6&pf_rd_t=101&pf_rd_p=d198b49d-d5bb-42a4-9be1-d335ce534f2f&pf_rd_i=172541'
        driver.get(url)
        html_doc = driver.page_source
        # driver.quit()
        soup = BeautifulSoup(html_doc, 'html.parser')

        # with open(r'test.html', 'w') as fp:
        #     fp.write(html_doc)
        #     fp.close()

        pages = []
        for i in soup.find_all("a", {"class": "s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"}):
            print('ok')
            print(k, ': ', i.get('href'), sep='')
            pages.append('https://www.amazon.com' + i.get('href'))
            url = 'https://www.amazon.com' + i.get('href')
            with open(r'pages.txt', 'a') as fp:
                fp.write('\n'.join(pages) + '\n')
import alloc
import preprocessor
import scraper
from os.path import exists


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def main():
    url = 'https://www.amazon.com/b/ref=s9_acss_bw_cg_HW14_1a1_w?node=12097479011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-6&pf_rd_r=1XCQQZDP4A1VNJBMVXT6&pf_rd_t=101&pf_rd_p=d198b49d-d5bb-42a4-9be1-d335ce534f2f&pf_rd_i=172541'
    if not exists('pages.txt'):
        print('Gathering Pages...')
        scraper.results(url)

    if not exists('urls.txt'):
        print('Gathering Urls...')
        for i in open('pages.txt').readlines():
            print(i.replace('\n', ''))
            url = i.replace('\n', '')
            scraper.collector(url)

    if not exists('stars.txt'):
        print('Gathering Stars...')
        j=0
        for u in open('urls.txt').readlines():
            j+=1
            print(j, ': ', u.replace('\n', ''), sep='')
            scraper.stars(u)

    if not exists('reviews.txt'):
        print('Gathering Reviews...')
        j = 0
        for u in open('urls.txt').readlines():
            j += 1
            print(j, ': ', u.replace('\n', ''), sep='')
            scraper.reviewer(u)


    # df1, df2 = preprocessor.preprocessor()

    # df = preprocessor.merger(df1, df2)
    #
    # alloc.alloc(df)

    # options = Options()
    # # options.add_argument('--disable-blink-features=AutomationControlled')
    # options.headless = True
    # driver = webdriver.Firefox(firefox_binary=r"/usr/bin/firefox", options=options)
    #
    # url = 'https://www.amazon.com/Sennheiser-HD-450SE-Bluetooth-Headphone/product-reviews/B09325WTV5/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
    # driver.get(url)
    # html_doc = driver.page_source
    # # driver.quit()
    # soup = BeautifulSoup(html_doc, 'html.parser')
    #
    # results =  soup.find_all("div", {"class": "a-section review aok-relative"})
    #
    # for i in results:
    #     print(i.find('span', attrs={'class':'a-size-base review-text review-text-content'}).text)

if __name__ == "__main__":
    main()


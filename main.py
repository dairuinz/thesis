import alloc
import preprocessor
import scraper
from os.path import exists

def main():
    url = 'https://www.amazon.com/b/ref=s9_acss_bw_cg_HW14_1a1_w?node=12097479011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-6&pf_rd_r=1XCQQZDP4A1VNJBMVXT6&pf_rd_t=101&pf_rd_p=d198b49d-d5bb-42a4-9be1-d335ce534f2f&pf_rd_i=172541'
    if not exists('pages.txt'):
        scraper.results(url)

    if not exists('urls.txt'):
        for i in open('pages.txt').readlines():
            print(i.replace('\n', ''))
            url = i.replace('\n', '')
            scraper.collector(url)

    if not exists('stars.txt'):
        j=0
        for u in open('urls.txt').readlines():
            j+=1
            print(j, ': ', u.replace('\n', ''), sep='')
            scraper.stars(u)

    if not exists('reviews.txt'):
        j = 0
        for u in open('urls.txt').readlines():
            j += 1
            print(j, ': ', u.replace('\n', ''), sep='')
            scraper.reviewer(u)


    df1, df2 = preprocessor.preprocessor()

    df = preprocessor.merger(df1, df2)

    alloc.alloc(df)

if __name__ == "__main__":
    main()


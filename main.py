import preprocessor
import scraper
from os.path import exists

def main():
    links = scraper.collector()
    # print(len(links))

    for i in links:
        print(i)
    #     scraper.reviewer(i)

    # if not exists('reviews.txt'):
    #     scraper.reviewer()
    #
    # if not exists('stars.txt'):
    #     scraper.stars()
    #
    # preprocessor.preprocessor()

if __name__ == "__main__":
    main()


import preprocessor
import scraper
from os.path import exists

def main():
    if not exists('urls.txt'):
        scraper.collector()

    urls_file = open('urls.txt', 'r')
    urls = urls_file.readlines()

    if not exists('stars.txt'):
        open('stars.txt', 'w')
        for u in urls:
            print(u)
            scraper.stars(u)

    if not exists('reviews.txt'):
        open('reviews.txt', 'w')
        for u in urls:
            print(u)
            scraper.reviewer(u)

    # preprocessor.preprocessor()

if __name__ == "__main__":
    main()


import scraper

def main():
    links = scraper.collector()

    # print(len(links))

    for i in links:
        scraper.reviewer(i)

if __name__ == "__main__":
    main()

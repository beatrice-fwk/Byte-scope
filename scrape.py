import requests
from bs4 import BeautifulSoup
from db import init_db, insert_news

def scrape_hacker_news():
    url = "https://thehackernews.com/"
    page_count = 0
    max_pages = 10
    while url and page_count < max_pages:
        print(f"Scraping page {page_count + 1}: {url}")
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("a", class_="story-link")

        for article in articles:
            headline = article.find("h2", class_="home-title")
            art_date = article.find("span", class_="h-datetime")
            content = article.find("div", class_="home-desc")
            link = article['href'] if article.has_attr('href') else None
            if headline:
                headline_text = headline.text.strip()
                art_date_text = art_date.text.strip() if art_date else None
                content_text = content.text.strip() if content else None
                insert_news(None, headline_text, art_date_text, link, content_text)
                print(f"Inserted: {headline_text}")

        page_count += 1
        # Find the next page link using the correct anchor tag
        next_link = soup.find("a", class_="blog-pager-older-link-mobile")
        if next_link and next_link.has_attr('href'):
            url = next_link['href']
        else:
            print("No more pages found. Scraping complete.")
            url = None
    if page_count >= max_pages:
        print(f"Page limit of {max_pages} reached. Stopping scrape.")

if __name__ == "__main__":
    init_db()
    scrape_hacker_news()
 

import os

from db import fetch_all_articles
from dotenv import load_dotenv
from google import genai

load_dotenv()

def store_article(articles):
    lines = []
    for id, headline, content in articles:
        lines.append(f"Article {id}:{headline}\n{content}\n\n")
    return "\n".join(lines)   

def main():
    articles = fetch_all_articles()
    article_text = store_article(articles)
    
    client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
    )
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = f"Summarize this article in 2 sentences: \n\n{article_text}"
    )
    print (response.text)
 
if __name__ == "__main__":
    main()   
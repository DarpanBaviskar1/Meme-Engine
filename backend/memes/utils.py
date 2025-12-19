from geminiapi import generate_funny_caption, generate_hashtags, generate_meme_image
import keys
import requests
from .storage import memes_storage, save_memes

def fetch_memes(query='', count=5):
    api_key = keys.NEWS_API_KEY
    if query:
        url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&language=en&apiKey={api_key}"
    else:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    articles = response.json().get("articles", [])[:count]
    memes = []
    for article in articles:
        headline = article.get("title", "")
        description = article.get("description", "")
        caption = generate_funny_caption(headline, description)
        hashtags = generate_hashtags(headline, description)
        image_b64 = generate_meme_image(caption, headline, description)
        meme = {
            "headline": headline,
            "description": description,
            "meme_caption": caption,
            "meme_image_b64": image_b64,
            "hashtags": hashtags
        }
        memes_storage.append(meme)
        save_memes(memes_storage)
        # print("memes_storage after append:", memes_storage)
    return memes
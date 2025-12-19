from django.shortcuts import render
import requests
from datetime import datetime
from geminiapi import generate_funny_caption, generate_hashtags, generate_meme_image
import os
from django.conf import settings
from .forms import MemeForm
from pillow import make_meme
import keys
from .utils import fetch_memes
from .storage import memes_storage, save_memes
from .input_news import user_assemble
import base64


def home(request):
    return render(request, 'home.html')
    
def news_list(request):
    api_key = keys.NEWS_API_KEY
    query = request.GET.get('q', '')  
    
    if query:
      
        url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&language=en&apiKey={api_key}"
    else:
       
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        articles = data.get("articles", [])

        
        structured_articles = []
        for article in articles:
            
            published_at = article.get("publishedAt")
            if published_at:
                try:
                    date_obj = datetime.fromisoformat(published_at.replace('Z', '+00:00'))
                    formatted_date = date_obj.strftime("%B %d, %Y at %I:%M %p")
                except:
                    formatted_date = published_at
            else:
                formatted_date = "Unknown"

            headline = article.get("title", "")
            description = article.get("description", "")

            

            structured_articles.append({
                "headline": headline,
                "source": article.get("source", {}).get("name"),
                "description": description,
                "url": article.get("url"),
                "image": article.get("urlToImage"),
                "published_at": formatted_date,
                "author": article.get("author"),
                
            })

        return render(request, 'news_list.html', {
            "articles": structured_articles,
            "query": query,
            "total_results": len(structured_articles)
        })
        
    except requests.RequestException as e:
        # Handle API errors
        return render(request, 'news_list.html', {
            "articles": [],
            "query": query,
            "error": f"Error fetching news: {str(e)}"
        })

def memes_view(request):
    query = request.GET.get('q', '')
    try:
        memes = fetch_memes(query)
        return render(request, 'memes.html', {"articles": memes, "query": query})
    except Exception as e:
        return render(request, 'memes.html', {"articles": [], "query": query, "error": str(e)})

def generate_meme_view(request):
    if request.method == "POST":
        headline = request.POST.get("headline", "")
        description = request.POST.get("description", "")
        meme_type = request.POST.get("meme_type", "ai")  # Default to AI generated
        
        caption = generate_funny_caption(headline, description)
        hashtags = generate_hashtags(headline, description)
        
        # Initialize variables
        image_b64 = None
        image_2 = None
        meme_image = None
        
        if meme_type == "ai":
            # Generate AI meme
            image_b64 = generate_meme_image(caption, headline, description)
            meme_image = "ai_generated"
        else:
            # Generate template-based meme
            news = headline + description
            try:
                # user_assemble(news)
                meme_image = "output_2.jpg"
                with open(r"C:\Users\darpa\OneDrive\Desktop\darpan\darpan\backend\memes\static\generated_memes\output_2.jpg", "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                image_2 = encoded_string
            except Exception as e:
                print(f"Error generating template meme: {e}")
                # Fallback to AI meme
                image_b64 = generate_meme_image(caption, headline, description)
                meme_image = "ai_generated"

        meme = {
            "headline": headline,
            "description": description,
            "meme_caption": caption,
            "meme_image_b64": image_b64,
        
            "hashtags": hashtags,
            "meme_type": meme_type
        }
        memes_storage.append(meme)
        save_memes(memes_storage)

        return render(request, "meme_display.html", {
            "meme": meme, 
            "meme_image": meme_image,
            "news": headline
        })
    else:
        return render(request, "meme_display.html", {"meme": None, "error": "Invalid request method."})
    

def meme_generator_view(request):
    meme_url = None
    if request.method == 'POST':
        form = MemeForm(request.POST)
        if form.is_valid():
            template = form.cleaned_data['template']
  
            headline = request.POST.get('headline', '')  
            description = request.POST.get('description', '')
      
            caption = generate_funny_caption(headline, description)
          
            top_text = caption 
            bottom_text = ""  
            template_path = os.path.join(settings.MEDIA_ROOT, 'templates', template)
            output_filename = f"meme_{headline[:10]}_{description[:10]}.jpg"
            output_path = os.path.join(settings.MEDIA_ROOT, 'generated', output_filename)
            make_meme(template_path, top_text, bottom_text, output_path)
            meme_url = settings.MEDIA_URL + 'generated/' + output_filename
    else:
        form = MemeForm()
    return render(request, 'meme_generator.html', {'form': form, 'meme_url': meme_url})

def another_func(request):
    if request.method == "POST":
        headline = request.POST.get("headline", "")
        description = request.POST.get("description", "")
        
        caption = generate_funny_caption(headline, description)
        hashtags = generate_hashtags(headline, description)
        
        # Initialize variables
        image_2 = None
        meme_image = None
        
        # Generate template-based meme only
        news = headline + description
        try:
            user_assemble(news)
            meme_image = "output_2.jpg"
            with open(r"C:\Users\darpa\OneDrive\Desktop\darpan\darpan\backend\memes\static\generated_memes\output_2.jpg", "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            image_2 = encoded_string
        except Exception as e:
            print(f"Error generating template meme: {e}")
            return render(request, "meme_display.html", {
                "meme": None, 
                "error": f"Failed to generate template meme: {str(e)}"
            })

        meme = {
            "headline": headline,
            "description": description,
            "meme_caption": caption,
            "meme_image_b64": None,
            "meme_image_2": image_2,
            "hashtags": hashtags,
            "meme_type": "template"
        }
        memes_storage.append(meme)
        save_memes(memes_storage)

        return render(request, "meme_display.html", {
            "meme": meme, 
            "meme_image": meme_image,
            "news": headline
        })
    else:
        return render(request, "meme_display.html", {"meme": None, "error": "Invalid request method."})

def generate_meme2_view(request):
    """Handle the Another Action button from news list"""
    if request.method == "POST":
        headline = request.POST.get("headline", "")
        description = request.POST.get("description", "")
        
        # You can add your custom logic here
        # For example: save to favorites, share , analyze, etc.
        
        # Load and encode the meme image
        news = headline
        user_assemble(news)
        meme_image = "output_2.jpg"
        # with open(r"C:\Users\darpa\OneDrive\Desktop\darpan\darpan\backend\memes\static\generated_memes\output_2.jpg", "rb") as image_file:
        meme_image_path = os.path.join(os.path.dirname(__file__), "static", "generated_memes", "output_2.jpg")
        with open(meme_image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        image_2 = encoded_string
        
        # Create meme object
        meme = {
            "headline": headline,
            "description": description,
            "meme_image_2": image_2,
        }
        
        # Save to storage
        memes_storage.append(meme)
        save_memes(memes_storage)

        # Return the response
        return render(request, "meme_display.html", {
            "meme": meme, 
            "meme_image": meme_image,
            "news": headline
        })
    else:
        return render(request, "meme_display.html", {"error": "Invalid request method."})
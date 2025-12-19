# from google import genai


from xmlrpc import client
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64
import keys
API_KEY = keys.GOOGLE_API_KEY

def generate_funny_caption(headline, description):
    client = genai.Client(api_key=API_KEY)
    prompt = f"Write only one funny meme caption for this news, also maintain the context of caption,such that one can understand the it easily: Headline-{headline} and Description- {description}"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text  # <-- return the caption

def generate_meme_image(caption, headline, description):
    client = genai.Client(api_key=API_KEY)
    contents = f"Create a popular meme-style image. Image with clean background, no inscriptions: {caption}.“no text,” “no words,” “no letters,” “no captions,” “no typography,” “no writing,” “no font,” “no handwriting,” “no calligraphy,” “no script,” “no signage,” “no labels,” “no logos,” “no watermarks.”"
    response = client.models.generate_content(
        model="gemini-2.0-flash-preview-image-generation",
        contents=contents,
        config=types.GenerateContentConfig(
            response_modalities=['TEXT', 'IMAGE']
        )
    )

    for part in response.candidates[0].content.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            image = Image.open(BytesIO((part.inline_data.data)))
            buffered = BytesIO()
            image.save(buffered, format="PNG")
            img_b64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
            return img_b64  # <-- return the base64 string
    return None  # fallback if no image found



# # generate_meme_image("Cat is playing with ball!")
# generate_funny_caption("Nolan's new movie", "A mind-bending thriller that will leave you questioning reality.") 
def generate_hashtags(headline, description):
    client = genai.Client(api_key=API_KEY)
    prompt = f"Generate a list of 5 relevant hashtags without spaces for the following news article: Headline-{headline} and Description- {description}. Output format should be: #hashtag1 #hashtag2 #hashtag3 #hashtag4 #hashtag5"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text  # <-- return the hashtags


# print(generate_hashtags("Nolan's new movie", "A mind-bending thriller that will leave you questioning reality."))
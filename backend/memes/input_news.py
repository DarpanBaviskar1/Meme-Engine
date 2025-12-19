# import requests, json
# from .constants import template1, template2
# import random
# from PIL import Image, ImageDraw, ImageFont
# import textwrap
# from .meme_detail import details

# def generate_meme_caption(news, part):
#     url = "https://api.mistral.ai/v1/chat/completions"
#     api_key = "Mfp20fD3sT6CxjcYJiy4gUPr2unaKLeq"
#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": "application/json"
#     }
    
    
#     if part == 1:
#         templates = template1
#     elif part == 2:
#         templates = template2


#     data = {
#         "model": "mistral-large-2467",
#         "messages": [
#             {
#                 "role": "user",
#                 "content": (
#                     """You are a savage Gen Z meme lord. I am giving you a trending news headline and a list of meme
#                     templates. Choose the single best template that fits the news. Then, generate captions that match
#                     the chosen template's structure.The captions must be:
#                     - Hilarious, outrageous, or deeply ironic
#                     - Loaded with sarcasm, absurdity, exaggeration, or pop culture
#                     - Rooted in dark Indian humor with censored cuss words (e.g., f*, b**, s*)
#                     - Not generic or cringe — push boundaries, but with light censorship
#                     - So funny, weird, or offensive that it shocks or makes people burst out laughing
#                     **Return only a JSON object** with captions matching the template's format. No extra words or explanations.
#                     Humor principles to follow: incongruity, relatability, exaggeration, absurdity, irony, dark humor, randomness, unpredictability.
#                     ONLY output the JSON. Nothing else.
#                     List of meme templates:""" + templates +

#                     """
#                     news:""" + news + """ 

#                     example output:
#                     {
#                     "news_headline": "Indias biggest IT firm has been making news after its unexpected decision to trim about two percent of its global workforce.",
#                     "meme_template": "Drake_Hotline_Bling",
#                     "meme_caption": {
#                     "top_text": "Getting a stable job",
#                     "bottom_text": "Getting laid off and finally pursuing your dream of becoming a stand-up comedian"
#                         }
#                     }
#                     The output that u give should look exactly like this example. DO NOT CHANGE THE FORMAT
#                     Remember to only return 1 json object containing meme data for one news do not give more than one captions for the same news.
#                     Try not to rely too much on 'Disaster Girl'. Only use them if you think it will be good. Otherwise, aim for and choose from the other templates.
#                     Even though I have given you examples of drake template and distracted boyfriend template, you are free
#                     to use the template of your choice.

#                     The top_text, bottom_text should vary according to the meme, like for distracted boyfriend, you have to give: girl, boyfriend, girlfriend.
#                     And, the captions you give should be in order left to right or top to bottom. Return a json file. Do not give more than the number of captions assigned for a meme template.
#                     for exmaple Mother_Ignoring_Kid_Drowning_In_A_Pool has a max of 3 captions, so give only 3.
#                      """
#                 )
#             }
#         ],
#         "temperature": 1.1,
#         "top_p": 0.98,
#         "max_tokens": 200,
#     }
#     try:
#         response = requests.post(url, headers=headers, json=data)
#         response.raise_for_status()
#         content = response.json()["choices"][0]["message"]["content"].strip()
#         return content
#     except Exception as e:
#         print("Mistral Error", e)
#         return "Meme error!"
    


# def user_assemble(news):

#     n = random.randint(1,2)

#     caption = generate_meme_caption(news,n)
#     print(caption)
#     print(type(caption))

#     if caption == "Meme error!":
#         print("stopping due to meme generation error")

#     cleaned = caption.replace("json", "").replace("  ", " ").strip()
#     cleaned = cleaned[3:-3]
#     print(cleaned)

#     parsed = json.loads(cleaned)
#     meme_list = []
#     meme_list.append(parsed)

#     ####################################################

#     number = 2
#     for info in meme_list:
#         news = info["news_headline"]
#         meme_template = info["meme_template"]
#         captions = info["meme_caption"]

#         img = Image.open(f"memes/static/meme_templates/{meme_template}.jpg")

#         index = 0
#         for i in details:
#             dict = i
#             if i["meme_template"] == meme_template:
#                 break
#             index += 1

#         draw = ImageDraw.Draw(img)

#         try:
#             font = ImageFont.truetype("memes/static/fonts/impact.ttf", details[index]["size"])

#         except:
#             font = ImageFont.load_default()

#         wrapped_text = []
#         for j in captions:
#             text = textwrap.fill(captions[j], width=details[index]["width"])
#             wrapped_text.append(text)

#         m = 0
#         for k in wrapped_text:
#             draw.multiline_text(details[index]["coordinates"][m], k, fill='white', font=font, stroke_width=2, stroke_fill='black')
#             m += 1

#         img.save(f"memes/static/generated_memes/output_{number}.jpg")
#         number += 1



import requests, json
from .constants import template1, template2
import random
from PIL import Image, ImageDraw, ImageFont
import textwrap
from .meme_detail import details

def generate_meme_caption(news, part):
    url = "https://api.mistral.ai/v1/chat/completions"
    # api_key = "Mfp20fD3sT6CxjcYJiy4gUPr2unaKLeq"
    api_key = "tLlXWtoZ2F7Qz6ogRq81xbbGjIBwbNu6"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    
    if part == 1:
        templates = template1
    elif part == 2:
        templates = template2


    data = {
        "model": "open-mixtral-8x7b",
        "messages": [
            {
                "role": "user",
                "content": (
                    """You are a savage Gen Z meme lord. I am giving you a trending news headline and a list of meme
                    templates. Choose the single best template that fits the news. Then, generate captions that match
                    the chosen template's structure.The captions must be:
                    - Hilarious, outrageous, or deeply ironic
                    - Loaded with sarcasm, absurdity, exaggeration, or pop culture
                    - Rooted in dark Indian humor with censored cuss words (e.g., f*, b*, s)
                    - Not generic or cringe — push boundaries, but with light censorship
                    - So funny, weird, or offensive that it shocks or makes people burst out laughing
                    *Return only a JSON object* with captions matching the template's format. No extra words or explanations.
                    Humor principles to follow: incongruity, relatability, exaggeration, absurdity, irony, dark humor, randomness, unpredictability.
                    ONLY output the JSON. Nothing else.
                    List of meme templates:""" + templates +

                    """
                    news:""" + news + """ 

                    example output:
                    {
                    "news_headline": "Indias biggest IT firm has been making news after its unexpected decision to trim about two percent of its global workforce.",
                    "meme_template": "Drake_Hotline_Bling",
                    "meme_caption": {
                    "top_text": "Getting a stable job",
                    "bottom_text": "Getting laid off and finally pursuing your dream of becoming a stand-up comedian"
                    }
                    }

                    another example output:
                    {
                    "news_headline": "Freight train slams into a bus outside Mexico City and kills at least 8 people - AP News",
                    "meme_template": "Buff_Doge_Vs_Cheems",
                    "meme_caption": {
                        "top_text": "Train back in the day:",
                        "bottom_text": "Train nowadays in Mexico City:"
                    }
                    }
                    
                    THE OUTPUT THAT YOU GIVE SHOULD CONTAIN ONLY THE JSON OBJECT IN THE ABOVE GIVEN FORMAT. DO NOT CHANGE THE FORMAT. DO NOT OUTPUT ANYTHING ELSE, IT IS A STRICT ORDER
                    Remember to only return 1 json object containing meme data for one news do not give more than one captions for the news.
                    Try not to rely too much on 'Disaster Girl'. Only use them if you think it will be good. Otherwise, aim for and choose from the other templates.
                    Even though I have given you examples of drake template and distracted boyfriend template, you are free
                    to use the template of your choice.

                    The top_text, bottom_text should vary according to the meme, like for distracted boyfriend, you have to give: girl, boyfriend, girlfriend.
                    And, the captions you give should be in order left to right or top to bottom. Return a json file. Do not give more than the number of captions assigned for a meme template.
                    for exmaple Mother_Ignoring_Kid_Drowning_In_A_Pool has a max of 3 captions, so give only 3.

                    Dont add any escape characters like backslash in the json object.
                     """
                )
            }
        ],
        "temperature": 1.1,
        "top_p": 0.98,
        "max_tokens": 200,
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"].strip().replace('\\', '')
        return content
    except Exception as e:
        print("Mistral Error", e)
        return "Meme error!"
    


def user_assemble(news):

    n = random.randint(1,2)

    caption = generate_meme_caption(news,n)
    print(caption)
    print(type(caption))

    if caption == "Meme error!":
        print("stopping due to meme generation error")

    # cleaned = caption.replace("json", "").replace("  ", " ").strip()
    # cleaned = cleaned[3:-3]
    # print(cleaned)

    # parsed = json.loads(cleaned)
    parsed = json.loads(caption)
    meme_list = []
    meme_list.append(parsed)

    ####################################################

    number = 2
    for info in meme_list:
        news = info["news_headline"]
        meme_template = info["meme_template"]
        captions = info["meme_caption"]

        img = Image.open(f"memes/static/meme_templates/{meme_template}.jpg")

        index = 0
        for i in details:
            dict = i
            if i["meme_template"] == meme_template:
                break
            index += 1

        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype("memes/static/fonts/impact.ttf", details[index]["size"])

        except:
            font = ImageFont.load_default()

        wrapped_text = []
        for j in captions:
            text = textwrap.fill(captions[j], width=details[index]["width"])
            wrapped_text.append(text)

        m = 0
        for k in wrapped_text:
            draw.multiline_text(details[index]["coordinates"][m], k, fill='white', font=font, stroke_width=2, stroke_fill='black')
            m += 1

        img.save(f"memes/static/generated_memes/output_{number}.jpg")
        number += 1
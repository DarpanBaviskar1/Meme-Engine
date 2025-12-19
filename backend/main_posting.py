import base64
import dropbox
import pathlib
import time
import requests
import json
from memes.storage import memes_storage, load_memes


memes_storage = load_memes()
if memes_storage:
    latest_meme = memes_storage[-1]
    # Use latest_meme['headline'], latest_meme['meme_caption'], latest_meme['meme_image_b64'], etc.
    print(latest_meme)
else:
    print("No memes generated yet.")
    
    
ig_user_id = "YOUR_BUSINESS_IG_ID_FROM_META_DEV"
access_token = "YOUR_GRAPH_API_ACCESS_TOKEN"

ACCESS_TOKEN = 'YOUR_DROPBOX_ACCESS_TOKEN' # Replace with your actual token
base64_string = latest_meme['meme_image_b64'].replace("data:image/png;base64,", "")
image_data = base64.b64decode(base64_string)
with open("output_image.png", "wb") as image_file:
    image_file.write(image_data)
    
    

            # Replace with your actual access token
dropbox_access_token = "sl.u.AF6_cQTB2oNbKTrVMpQepFdFofXaDyy0Djtuqu3KY6Q50YZjBDXgktvVcmL5CQTc_dDGoBrAw18tl6DReWwOomg1l7HzOsT93boT80SM1o0io8D_icK4TqvDO_p5yOQvyBeQlYe1pWQ8xGk0GsN89YYgBLGJTSuK9VEMbJ6HLESdhlXE7kNwMiobrbpVLoPYxiaIC0jW7Jj5DjlDXKfbEUff40i-RTQHZGSVccn9qPfBwJa1aWjEG3bktWiVPLAzSNgAguq-sQyTGYzZck_BogjPhhlHpaKS7bYdImiIH-lby4UD38-SkjoGCVPc-W62sEaahIsvveKY19_c4PFkeon9dRCk7LFkovfnIBCWTzinLxMEsdd6UxxTW3yX-epN65dFYaCi5M-PuOj2kFkb7i9IjHxft-pX3DpG_KMPqK-VfZfkC6NsNOV3NRNYpe6nT87CDd0C9jIfY_JdX_b6oSAJXFuFAdVyFHojdkg7N4w1nfEY5seb26Jv_q2GF8pZOg6k9W6F7sNO3yhh0SKWYhWOCFsmWG3m5p07Mv5MI2Ee3d8Rq6pyu6In-cj9RrDDLVOC2hhoadYWfY7cpY8sr4Zif_GnFpldF84O25AQBHiLMiEIsfsEQ-QViFmGu3As8ZApT2wIWKXkFSsaeuh-4lwt2O-rp4r9Jk6eGF1qm8hVUre__ZNUq3wetoGYEzrBC3T84E6JHn2-2a79tmguwX4Zz3nt5sCmCcZX8slaRI2ThC0bfuhia1P7cgROoZqA7rvfUZOH_T2D6DYs8f82C3r1S6RERGfthLgcem_830pmo0XwUJAn3KMjfXV8MCQU_w5cTT-pEc3s4Yjevxf5ef6c7kWXLV-G03vt1Z0tT0CaNsaL4AtJdWdjSU8y_fZ1LL2jl_2Sr84WnBgGynKyOSkbexBsGpkyqBzdNMOJyOwgdhQJ0Wf38gsFIkAR_gjnFdUpS0fE5U3v26ipLK8QYK1UJums0Kk7v4neCZZZov9dke17k9nRFX5heUA8iDOxz9VJfp3ixskIVzqFGu2pjjjwh-b8BHP97ejltMKAD7BVOCri9w1zzaamwE7nnHjTIcCaD1WdB-tGJBQDKt_dWW7PgYlNPqF6XNFCF6jcc1Mf2qMPlNMOWFWedJyxuONFic3S20HuGGTPjNt1YIWXg8czV97Q2XKM9ZU-XxeQd9aKGjTR16z2klmbg8p1R-oPm7kti_NUdFBT2nncnAsrgpNxB_uU1X7HH6_AoVY2KVwE7XSCmcbaRMV0MbH8BYaB7G09Y9ogXCG0k7ygqfyZIRsRezo3NruLMBabSTQhqog-53jggOsu0w7Wrnwf99wYQvfJnVm0jVEwaWAKGgFWhH6NTCJ-TOeKfBKkd-etzwL85Hx9bjtClTM5o9f9g2Ozy6cjckLhLHUAbmclOF1Dt1cd9btdKahLDAT-ui7O_wnqbQ" 

            # Local path to the image file
local_image_path = pathlib.Path("C:/Users/darpa/OneDrive/Desktop/MemeEngine Clone/MemeEngine/backend/output_image.png")

            # Desired path in your Dropbox (e.g., /my_images/uploaded_image.jpg)
dropbox_target_path = "/Test/uploaded_image.jpg" 

try:
        # Initialize Dropbox client
        dbx = dropbox.Dropbox(dropbox_access_token)

        # Open the image file in binary read mode
        with local_image_path.open("rb") as f:
            # Upload the file
            meta = dbx.files_upload(f.read(), dropbox_target_path, mode=dropbox.files.WriteMode("overwrite"))
            print(f"File uploaded successfully: {meta.name} ({meta.size} bytes)")
            print(meta)

except dropbox.exceptions.ApiError as err:
        print(f"*** API error: {err}")
except Exception as err:
        print(f"*** Other error: {err}")
        

def get_image_url(dropbox_path):
    """
    Creates a direct URL for an image stored on Dropbox.

    :param dropbox_path: The full path to the image file in your Dropbox.
                          For example: '/Images/uploaded_image.jpg'
    :return: A string containing the direct image URL, or None if an error occurs.
    """
    try:
        dbx = dropbox.Dropbox(ACCESS_TOKEN)
        
        # Create a shared link with 'public' visibility.
        # This requires the 'sharing.write' permission scope.
        shared_link_metadata = dbx.sharing_create_shared_link_with_settings(dropbox_path, settings=dropbox.sharing.SharedLinkSettings(
            requested_visibility=dropbox.sharing.RequestedVisibility.public))
            
        # Get the URL from the shared link metadata
        shared_url = shared_link_metadata.url
        
        # Modify the shared URL for direct image access
        # Replace "?dl=0" with "?raw=1" to get the raw file content.
        
        # direct_url = shared_url.replace('dl=0', 'raw=1')
        
        shared_url = shared_url[:-4]
        shared_url += "raw=1"
        direct_url = shared_url
        # print(direct_url)
        return direct_url

    except dropbox.exceptions.ApiError as err:
        # Handle cases where a link already exists
        if err.error.is_shared_link_already_exists():
            print("Shared link already exists for this path. Retrieving existing link.")
            
            # Use list_shared_links to get the existing link
            links = dbx.sharing_list_shared_links(path=dropbox_path).links
            if links:
                shared_url = links[0].url
                direct_url = shared_url.replace('?dl=0', '?raw=1')
                return direct_url
        
        print(f"Dropbox API error: {err}")
        return None
    
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
        return None

# --- Example usage ---
# Replace with the path to your uploaded image
image_path = '/Test/uploaded_image.jpg' 

# It's good practice to wait a moment after uploading,
# before trying to create the shared link.
print("Waiting a moment to ensure upload is complete...")
time.sleep(10)

image_url = get_image_url(image_path)
if image_url:
    shared_url = image_url[:-4] + "raw=1"
    direct_url = shared_url
    print(f"Direct image URL: {direct_url}")
else:
    print("Could not retrieve image URL.")
    direct_url = None  # Prevent further errors

# Only proceed if direct_url is valid
if direct_url:
    url = f"https://graph.facebook.com/v23.0/{ig_user_id}/media"
    params = {
        "image_url": direct_url,
        "caption": latest_meme['meme_caption'] + " " + "".join(latest_meme['hashtags']),
        "access_token": access_token
    }
    response = requests.post(url, data=params)
    data = response.json()
    print(data)

    creation_id = data.get('id')
    if creation_id:
        publish_url = f"https://graph.facebook.com/v23.0/{ig_user_id}/media_publish"
        publish_params = {
            "creation_id": creation_id,
            "access_token": access_token
        }
        publish_response = requests.post(publish_url, data=publish_params)
        print(publish_response.json())
        print("Your post is live now!")
    else:
        print("Failed to create media on Instagram.")
else:
    print("Skipping Instagram post due to missing image URL.")
# After uploading
print(f"Trying to share Dropbox path: {dropbox_target_path}")
print("Dropbox path:", repr(dropbox_target_path))

# List files in /Test to confirm upload
try:
    for entry in dbx.files_list_folder("/Test").entries:
        print("Found in /Test:", entry.name)
except Exception as err:

    print("Error listing /Test folder:", err)

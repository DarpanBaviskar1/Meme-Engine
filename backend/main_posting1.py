import base64
import dropbox
import pathlib
import time
import requests
import json
from memes.storage import memes_storage, load_memes
import os

memes_storage = load_memes()
i=1
if memes_storage:
    latest_meme = memes_storage[-i]
    # Use latest_meme['headline'], latest_meme['meme_caption'], latest_meme['meme_image_b64'], etc.
    print(latest_meme)
else:
    print("No memes generated yet.")


ig_user_id = "17841476723984166"
access_token = "EAAPYWucuY4oBPJfEUsI33WC0rRwmQ3XOzw1H5oBJaBFHRwzBDeJvRTlRTZB4eZBZAtpQt4Tjt4gOfnngecx7cQG2T0kORFFDiIbze24DYnGaZCJBpXfL8Fgzph3yr83UPcivZBpSyTFZAKeCLq4qZAKHtBqGCx7i7he3QuuWEZCZCIFmR65OZBDcJA5Xtgv58C9FDz"

ACCESS_TOKEN = 'sl.u.AGDr7x3eS96txWka8wsknjvDc8LJ7YVpOUdN2VpjvdktxONUSiz0_4iIReOYLhkjJmGiuU75RqWGkZwzMU816sh2k60adSmXAJtdbFT1g99k3VypsovIxA0zA7QaQVPDGkhCVwr-zwfTEqqXe4VUlYB56d_Pl27V9OKlmmFaFpfkrkwEeIcop7aE0MTqfghgWS45VaOxTeDdIWTmSB5gyqRv698YSv0djZAi5EcmL0lk1eP8PmpCYPz4YhpGmYIeQheFIHf5UD6JRK9Zc4te7O_QPJcmCPXOYUvuxbVy4QfPSL1ekOvDp2wL5wt1GUi4z-B5h_V9L7waKgsT-QuPNKNqmCCZle88a468i-1GpzoVIc3jECntR7vq8_4abntrtMC6uTpzLOmTwZqljK30b50myRbuuC_kRzZ49jQn06g2sIGpRXOD4xpk4fxx7GJGhUfkg2zhkIhUDtYsa9aTarM3ydSTJ2afUT1Ef02oXMt-uq82tuShCOqZ2pHmiy6_799eAKa3ipzogKXnk_WffhBs1w87taXWZPqD58GtzgXuKQsxpHP38sk4IP2ZmuN0eggIcbTT8m5Q3NuxTlHn1_QBn3XzwugIfSRBVKgBK7h_3fiKtM4_6AuE3mg1nHX8l-CLjiLk2X0xWOkhgX6d61WZyCMOKNtB90J1DogD7EhdBCJQmFnJlvtQ8bZynpuCWclpKVB49Bfk-SsN7zGMNfynHEoOHIrV-vt6cyeG3r0DlgXK5CPOclW1HmlRBzhjv1BBltX-KPxIFOVg6KDSAhEnQZG2I-knugTf6icCHtBr0n4K8b1MCgf669y7WJlzzSppJmRog-IU_V3nw4ocn7ZhdiAl-q8RUXgIi_PqXIXSae8_XJqtqx7hYHm5wepxhvI7YhG4wZ1xYcMexSO71-XqVoYxK4aEjBh2lvgx2W3XIp7ScyHdv6MxRMk7D3GzPE594nYqLp4R1UrLp5Q-LZmV5rVSBkJfHN0Lb5e4Elk4C-I4C7TT2xI4crWExvF8S7nCdNTkqLplQmVyy9Wmd5cu4sFO4cLVmDYDNu2jCcNRfXYtiVscB_4owvzNDPkbS8jepDk8dnMrt7uC3ynkZxUhRnk8i5IzxM85RB7GfKsmVKAFwK3GoGlrKMk_3qA44fwpHUBXPrakO41F3rXhGhPxVzENBUcl28ALAnYNScLdwZjdvt8OVH9akjtlHujHSKIfRWKmeUG0vN5R1SJquG6pRhqZ1rtxuMaFT73R46uF172L6NxxFgRxTBpqi32O7g9rI2S-MyS-1nilcvGrVXAZkFOv7NTg5d4sNdKNo4tLBTdFSy6GqmkvM2ixHcSyfI7FCwJRb08JA1IrvD_CGJ2m9JK1nXfQ0vtdrp5irn_tKe7z3HNOhc37TM6BME_j0-_EHSgG8C9Eh6_z7qyS8Yoj8mLYlNqJEGdiWKP2CRerGg' # Replace with your actual token
base64_string = latest_meme['meme_image_2'].replace("data:image/png;base64,", "")
image_data = base64.b64decode(base64_string)
with open("output_image.png", "wb") as image_file:
    image_file.write(image_data)
    
time.sleep(3)  # Ensure the file is written before proceeding

os.system("python C:\\Users\\darpa\\OneDrive\\Desktop\\darpan\\darpan\\backend\\upload_dropbox.py")

#             # Replace with your actual access token
# dropbox_access_token = "sl.u.AF7nVW_bYzRfTeTpDl8rLA_Aw8cK2qYOwXH9_5B8sDeSxvhk9WYeXxdznkbhTcJpVBKnSWiayZP0v-Wf9vaFjq8Z9YrK2F2aFyI52CP-7efzFis8N9LJKYNw11uoI6_cnEOlylkxT4BYMGVYmVtaQ52cp7V-D9ypwP7s66nMKbc0C8KBMJNroLYlEwqMHp7ay8kVkwYXIFC3npIifhLsXiFKNE8hRqUH4zPdN9IaQ_ob15If03pPcjPoI9WN1p3RfSNXhXoBS1VjbJ4cd02XbCaBnW04czk5B_Bz9AUaWYBXsxdiFFnl6K7OpMxKboSsY7RjvoKcj_AMaJVDb05i4IGlvR62gRvh7bqvDII4OchDOSWlOVj6gnv4rEOp3_mvT-bf7gMl0IinuLpKo0LDkS_AW9Dfeb3eJrF2dwCVkIpjhs5M_-DvToS-h7zUdkx2beBGPAOYgux1z4FtIlC0HSbr2FK8sBzu11Ei8DEttO34lVOXJ4m93nGr60ZLjDa92qAbunNctzSIDKlQcd7dYckCh17LbbcjIfM-kNNLQ4O7mN7iHymUck53uA7XpgNt0at9qwjJWAJZekCK_89UEj0Y_ViLNaI-moPMWzQ5ouufwJ7Ik7sfQijqU5M16nou_QimSVQGAJcPcEdge_AMez5c6OdKRruJToKc3YKGmg2R4bFtXUaNviNuwUDLndbo90iQu6qEP9dNHOJMYTRvQobA6XO0perBZCHbX8i_QT2kbqe7Qci_ZvVvpIBdkg_UYSNLfY3T3hFLRq4tN7RnV0EoZy_1_U1065N-Y3N5XPJyN2qPt6FyD6TKHkfp0l4txsm0mQX5edlEJJ5E4rzFgXt5ltxff7Oa2QcVuIQeWnnD7wyAhXlr5AAMb3GszlJdrICLdxDU3kObBL40TJ7Tk5w8EPxMTcVOQ8I2OnqAdWEojabZDJmSKjTZbfuzLDs1ssvSzRbWHMX0fQmfP2HuQZ1CAwY_A7VCT-Yloh1VsKFOwoqLM_4i3EpzdvLTodLqaX9NZmRR0_mQtiJTNmupx1t322nV7PXO8ZtBiRdQIet3t9Ky6Nn9VjxZ2l9DIO-VLTmNgSrhjyMBsROQnk_d4plrwwMy5iWHO68dJT5miwJCDx9eTzxtAZ9K5hIorP-XKouluahq2CbaLW0jf7bxinUluDshYFkKJ4ftF1rVovxJOw9djma3R57O4_LgG-IABuBgsH2vZXDNhE_fb8anCNS10Mtkna3pvugXfwGoSJG1m7QdcmX8YJ8f5lW8-YFPOjoXG4wsVuLwPfuZWndNKlQQg6BNaJVb4q5Q62AQULzbRHXba5kUj3fiksDo2WPgzEaJnLWxF2FA4EzmhoQdqchBqZkmeA1kGTkLZcXY8CehuUTX8EFDmgoJyt9hoUbtIe9HJV8HuIxIQDevlSIFlm6xe9V6cmniYEt-zLAFwxxZbw" 

#             # Local path to the image file
# local_image_path = pathlib.Path("C:\\Users\\darpa\\OneDrive\\Desktop\\MemeEngine Clone\\MemeEngine\\backend\\output_image.png")

#             # Desired path in your Dropbox (e.g., /my_images/uploaded_image.jpg)
# dropbox_target_path = "/Test/uploaded_image.jpg"


# #####################
# try:
#         # Initialize Dropbox client
#         dbx = dropbox.Dropbox(dropbox_access_token)

#         # Open the image file in binary read mode
#         with local_image_path.open("rb") as f:
#             # Upload the file
#             meta = dbx.files_upload(f.read(), dropbox_target_path, mode=dropbox.files.WriteMode("overwrite"))
#             print(f"File uploaded successfully: {meta.name} ({meta.size} bytes)")
# ##################################



# except dropbox.exceptions.ApiError as err:
#         print(f"*** API error: {err}")
# except Exception as err:
#         print(f"*** Other error: {err}")


#Clean local image file
# file_to_delete = "C:\\Users\\darpa\\OneDrive\\Desktop\\MemeEngine Clone\\MemeEngine\\backend\\output_image.png"
# os.remove(file_to_delete)
# ######
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
        print(direct_url)
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
time.sleep(5) 

image_url = get_image_url(image_path)
if image_url:
    shared_url = image_url[:-4] + "raw=1"
    direct_url = shared_url
    print(f"Direct image URL: {direct_url}")
else:
    print("Could not retrieve image URL.")
    direct_url = None  # Prevent further errors
    
    
url = f"https://graph.facebook.com/v23.0/{ig_user_id}/media"

# Parameters
params = {
    "image_url": direct_url,   # Publicly accessible URL

    "caption": ""+ latest_meme['meme_caption'] + " " + "".join(latest_meme['hashtags']),
    "access_token": access_token
}

# Send POST request
response = requests.post(url, data=params)
            


data = response.json()
print(data)


creation_id = data['id']

# The creation_id returned from the first request
# creation_id = "MEDIA_CREATION_ID_FROM_STEP_1"

publish_url = f"https://graph.facebook.com/v23.0/{ig_user_id}/media_publish"

publish_params = {
    "creation_id": creation_id,
    "access_token": access_token
}

# Send POST request
publish_response = requests.post(publish_url, data=publish_params)
print(publish_response.json())
print("Your post is live now!")
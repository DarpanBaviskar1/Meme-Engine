import dropbox
import pathlib

            # Replace with your actual access token
dropbox_access_token = "YOUR_DROPBOX_ACCESS_TOKEN"
            # Local path to the image file
local_image_path = pathlib.Path(r"C:\Users\darpa\OneDrive\Desktop\darpan\darpan\output_image.png")

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

except dropbox.exceptions.ApiError as err:
        print(f"*** API error: {err}")
except Exception as err:

        print(f"*** Other error: {err}")

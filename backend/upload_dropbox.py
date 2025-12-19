import dropbox
import pathlib

            # Replace with your actual access token
dropbox_access_token = "sl.u.AGDr7x3eS96txWka8wsknjvDc8LJ7YVpOUdN2VpjvdktxONUSiz0_4iIReOYLhkjJmGiuU75RqWGkZwzMU816sh2k60adSmXAJtdbFT1g99k3VypsovIxA0zA7QaQVPDGkhCVwr-zwfTEqqXe4VUlYB56d_Pl27V9OKlmmFaFpfkrkwEeIcop7aE0MTqfghgWS45VaOxTeDdIWTmSB5gyqRv698YSv0djZAi5EcmL0lk1eP8PmpCYPz4YhpGmYIeQheFIHf5UD6JRK9Zc4te7O_QPJcmCPXOYUvuxbVy4QfPSL1ekOvDp2wL5wt1GUi4z-B5h_V9L7waKgsT-QuPNKNqmCCZle88a468i-1GpzoVIc3jECntR7vq8_4abntrtMC6uTpzLOmTwZqljK30b50myRbuuC_kRzZ49jQn06g2sIGpRXOD4xpk4fxx7GJGhUfkg2zhkIhUDtYsa9aTarM3ydSTJ2afUT1Ef02oXMt-uq82tuShCOqZ2pHmiy6_799eAKa3ipzogKXnk_WffhBs1w87taXWZPqD58GtzgXuKQsxpHP38sk4IP2ZmuN0eggIcbTT8m5Q3NuxTlHn1_QBn3XzwugIfSRBVKgBK7h_3fiKtM4_6AuE3mg1nHX8l-CLjiLk2X0xWOkhgX6d61WZyCMOKNtB90J1DogD7EhdBCJQmFnJlvtQ8bZynpuCWclpKVB49Bfk-SsN7zGMNfynHEoOHIrV-vt6cyeG3r0DlgXK5CPOclW1HmlRBzhjv1BBltX-KPxIFOVg6KDSAhEnQZG2I-knugTf6icCHtBr0n4K8b1MCgf669y7WJlzzSppJmRog-IU_V3nw4ocn7ZhdiAl-q8RUXgIi_PqXIXSae8_XJqtqx7hYHm5wepxhvI7YhG4wZ1xYcMexSO71-XqVoYxK4aEjBh2lvgx2W3XIp7ScyHdv6MxRMk7D3GzPE594nYqLp4R1UrLp5Q-LZmV5rVSBkJfHN0Lb5e4Elk4C-I4C7TT2xI4crWExvF8S7nCdNTkqLplQmVyy9Wmd5cu4sFO4cLVmDYDNu2jCcNRfXYtiVscB_4owvzNDPkbS8jepDk8dnMrt7uC3ynkZxUhRnk8i5IzxM85RB7GfKsmVKAFwK3GoGlrKMk_3qA44fwpHUBXPrakO41F3rXhGhPxVzENBUcl28ALAnYNScLdwZjdvt8OVH9akjtlHujHSKIfRWKmeUG0vN5R1SJquG6pRhqZ1rtxuMaFT73R46uF172L6NxxFgRxTBpqi32O7g9rI2S-MyS-1nilcvGrVXAZkFOv7NTg5d4sNdKNo4tLBTdFSy6GqmkvM2ixHcSyfI7FCwJRb08JA1IrvD_CGJ2m9JK1nXfQ0vtdrp5irn_tKe7z3HNOhc37TM6BME_j0-_EHSgG8C9Eh6_z7qyS8Yoj8mLYlNqJEGdiWKP2CRerGg" 

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
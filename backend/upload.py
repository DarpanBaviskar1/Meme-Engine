import dropbox
import pathlib

            # Replace with your actual access token
dropbox_access_token = "sl.u.AF88diNS1nY1mc8TRo6Yzv41C_An24IBx4gZbCXbODxkoAdoIez2_oUOJydHHGNo1DmqjuJCka1IaVjn5ax2kaUFbs3a0c20JK3O4rJmci2ROEy4_dHQT_9unPL9WEnlGmOAYiaPG-huSoXOuExq8ivDh2kNW3Oug0VJFZTDvVfdDxpidmlZLJco_I1ZsgkZ1LcdrzDM7aAh22k13YDL0VKqbXLpTLlDacdNT9Q47Zc6_2vPxbII_uzttku8ZCfbiaVOAFotpmDO2QKOBtxMCgFHe2Ek3PNm3yVoL4QB0LBYxd5g8EGKLVuoQaO4sxoMX90OCrcl_z44mD5ve41ss44a55gvw67DJBdRZafZp844Ooe8kQg9txjxHvURgKhWVBhDQu_GZIDyYFUuJWS2axU7fxHQK4PzlpyTT9Un6eAuPS4269ux98C3wAaakPZbm_VBwVE-uiOXqsnke8mY2e2j45UoSwL4ubM5vkTv82GVnY46kOPhIrefi_oKYfa3LAa7JmbSNSemEoN22pEX5L7MPsRozpoM42rs8h_jkBhsoY0uThvnWYg26Aup51I6yvXYLPFvFN5cZvttzcem7mum8oeMrrJoqn84dRHhu5xxqvnEqgguNLaegyJ_ra5b1C5kL-n4MaaVZF5dhbJcWNo_CNA1mThxIpeZ3dfmsNZb7eJcLdVdJNNoSWzhGpHBYI6Y9JVPUJhgDmQ1HK8nl6AhZOB86vpqMdPXH7I4mCfTDji3Av74MO6IVkSOpg1jIOEibU0Cg_l38cOQrroy1s7L48G4AylCL1K4_gfg0tMLhgGxJtAdwrZWAvOn1EBjlPYHddTZ53VgUoPV_CVEk3q8_vn4DR4KPZkjyx6tz1roQw58aaH2k9xLvMyqFqkG0kUzc9wmiZJz0AoRwxNMHL3cJrrGScRO62cDQSxS5A7Db8-R589Wz2weOKS8OSOsx5jS_z5iyXWW3s6iakwZPDbUvjbJkPf24ai5gS-JoVI6xZ65YNmp0zrqy5G2nB09ogZbf5oYqb9czH-3td4nkQvjaiWf5tOHkHyo8QVwr8eDPtcXzVAOKba4NRy1C6Xhkzp6mvTOhLIXyjZUVCaYagtzIV3yYCTpFtaduM5jgkxPjbnmgGolctvzur5x8vtIP_Hzn4jDIJkAzvvCzKWNZiVeYLpqU_ieVokS0dd5FzhiMGR_mpni_0d3n-hPeLuAq5aKZk0LQ8KY4T2WA6EuLziD3vUT6M8BC1HoErY2gtfLOSaLZ-eEFezsGLzSKUpXmcsN1lWxQaX7Rqb35mSN5NVxeXeZ1C6DcMp14vNRuY7rEgdc1bynbLq32frAJFVA1YAcotZOLPViFhB4LBNHS0gBm5o2YEzpxdqgKc8JuS-jbVZhayQYDFOgpwqrE9nH2z-dmD6V8F6eCBcOTNekvSrkskRS5QNxcxPLo3EMnWI0jQ" 

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
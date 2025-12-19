import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

class ImageApprovalApp:
    def __init__(self, root, image_url):
        self.root = root
        self.root.title("Image Approval System")

        # Fetch image from URL
        response = requests.get(image_url)
        img_data = response.content
        pil_image = Image.open(BytesIO(img_data))

        # Resize image if too large for window
        max_size = (500, 500)
        pil_image.thumbnail(max_size)

        # Convert to ImageTk
        self.img = ImageTk.PhotoImage(pil_image)
        
        # Display image
        self.label = tk.Label(root, image=self.img)
        self.label.pack(pady=10)

        # Approve and Disapprove buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        approve_btn = tk.Button(btn_frame, text="Approve", width=10, command=self.approve)
        approve_btn.pack(side=tk.LEFT, padx=10)

        disapprove_btn = tk.Button(btn_frame, text="Disapprove", width=10, command=self.disapprove)
        disapprove_btn.pack(side=tk.LEFT, padx=10)

    def approve(self):
        messagebox.showinfo("Result", "Image approved!")
        self.root.quit()

    def disapprove(self):
        messagebox.showinfo("Result", "Image disapproved!")
        self.root.quit()

if __name__ == "__main__":
    url = "https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_16x9.jpg?w=1200"  # Replace with your image URL
    root = tk.Tk()
    app = ImageApprovalApp(root, url)
    root.mainloop()

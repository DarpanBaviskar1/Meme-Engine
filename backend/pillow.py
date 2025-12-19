from PIL import Image, ImageDraw, ImageFont

def make_meme(template_path, top_text, bottom_text, output_path, font_path="arial.ttf"):
    # Open the template image
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)
    width, height = img.size

    # Load a font (adjust size as needed)
    font_size = int(height / 10)
    font = ImageFont.truetype(font_path, font_size)

    # Helper to center text
    def draw_text_centered(text, y):
        text = text.upper()
        text_width, text_height = draw.textsize(text, font=font)
        x = (width - text_width) / 2
        # Add black outline for readability
        draw.text((x-2, y-2), text, font=font, fill="black")
        draw.text((x+2, y-2), text, font=font, fill="black")
        draw.text((x-2, y+2), text, font=font, fill="black")
        draw.text((x+2, y+2), text, font=font, fill="black")
        draw.text((x, y), text, font=font, fill="white")

    # Draw top and bottom text
    if top_text:
        draw_text_centered(top_text, 10)
    if bottom_text:
        draw_text_centered(bottom_text, height - font_size - 10)

    img.save(output_path)

def overlay_caption_on_base64_image(img_b64, caption, font_path="arial.ttf"):
    import base64
    from io import BytesIO
    img_data = base64.b64decode(img_b64)
    img = Image.open(BytesIO(img_data))
    draw = ImageDraw.Draw(img)
    width, height = img.size
    font_size = int(height / 10)
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()
    # Centered text at bottom
    text = caption.upper()
    text_width, text_height = draw.textsize(text, font=font)
    x = (width - text_width) / 2
    y = height - text_height - 10
    # Draw outline for readability
    for dx in [-2, 2]:
        for dy in [-2, 2]:
            draw.text((x+dx, y+dy), text, font=font, fill="black")
    draw.text((x, y), text, font=font, fill="white")
    # Save to base64
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8") 
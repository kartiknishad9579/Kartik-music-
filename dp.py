import os
import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pyrogram import Client, filters
from pyrogram.types import Message
import requests
import io

# Fonts download karne ke liye
FONT_URL = "https://github.com/google/fonts/raw/main/ofl/pacifico/Pacifico-Regular.ttf"

def get_font():
    if not os.path.exists("font.ttf"):
        r = requests.get(FONT_URL)
        with open("font.ttf", "wb") as f:
            f.write(r.content)
    return "font.ttf"

@Client.on_message(filters.command("name_dp"))
async def name_dp_cmd(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply("**Naam to likh bhai!**\nEx: `/name_dp Kartik`")

    name = " ".join(message.command[1:]).upper()
    if len(name) > 15:
        return await message.reply("**Naam 15 letters se chhota rakh 😅**")

    m = await message.reply("**DP Bana Raha Hu... ⏳**")

    try:
        # 1. Background banate hain - Gradient
        img = Image.new('RGB', (1080, 1080), color='black')
        draw = ImageDraw.Draw(img)

        # Gradient colors
        colors = [
            [(255, 0, 150), (0, 150, 255)], # Pink-Blue
            [(255, 150, 0), (255, 0, 150)], # Orange-Pink
            [(0, 255, 150), (0, 150, 255)], # Green-Blue
            [(150, 0, 255), (255, 0, 150)], # Purple-Pink
        ]
        color1, color2 = random.choice(colors)

        for y in range(1080):
            r = int(color1[0] + (color2[0] - color1[0]) * y / 1080)
            g = int(color1[1] + (color2[1] - color1[1]) * y / 1080)
            b = int(color1[2] + (color2[2] - color1[2]) * y / 1080)
            draw.line([(0, y), (1080, y)], fill=(r, g, b))

        # 2. Blur effect
        img = img.filter(ImageFilter.GaussianBlur(5))
        draw = ImageDraw.Draw(img)

        # 3. Circle banate hain center me
        circle_img = Image.new('RGBA', (800, 800), (0, 0, 0, 0))
        circle_draw = ImageDraw.Draw(circle_img)
        circle_draw.ellipse([(0, 0), (800, 800)], fill=(255, 255, 255, 40))

        # Glass effect ke liye
        circle_img = circle_img.filter(ImageFilter.GaussianBlur(10))
        img.paste(circle_img, (140, 140), circle_img)

        # 4. Text likhte hain
        font_big = ImageFont.truetype(get_font(), 120)
        font_small = ImageFont.truetype(get_font(), 40)

        # Name center me
        draw.text((540, 480), name, font=font_big, fill='white', anchor='mm', stroke_width=3, stroke_fill='black')

        # Watermark
        draw.text((540, 600), "KARTIK X MUSIC", font=font_small, fill=(255, 255, 255, 180), anchor='mm')

        # 5. Border
        draw.ellipse([(130, 130), (950, 950)], outline='white', width=8)

        # Save karo
        bio_img = io.BytesIO()
        bio_img.name = f"{name}_dp.jpg"
        img.save(bio_img, "JPEG", quality=95)
        bio_img.seek(0)

        await message.reply_photo(
            bio_img,
            caption=f"**✨ Name DP Ready ✨**\n\n**Name:** `{name}`\n**By:** @KartikXMusicBot"
        )
        await m.delete()

    except Exception as e:
        await m.edit(f"**Error:** `{e}`\n\nPillow install hai? `pip install pillow`")

import random # ye upar add kar dena imports me

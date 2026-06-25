import random
from pyrogram import Client, filters
from pyrogram.types import Message

SHAYARI_LIST = [
    "Mohabbat ka junoon jab had se badh jata hai,\nTabhi to aashiq deewana kehla jata hai ❤️",
    
    "Tere chehre me mera noor hoga,\nPhir tu na kabhi mujhse door hoga 💫",
    
    "Zindagi ki raah me gum naam ke bhi hote hain,\nKabhi milte nahi ye jaam ke bhi hote hain 🥀",
    
    "Dil se teri yaad na jaye to kya karun,\nTu hi bata tujhe yaad na aaye to kya karun 💔",
    
    "Kismat se apni sab shikayat karte hain,\nHum to dard me bhi mohabbat karte hain 🌙",
    
    "Tere ishq me hum itna kho gaye,\nKhud ko dhundte dhundte tere ho gaye 🦋",
    
    "Aankhon me nami si hai, tere intezaar me,\nBaitha hu tanha mai, teri hi pyaar me 🌧️",
    
    "Wafa ki baat karte ho, bewafa ho gaye ho tum,\nMere dil ko tod ke, kisike ho gaye ho tum 💘",
    
    "Chand se chehra, chandni si baatein,\nTeri yaadon me guzar gayi saari raatein ✨",
    
    "Ishq adhura hai tere bagair,\nZindagi sooni hai tere bagair 🥺",
    
    "Teri hasi meri pehchaan hai,\nTeri khushi meri jaan hai 😊",
    
    "Mohabbat karne walo ka dil toda nahi karte,\nJisse pyaar ho usse chhoda nahi karte 💯",
    
    "Raat bhar karvat badalta raha mai,\nTeri yaad me jaltaa raha mai 🔥",
    
    "Dosti ka rishta anmol hota hai,\nJo har pal khushiyon me dhol hota hai 👬",
    
    "Tanha raat me tera khayal aata hai,\nDil me ek dard sa jagata hai 🌃"
]

@Client.on_message(filters.command("shayari"))
async def shayari_cmd(client: Client, message: Message):
    shayari = random.choice(SHAYARI_LIST)
    await message.reply_text(f"**🦋 Shayari For You 🦋**\n\n`{shayari}`\n\n__By: Kartik X Music__")

@Client.on_message(filters.command("love"))
async def love_shayari(client: Client, message: Message):
    love_list = [
        "Tum mile to laga zindagi mil gayi,\nTum na mile to zindagi kya cheez hai ❤️",
        "Pyaar kya hai ye tumse seekha hai,\nIshq kya hai ye tumse jana hai 💕",
        "Meri har saans me tera naam hai,\nMeri har dua me tera paigaam hai 💌"
    ]
    await message.reply_text(f"**💘 Love Shayari 💘**\n\n`{random.choice(love_list)}`")

@Client.on_message(filters.command("sad"))
async def sad_shayari(client: Client, message: Message):
    sad_list = [
        "Dard jab had se guzar jata hai,\nInsaan phir pathar ban jata hai 💔",
        "Rote rote ye raat guzar jayegi,\nPar teri yaad na guzar payegi 😢",
        "Tanha hoon is bheed me,\nKoi apna nahi hai is shehar me 🥀"
    ]
    await message.reply_text(f"**💔 Sad Shayari 💔**\n\n`{random.choice(sad_list)}`")

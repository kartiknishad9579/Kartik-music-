import os
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio
import yt_dlp

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
STRING_SESSION = os.environ.get("STRING_SESSION")

app = Client("KartikMusicBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
userbot = Client("KartikUserBot", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)
call_py = PyTgCalls(userbot)

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/%(id)s.%(ext)s',
    'quiet': True,
    'no_warnings': True,
}

@app.on_message(filters.command("start"))
async def start_cmd(_, message: Message):
    await message.reply_text("**Kartik Music Bot 🎵**\n\n/play <song name> - VC me gaana bajane ke liye\n/stop - Gaana band\n/pause - Pause\n/resume - Resume")

@app.on_message(filters.command("play"))
async def play_cmd(_, message: Message):
    if len(message.command) < 2:
        return await message.reply("Gaane ka naam to de bhai. Ex: `/play kesariya`")

    query = " ".join(message.command[1:])
    m = await message.reply(f"**Searching:** `{query}`")

    chat_id = message.chat.id

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
        except:
            return await m.edit("**Gaana nahi mila 😕**")

    title = info['title']
    url = info['url']
    duration = info['duration']

    await m.edit(f"**Playing:** `{title}`\n**Duration:** `{duration//60}:{duration%60}`")

    try:
        await call_py.join_group_call(
            chat_id,
            AudioPiped(url, HighQualityAudio()),
        )
    except Exception as e:
        await m.edit(f"**Error:** VC start hai kya? Mujhe admin bana\n`{e}`")

@app.on_message(filters.command(["stop", "end"]))
async def stop_cmd(_, message: Message):
    try:
        await call_py.leave_group_call(message.chat.id)
        await message.reply("**Stopped ✅**")
    except:
        await message.reply("**Kuch baj hi nahi raha tha**")

@app.on_message(filters.command("pause"))
async def pause_cmd(_, message: Message):
    try:
        await call_py.pause_stream(message.chat.id)
        await message.reply("**Paused ⏸**")
    except:
        await message.reply("**Gaana chal hi nahi raha**")

@app.on_message(filters.command("resume"))
async def resume_cmd(_, message: Message):
    try:
        await call_py.resume_stream(message.chat.id)
        await message.reply("**Resumed ▶️**")
    except:
        await message.reply("**Pehle pause to karo**")

async def start_bot():
    await app.start()
    await userbot.start()
    await call_py.start()
    print("Kartik Music Bot Started!")
    await app.idle()

if __name__ == "__main__":
    import asyncio
    asyncio.run(start_bot())

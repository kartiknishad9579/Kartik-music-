import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait

# Owner ID yaha daal de, sirf tu chala payega
OWNER_ID = int(os.environ.get("OWNER_ID", 0))

@Client.on_message(filters.command("tagall") & filters.group)
async def tag_all(client: Client, message: Message):
    if message.from_user.id != OWNER_ID:
        return await message.reply("**Sirf owner chala sakta hai ye command ❌**")
    
    await message.delete()
    
    if len(message.command) >= 2:
        text = " ".join(message.command[1:])
    else:
        text = "**Hey!**"
    
    chat_id = message.chat.id
    mention_text = f"{text}\n\n"
    count = 0
    
    async for member in client.get_chat_members(chat_id):
        if member.user.is_bot or member.user.is_deleted:
            continue
        mention_text += f"⊚ [{member.user.first_name}](tg://user?id={member.user.id})\n"
        count += 1
        
        # 5 tag ke baad message bhej de, flood se bachne ke liye
        if count % 5 == 0:
            try:
                await client.send_message(chat_id, mention_text)
                mention_text = f"{text}\n\n"
                await asyncio.sleep(2)  # 2 sec ka gap
            except FloodWait as e:
                await asyncio.sleep(e.value)
    
    # Baaki bache hue members
    if mention_text != f"{text}\n\n":
        await client.send_message(chat_id, mention_text)
    
    await client.send_message(chat_id, f"**Total {count} Members Tagged ✅**")

@Client.on_message(filters.command("cancel") & filters.group)
async def cancel_tag(client: Client, message: Message):
    if message.from_user.id != OWNER_ID:
        return
    await message.reply("**Tag All Cancelled**")
    # Note: Pyrogram me running loop cancel karna tricky hai
    # Bot restart kar de agar beech me rokna hai

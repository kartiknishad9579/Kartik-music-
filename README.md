# 🎵 Kartik Music Bot

Telegram Group Voice Chat me YouTube se gaane bajane wala bot. Railway pe 1-click deploy hota hai.

### ✨ Features
- `/play <song name>` - YouTube se gaana search karke VC me bajayega
- `/stop` - Gaana band karo
- `/pause` - Gaana pause karo  
- `/resume` - Gaana wapas chalu karo
- High Quality Audio support
- UserBot + Bot combo - Ban ka risk kam

### 🚀 Deploy to Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template)

**Manual Deploy Steps:**

1. **Fork This Repo** ya saare files copy karke apna repo bana le

2. **Requirements Banaye**
   - **BOT_TOKEN**: [@BotFather](https://t.me/BotFather) se naya bot banake token le
   - **API_ID & API_HASH**: https://my.telegram.org se nikale
   - **STRING_SESSION**: Userbot ke liye session. Replit me ye code chala:
   ```python
   from pyrogram import Client
   API_ID = 12345
   API_HASH = "your_hash"
   with Client("Kartik", API_ID, API_HASH) as app:
       print(app.export_session_string())

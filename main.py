from telethon import TelegramClient, events
import yt_dlp
import os

# 🔹 Replace these with your API details
API_ID = "1400991"
API_HASH = "e781477beae59ec94dd73d1bb9303c8b"
BOT_TOKEN = "7975029749:AAEEsb4zVjcF6ys2s879CBhbGUD7UlUtSiI"

client = TelegramClient("bot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Function to download YouTube videos
def download_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'video.mp4',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Handle messages with YouTube links
@client.on(events.NewMessage)
async def handler(event):
    message = event.message.text

    if "youtube.com" in message or "youtu.be" in message:
        await event.reply("🔄 Downloading your video, please wait...")

        try:
            download_video(message)
            await client.send_file(event.chat_id, "video.mp4")
            os.remove("video.mp4")  # Delete the file after sending
        except Exception as e:
            await event.reply("❌ Failed to download the video.")
            print("Error:", e)

client.run_until_disconnected()

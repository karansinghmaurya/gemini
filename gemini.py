import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8344010103:AAFRJHcm1BfI3TEWf4emhN9_y3AE8O1YaL0"

CHAT_API = "https://api.affiliateplus.xyz/api/chatbot?message={msg}&botname=AI&ownername=User"
IMAGE_API = "https://api.affiliateplus.xyz/api/imagegen?text={msg}&type=neon"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    # Chat API
    res = requests.get(CHAT_API.format(msg=user_text))
    data = res.json()
    reply = data.get("message", "Error aaya 😢")

    await update.message.reply_text(reply)

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot chal raha hai 🚀...")
    app.run_polling()

if __name__ == "__main__":
    main()
if user_text.startswith("/img"):
    text = user_text.replace("/img ", "")
    img_url = IMAGE_API.format(msg=text)
    await update.message.reply_photo(img_url)
    return


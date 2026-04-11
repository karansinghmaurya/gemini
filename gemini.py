import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

# Tokens
GEMINI_KEY = "AIzaSyDzIN_g46eu2JhU0vOeOPtioQ_GkHTtBgk"
TG_TOKEN = "8344010103:AAFRJHcm1BfI3TEWf4emhN9_y3AE8O1YaL0"

# AI Setup
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-pro')

# /start command ke liye function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Stylish Font (Unicode text)
    welcome_text = "✨ 𝑴𝒂𝒅𝒂𝒎 𝒋𝒊 ✨\n\nMain aapki kaise madad kar sakta hoon?"
    await update.message.reply_text(welcome_text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    response = model.generate_content(user_text)
    await update.message.reply_text(response.text)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TG_TOKEN).build()
    
    # Start handler pehle add karein
    app.add_handler(CommandHandler("start", start))
    
    # Message handler
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    print("Bot chalu hai... Madam ji ke liye tayyar!")
    app.run_polling()



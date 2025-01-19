import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Bot Token
BOT_TOKEN = "7637067404:AAF_5aH3zfbJTGHTNiZlw0v99nRTT6cT3Jo"
bot = telebot.TeleBot(BOT_TOKEN)

# Your links
OWNER_LINK = "https://t.me/GOD_ALEN"  # Replace with your Telegram ID or username
CHANNEL_LINK = "https://t.me/gtmopbolte"  # Replace with your Channel link

# Start Command Handler
@bot.message_handler(commands=["start"])
def send_welcome(message):
    # Main menu
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("Gates 🌤", callback_data="gates"),
        InlineKeyboardButton("Channel 🌤", url=CHANNEL_LINK),
        InlineKeyboardButton("Owner ⚡", url=OWNER_LINK),
        InlineKeyboardButton("Exit ⚠️", callback_data="exit")
    )
    bot.send_message(
        message.chat.id,
        "🌟 Greetings from Hitter!\n"
        "🌸 Unleash the Power of Hitter:\n"
        "Your Gateway to ⚡ Fast and 🔒 Safe Checkups with Exceptional Tools at Your Fingertips!\n\n"
        "🤖 Bot Version => 1.0",
        reply_markup=markup
    )

# Callback Handler for Buttons
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "gates":
        send_gates_menu(call.message)
    elif call.data == "auth":
        send_auth_section(call.message)
    elif call.data == "exit":
        bot.send_message(call.message.chat.id, "Exiting... Bye!")
    else:
        bot.answer_callback_query(call.id, "Invalid option!")

# Gates Menu
def send_gates_menu(message):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Auth", callback_data="auth"),
        InlineKeyboardButton("Exit ⚠️", callback_data="exit")
    )
    bot.send_message(
        message.chat.id,
        "Welcome »\n\n"
        "Total Gates => 1\n"
        "Gates On => 1\n"
        "Gates Off => 0\n"
        "Gates Maintenance => 0\n\n"
        "Auth => 1\n"
        "Charged => 0\n"
        "Special => 0\n"
        "Shopifys => 0\n\n"
        "Please choose the gate that suits your needs from the menu!",
        reply_markup=markup
    )

# Auth Section
def send_auth_section(message):
    # Replace the placeholder text with actual content and image
    bot.send_message(message.chat.id, "Displaying the Auth Section...")
    # To display a photo:
    # with open("path_to_image.jpg", "rb") as photo:
    #     bot.send_photo(message.chat.id, photo)

# Check Command (Uses gatet.py)
@bot.message_handler(commands=["check"])
def check_gate(message):
    try:
        # Execute gatet.py
        exec(open("gatet.py").read())
        bot.send_message(message.chat.id, "Executed gatet.py successfully!")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error executing gatet.py: {e}")

# Polling the bot
print("Bot is running...")
bot.infinity_polling()
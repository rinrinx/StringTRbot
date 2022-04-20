from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

If you don't trust this bot, 
1) stop reading this message
2) delete this chat

Still reading?
You can use me to generate pyrogram and telethon string session. Use below buttons to learn more !

By @kamileecherch
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton("✨ More Bots ✨", url="https://t.me/kamileecherch")],
        [
            InlineKeyboardButton("Command Bot ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ Admin ♥", url="https://t.me/kamileecher")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
**About Bot**
    """

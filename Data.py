from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
ʜᴇʏ {}

ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {}

ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴄʜᴀɴɴᴇʟꜱ ᴡɪᴛʜ ᴛᴏɴꜱ ᴏꜰ ꜰᴇᴀᴛᴜʀᴇꜱ. ᴜꜱᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ !

ʙʏ @HNYROBO

    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("ʙᴏᴛ ꜱᴛᴀᴛᴜꜱ ᴀɴᴅ ᴍᴏʀᴇ ʙᴏᴛꜱ", url="https://t.me/hnyrobo/9")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜꜱᴇ", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ],
        [InlineKeyboardButton("ᴍᴏʀᴇ ᴀᴍᴀᴢɪɴɢ ʙᴏᴛꜱ", url="https://t.me/hnyrobo")],
        [InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="https://t.me/hnyxcandy_support")],
    ]

    # Help Message
    HELP = """
Everything is self explanatory after you add a channel.
To add a channel use keyboard button 'Add Channels' or alternatively for ease, use `/add` command

✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot

Alternative Commands
/channels - List added Channels
/add - Add a channel
/report - Report a Problem
    """

    # About Message
    ABOUT = """
**ᴀʙᴏᴜᴛ ᴛʜɪꜱ ʙᴏᴛ** 

ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ ᴀᴜᴛᴏᴍᴀᴛɪᴏɴ ʙᴏᴛ 

ᴜᴘᴅᴀᴛᴇꜱ : @HNYOP

ꜰʀᴀᴍᴇᴡᴏʀᴋ : [ᴘʏʀᴏɢʀᴀᴍ](ᴅᴏᴄꜱ.ᴘʏʀᴏɢʀᴀᴍ.ᴏʀɢ)

ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](ᴡᴡᴡ.ᴘʏᴛʜᴏɴ.ᴏʀɢ)

ᴅᴇᴠᴇʟᴏᴘᴇʀ : @HNYOP
    """

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from VenomX import app as bot
import requests
from config import OWNER_ID
from VenomX.utils.errors import capture_err

start_txt = """**
➤ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴍʏ ᴡᴏʀʟᴅ ᥫᩣ
 
 ⦿ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ɴ ᴠᴘs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ !
 
 ⦿ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ !
 
 ⦿ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ !
 
 ⦿ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴅᴍ ᴍᴇ !
**"""

@bot.on_message(filters.command(["repo"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("⦿ ᴀᴅᴅ ᴍᴇ ⦿", url="https://t.me/BWF_MUSIC1"),
        ],
        [
          InlineKeyboardButton("⛩️ʜᴇʟᴘ🦋", url="https://t.me/BWF_MUSIC1"),
          InlineKeyboardButton("🔥 ᴏᴡɴᴇʀ 🔥", url="https://t.me/L2R_KING"),
        ],
        [
          InlineKeyboardButton("💒ʙωғ sᴜᴘᴘᴏʀᴛ💒", url=f"https://t.me/BWF_MUSIC1"),
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/e576aa8308c49d945f433.jpg",
        caption=start_txt,
        reply_markup=reply_markup,
    )



#-------------------------------------------------------#


@bot.on_message(filters.command("repo", prefixes="@"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/stkeditz/AAROHIxMUSICv2/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[ʀᴇᴘᴏ](https://telegra.ph/file/e576aa8308c49d945f433.jpg) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/BWF_MUSIC1)
| ᴄᴏɴᴛʀɪʙᴜᴛᴏʀs |
----------------
{list_of_users}"""
        await bot.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await bot.send_message(message.chat.id, text="Failed to fetch contributors.")

from telegraph import upload_file
from pyrogram import filters
from VenomX import app
from pyrogram.types import InputMediaPhoto

### ❖ ➥ 𝗕𝐖𝗙™🇮🇳
@app.on_message(filters.command(["tgm" , "telegraph"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("💌ʙω͠ғ™ ɪᴍᴀɢᴇs🦋")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f'💌ʙω͠ғ™ ʟɪɴᴋ ɪᴍᴀɢᴇs🦋 {url}')

########____________________________________________________________######

@app.on_message(filters.command(["graph" , "grf"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("💌ʙω͠ғ™ ɪᴍᴀɢᴇs🦋")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://graph.org" + x

        i.edit(f'💌ʙω͠ғ™ ʟɪɴᴋ ɪᴍᴀɢᴇs🦋 {url}')

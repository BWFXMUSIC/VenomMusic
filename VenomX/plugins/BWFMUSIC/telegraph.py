from telegraph import upload_file
from pyrogram import filters
from VenomX import app
from pyrogram.types import InputMediaPhoto

@app.on_message(filters.command(["tgm", "telegraph"]))
async def ul(_, message):
    reply = message.reply_to_message
    if reply and reply.media:
        if not reply.photo:  # Check if the media is a photo or image
            return await message.reply("**ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋs ᴡɪᴛʜ ɪᴍᴀɢᴇs.**")
        
        i = await message.reply("💌ʙω͠ғ™ ɪᴍᴀɢᴇs🦋")
        path = await reply.download()  # Download the file
        
        # Upload the file to Telegraph
        try:
            fk = upload_file(path)
            url = "https://telegra.ph" + fk[0]  # Get the first URL from the list
            
            # Send the link back to the user
            await i.edit(f'💌ʙω͠ғ™ ʟɪɴᴋ ɪᴍᴀɢᴇs🦋 {url}')
        except Exception as e:
            await i.edit(f"Error uploading the image to Telegraph.\nError: {str(e)}")
        finally:
            # Clean up the downloaded file
            os.remove(path)

@app.on_message(filters.command(["graph", "grf"]))
async def ul(_, message):
    reply = message.reply_to_message
    if reply and reply.media:
        if not reply.photo:  # Check if the media is a photo or image
            return await message.reply("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋs ᴡɪᴛʜ ɪᴍᴀɢᴇs.")
        
        i = await message.reply("💌ʙω͠ғ™ ɪᴍᴀɢᴇs🦋")
        path = await reply.download()  # Download the file
        
        # Upload the file to Graph.org
        try:
            fk = upload_file(path)
            url = "https://graph.org" + fk[0]  # Get the first URL from the list
            
            # Send the link back to the user
            await i.edit(f'💌ʙω͠ғ™ ʟɪɴᴋ ɪᴍᴀɢᴇs🦋 {url}')
        except Exception as e:
            await i.edit(f"Error uploading the image to Graph.org.\nError: {str(e)}")
        finally:
            # Clean up the downloaded file
            os.remove(path)

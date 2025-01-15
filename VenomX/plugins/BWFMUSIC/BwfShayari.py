from VenomX import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋", "🧚🌸🧋🍬🫖", "🥀🌷🌹🌺💐", "🌸🌿💮🌱🌵", "❤️💚💙💜🖤", "💓💕💞💗💖", "🌸💐🌺🌹🦋", "🍔🦪🍛🍲🥗", "🍎🍓🍒🍑🌶️", "🧋🥤🧋🥛🍷", "🍬🍭🧁🎂🍡", "🍨🧉🍺☕🍻", "🥪🥧🍦🍥🍚", "🫖☕🍹🍷🥛", "☕🧃🍩🍦🍙", "🍁🌾💮🍂🌿", "🌨️🌥️⛈️🌩️🌧️", "🌷🏵️🌸🌺💐", "💮🌼🌻🍀🍁", "🧟🦸🦹🧙👸", "🧅🍠🥕🌽🥦", "🐷🐹🐭🐨🐻‍❄️", "🦋🐇🐀🐈🐈‍⬛", "🌼🌳🌲🌴🌵", "🥩🍋🍐🍈🍇", "🍴🍽️🔪🍶🥃", "🕌🏰🏩⛩️🏩", "🎉🎊🎈🎂🎀", "🪴🌵🌴🌳🌲", "🎄🎋🎍🎑🎎", "🦅🦜🕊️🦤🦢", "🦤🦩🦚🦃🦆", "🐬🦭🦈🐋🐳", "🐔🐟🐠🐡🦐", "🦩🦀🦑🐙🦪", "🐦🦂🕷️🕸️🐚", "🥪🍰🥧🍨🍨", " 🥬🍉🧁🧇"]
TAGMES = [ 
    "✨बहुत अच्छा लगता है तुझे सताना और फिर प्यार से तुझे मनाना।🍃", 
    "⚚•👁मेरी जिंदगी मेरी जान हो तुम मेरे सुकून का दुसरा नाम हो तुम।👻", 
    "🕊⃟♥️तुम मेरी वो खुशी हो जिसके बिना, मेरी सारी खुशी अधूरी लगती है।*🍃*", 
    "ᴛᴏᴏᴛᴇ 💔 ʜᴜʏᴇ ᴅɪʟ ɴᴇ ʙʜɪ ᴜsᴋᴇ", 
    "❤🥀अगर एक हारा हुआ इंसान◑❃हारने के बाद भी🌸🍃", 
    "🥀🍃मुस्कुरा दे....❁✥◓❤🌸🍃तो जितने वाला भी जीत कि खुशी खो देता है...!!🌸", 
    "🌸❤आंखों से अश्कों की बरसात हो गई✨", 
    "🥀गम की हमसे ऐसी मुलाकात हो गई🌸"
    # more items...
]
VC_TAG = [ 
    "🍷जिन लड़कियों ने मुझे माना किया है.....👁", 
    "🦋उनकी माँ बाप को फ़ोन करके.....💨", 
    "🙊उनकी @SHAYRI_CHANNEL1 लोकेशन बताऊँगा👻", 
    "💔👑🌷मालूम होती फ़ितर तुम्हारी तो हम इतना इश्क़ नहीं करते🍃🥀💌", 
    "🥀🌹🍃तुम जिस्म के शौकीन हों हमको कैसे समझते 💔🌸🍃", 
    "👀❣️🌸आँखें तो ठीक है मे  तो रूह तक रोयी है🍷🖇🎭", 
    "🌸🥀🍃𝐎𝐲𝐞𝐞 𝐭𝐞𝐫𝐞 𝐛𝐚𝐚𝐝 𝐡𝐮𝐦 𝐭𝐞𝐫𝐢 𝐭𝐫𝐡 𝐤𝐢𝐬𝐢 𝐤𝐨 𝐜𝐡𝐚𝐡𝐞𝐧𝐠𝐞 𝐧𝐡𝐢🫠❤️", 
    "❤दिल ना दुखायेंगे कभी..🎀 🍒ना छोड़ के जायेंगे🥀", 
    "♦️हर चीज से बडकर.💌🍷सिर्फ तुझको चाहेंगे.....👁", 
    "🍷बहुत उदास है कोई तेरे जाने से 👻", 
    "❣️हो सके तो लौट आ किसी बहाने से🦋", 
    "🍃तू लाख खफा सही, मगर एक बार तो देख 👑"
    # more items...
]

async def is_user_admin(client, chat_id, user_id):
    """Check if the user is an admin."""
    try:
        participant = await client.get_chat_member(chat_id, user_id)
        return participant.status in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER)
    except UserNotParticipant:
        return False

@app.on_message(filters.command(["Shayaritag", "Lovetag", "Pyartag", "shaaditag", "tagall", "all"], prefixes=["/", "@", "#"]))
async def mention_all(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")
    
    if not await is_user_admin(client, chat_id, message.from_user.id):
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ...")
    
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(TAGMES)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""

    spam_chats.remove(chat_id)

@app.on_message(filters.command(["vctag"], prefixes=["/", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")
    
    if not await is_user_admin(client, chat_id, message.from_user.id):
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ...")
    
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""

    spam_chats.remove(chat_id)

@app.on_message(filters.command(["cancel", "offtag", "Shayariofftag", "lovetag", "off", "offtag", "stop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠 𝐁𝐚𝐛𝐲.")
    
    if not await is_user_admin(client, message.chat.id, message.from_user.id):
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    
    spam_chats.remove(message.chat.id)
    return await message.reply("♦ ≛ 🄸🥂Gʀᴏᴜᴘꨄ︎[•ʙω͠ф•]™✺🕊️⃝🔥 ♦")

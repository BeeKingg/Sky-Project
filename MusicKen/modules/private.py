import logging
from MusicKen.modules.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from MusicKen.config import SOURCE_CODE, ASSISTANT_NAME, PROJECT_NAME, SUPPORT_GROUP, UPDATES_CHANNEL, BOT_USERNAME, OWNER

logging.basicConfig(level=logging.INFO)


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited 
)
async def start_(client: Client, message: Message):
        await message.reply_text(
        f"""๐๐ป Hallo, saya adalah [{PROJECT_NAME}] yang dapat memutar music dengan mudah di voice call group maupun channel.
Saya memiliki banyak fitur seperti : 
โโโโโโโโโโโโฆโโโโโโโโโโโ
โโ Memutar lagu di group 
โโ Memutar lagu di channel
โโ Mendownload lagu
โโ Mencari link youtube
โโโโโโโโโโโโฆโโโโโโโโโโโ
โโโโโโโโโโเผบเผปโโโโโโโโโโ
๐ฎ Dikelola oleh : @{OWNER}
โโโโโโโโโโเผบเผปโโโโโโโโโโ
โ๏ธ Klik tombol bantuan untuk informasi lebih lanjut.
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก สแดษดแดแดแดษด", callback_data = f"help+1"),
                    InlineKeyboardButton(
                        "โ แดแดแดสแดสแดแดษด โ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "๐ฐ ษขสแดแดแด", url=f"https://t.me/{SUPPORT_GROUP}"), 
                    InlineKeyboardButton(
                        "๐ฎ แดสแดษดษดแดส", url=f"https://t.me/{UPDATES_CHANNEL}")],
                [
                    InlineKeyboardButton("๐ ๐ณ๐พ๐ฝ๐ฐ๐๐ธ ๐", url=f"boyfriendnice")
                ]        
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""**๐ด {PROJECT_NAME} is online**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("๐ฐ sแดแดแดแดสแด แดสแดแด", url=f"https://t.me/{SUPPORT_GROUP}"),
                    InlineKeyboardButton("๐ฎ แดสแดษดษดแดส", url=f"https://t.me/{UPDATES_CHANNEL}")
                ]
            ]
        ),
    )


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = 'โฌ๏ธ Sebelummya', callback_data = "help+5"),
             InlineKeyboardButton(text = 'Selanjutnya โก๏ธ', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            [InlineKeyboardButton(text = '๐ก สแดษดแดแดแดษด', callback_data = f"help+1"),
             InlineKeyboardButton(text = 'โ แดแดแดสแดสแดแดษด โ', url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [InlineKeyboardButton(text = '๐ฐ ษขสแดแดแด', url=f"https://t.me/{SUPPORT_GROUP}"),
             InlineKeyboardButton(text = 'แดสแดษดษดแดส ๐ฎ', url=f"https://t.me/{UPDATES_CHANNEL}")],
            [InlineKeyboardButton("๐ ๐ณ๐พ๐ฝ๐ฐ๐๐ธ ๐", url=f"boyfriendnice")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = 'โฌ๏ธ sแดสแดสแดแดษดสแด', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = 'sแดสแดษดแดแดแดษดสแด โก๏ธ', callback_data = f"help+{pos+1}")
            ],
        ]
    return button

@Client.on_message(
    filters.command("reload")
    & filters.group
    & ~ filters.edited
)
async def reload(client: Client, message: Message):
    await message.reply_text("""โ Bot **berhasil dimulai ulang!**\n\nโข **Daftar admin** telah **diperbarui**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฐ GROUP", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "๐ฉโ๐ป OWNER", url=f"https://t.me/boyfriendnice"
                    )
                ]
            ]
        )
   )

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
      f"""
**๐ฐ Perintah**
      
**=>> Memutar Lagu ๐ง**
      
โข /play (nama lagu) - Untuk Memutar lagu yang Anda minta melalui youtube
โข /ytplay (nama lagu) - Untuk Memutar lagu yang Anda minta melalui youtube
โข /yt (nama lagu) - Untuk Memutar lagu yang Anda minta melalui youtube
โข /p (nama lagu) - Untuk Memutar lagu yang Anda minta melalui youtube
โข /dplay (nama lagu) - Untuk Memutar lagu yang Anda minta melalui deezer
โข /splay (nama lagu) - Untuk Memutar lagu yang Anda minta melalui jio saavn
โข /player: Buka menu Pengaturan pemain
โข /skip: Melewati trek saat ini
โข /pause: Jeda trek
โข /resume: Melanjutkan trek yang dijeda
โข /end: โโMenghentikan pemutaran media
โข /current: Menampilkan trek yang sedang diputar
โข /playlist: Menampilkan daftar putar
      
Semua Perintah Bisa Digunakan Kecuali Perintah /player /skip /pause /resume  /end Hanya Untuk Admin Grup
      
**==>>Download Lagu ๐ฅ**
      
โข /song [nama lagu]: Unduh audio lagu dari youtube

**=>> Saluran Music Play ๐?**
      
โช๏ธ Hanya untuk admin grup tertaut:
      
โข /cplay (nama lagu) - putar lagu yang Anda minta
โข /cdplay (nama lagu) - putar lagu yang Anda minta melalui deezer
โข /csplay (nama lagu) - putar lagu yang Anda minta melalui jio saavn
โข /cplaylist - Tampilkan daftar yang sedang diputar
โข /cccurrent - Tampilkan sedang diputar
โข /cplayer - buka panel pengaturan pemutar musik
โข /cpause - jeda pemutaran lagu
โข /cresume - melanjutkan pemutaran lagu
โข /cskip - putar lagu berikutnya
โข /cend - hentikan pemutaran musik
โข /userbotjoinchannel - undang asisten ke obrolan Anda""",
      reply_markup=InlineKeyboardMarkup(
                  [
                    [InlineKeyboardButton(text = '๐ฉโ๐ป แดแดกษดแดส', url = f"t.me/{OWNER}")],
                    [InlineKeyboardButton(text = '๐ฐ ษขสแดแดแด', url=f"https://t.me/{SUPPORT_GROUP}"),
                     InlineKeyboardButton(text = '๐ฎ แดสแดษดษดแดส', url=f"https://t.me/{UPDATES_CHANNEL}")],
                    [InlineKeyboardButton("๐ ๐ณ๐พ๐ฝ๐ฐ๐๐ธ ๐", url=f"boyfriendnice")]
                ]
        ),
    )



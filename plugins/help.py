from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Aare Bsdk! Me YouTube downloader hun tho youtube app open kar aur video ka link copy kar, then mereko send kar me direct download link dunga. samjha kya Noob. Powered by @iAmLiKu1"
    await message.reply_text(helptxt)

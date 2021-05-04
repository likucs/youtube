from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("👑 Owner 👑", url="https://t.me/iAmLiKu1")],
        [InlineKeyboardButton(
            "🤓 Assistant 🤓", url="https://t.me/likuGF")]
    ])
    welcomed = f"Hi! <b>{message.from_user.first_name}</b>\n/help le Bete mouj kardi bsdk bc help pe click kar, mujhe kya dekh raha he."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation

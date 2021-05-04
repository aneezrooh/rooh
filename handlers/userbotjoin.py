# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.




from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["join"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
        invitelink = await client.export_active_calls_invite_link
    except:
        await message.reply_text(
            "<b>Add me as admin of yor group first</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "musicangel"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>നിൻ്റെ കണ്ണിൽ കുരുവാണോ? കണ്ടൂടെ ഞാൻ vc യില് നിക്കണ</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n User {user.first_name} couldn't join your group due to heavy join requests for userbot! Make sure user is not banned in group."
            "\n\nOr manually add @musicangelassistant to your Group and try again</b>",
        )
        return
    await message.reply_text(
            "<b>ഞാൻ ഗ്രൂപ്പിൽ കയറി</b>",
        )

@Client.on_message(filters.group & filters.command(["joinvc"]))
@authorized_users_only
@errors
    try:
        await USER.join_pytgcalls.active_calls(invitelink)
        await USER.send_message(message.chat.id,"ഞാൻ വീസിയിൽ കയറി.അപ്പോ തുടങ്ങട്ടെ")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>ഞാൻ വിസിയിലു കൊറേ നേരമായി കയറിയിട്ട്</b>",
        )

async def addchannel(client, message):
    chid = message.chat.id

@Client.on_message(filters.group & filters.command(["leavevc"]))
@authorized_users_only
@errors
     try:
        await USER.leave_pytgcalls.active_calls
     expect:
        await message.reply_text(
            f"<b><i>ഞാ പോവൂല..... എന്നെ എറക്കി വിട്ടാലും പൊവൂല</u></b>
       )
       return   
    
@USER.on_message(filters.group & filters.command("leave"))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>User couldn't leave your group! May be floodwaits."
            "\n\nOr manually kick me from to your Group</b>",
        )
        return

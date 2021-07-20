# COPYRIGHT (C) 2021 BY userbotX22 AND PROBOYX, ALAIN

"""
(((((((((((((((((((((((@userbotX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@userbotX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@userbotX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@userbotX22)))))))))))))))))))))))))))
                 MADE BY userbotX AND PROBOY X
                   DISIGNED BY ALAIN_CHAMPION
                   CREDITS #TEAMuserbot 
                PLEASE DON'T REMOVE THIS LINES
"""

from telethon import events, Button, custom
import re, os
from userbotX import PHOTO, xbot, BOT, VERSION
from userbot import bot
@xbot.on(events.NewMessage(pattern=("/alive|/start")))
async def awake(event):
  userbotX = f"ʜᴇʟʟᴏ ᴛʜɪs ɪs  {BOT}\n\n"
  userbotX += "ᴀʟʟ sʏsᴛᴇᴍ ɪs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ\n\n"
  userbotX += f"{BOT} VERSION : {VERSION} ʟᴀsᴛᴇsᴛ\n\n"
  userbotX += f"ᴍʏ ᴍᴀsᴛᴇʀ @{bot.me.username} ☺️\n\n"
  userbotX += "ғᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ\n\n"
  userbotX += "ᴛᴇʟᴇᴛʜᴏɴ : 1.20 LATEST\n\n"
  userbotX += "ᴛʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ"
  BUTTON = [[Button.url("𝙼𝙰𝚂𝚃𝙴𝚁", f"https://t.me/{bot.me.username}"), Button.url(f"{BOT} 𝚁𝙴𝙿𝙾", "https://github.com/userbotXOP/userbot-BOT")]]
  BUTTON += [[custom.Button.inline("𝚁𝙴𝙿𝙾𝚂𝙸𝚃𝙾𝚁𝚈", data="userbotX")]]
  await xbot.send_file(event.chat_id, PHOTO, caption=userbotX,  buttons=BUTTON)




@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"userbotX")))
async def callback_query_handler(event):
# inline by userbotX22 and PROBOY22 🔥
  PROBOYX = [[Button.url("REPO-userbot", "https://github.com/userbotXOP/userbot-BOT")]]
  PROBOYX +=[[Button.url("DEPLOY-userbot", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FuserbotXOP%2Flegendpack&template=https%3A%2F%2Fgithub.com%2FuserbotXOP%2Flegendpack")]]
  PROBOYX +=[[Button.url("TUTORIAL", "https://youtu.be/rGCSSFPsS4Q"), Button.url("STRING-SESSION", "https://repl.it/@legendx22/userbot-BOT#main.py")]]
  PROBOYX +=[[Button.url("API_ID & HASH", "https://t.me/usetgxbot"), Button.url("REDIS", "https://redislabs.com")]]
  PROBOYX +=[[Button.url("SUPPORT CHANNEL", "https://t.me/userbotBOT_OFFICIAL"), Button.url("SUPPORT GROUP", "https://t.me/userbot_USERBOT_SUPPORT")]]
  PROBOYX +=[[custom.Button.inline("ALIVE", data="PROBOY")]]
  await event.edit(text=f"𝙰𝙻𝙻 𝙳𝙴𝚃𝙰𝙸𝙻𝚂 𝙾𝙵 𝚁𝙴𝙿𝙾𝚂", buttons=PROBOYX)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"PROBOY")))
async def callback_query_handler(event):
# inline by userbotX22 and PROBOY22 🔥
  userbotX = f"ʜᴇʟʟᴏ ᴛʜɪs ɪs  {BOT}\n\n"
  userbotX += "ᴀʟʟ sʏsᴛᴇᴍ ɪs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ\n\n"
  userbotX += f"{BOT} OS : {VERSION} ʟᴀsᴛᴇsᴛ\n\n"
  userbotX += f"ᴍʏ ᴍᴀsᴛᴇʀ @{bot.me.username} ☺️\n\n"
  userbotX += "ғᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ\n\n"
  userbotX += "ᴛᴇʟᴇᴛʜᴏɴ : 1.20 LATEST\n\n"
  userbotX += "ᴛʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ"
  BUTTONS = [[Button.url("𝙼𝙰𝚂𝚃𝙴𝚁", f"https://t.me/{bot.me.username}"), Button.url(f"{BOT} 𝚁𝙴𝙿𝙾", "https://github.com/userbotXOP/userbot-BOT")]]
  BUTTONS += [[custom.Button.inline("𝚁𝙴𝙿𝙾𝚂𝙸𝚃𝙾𝚁𝚈", data="userbotX")]]
  await event.edit(text=userbotX, buttons=BUTTONS)


@xbot.on(events.NewMessage(pattern=("/repo|#repo")))
async def repo(event):
  await xbot.send_message(event.chat, "ʀᴇᴘᴏ ᴏғ ʟᴇɢᴇɴᴅ-ʙᴏᴛ", buttons=[[Button.url("⚜️ ʀᴇᴘᴏ ⚜️", "https://github.com/userbotXOP/userbot-BOT")]])

# COPYRIGHT © BY userbotX22

"""
(((((((((((((((((((((((@userbotX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@userbotX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@userbotX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@userbotX22)))))))))))))))))))))))))))

                 MADE BY userbotX22
                 IDEA BY PROBOYX
                 CREDITS TEAMuserbot
                 PLEASE KEEP CREDITS 🥺
"""



from telethon import events, Button, custom
from userbotX import BOT
import os,re
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@tgbot.on(events.InlineQuery(pattern=r"repo"))
async def inline_id_handler(event: events.InlineQuery.Event):
 userbot = event.builder
 X= [[custom.Button.inline("🔥 CLICK ME 🔥",data="obhai")]]
 query = event.text
 result = userbot.article("userbot",text="REPO AND SUPPORT",buttons=X,link_preview=False)
 await event.answer([result])
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"obhai")))
async def callback_query_handler(event):

# inline by userbotX22 and PROBOYX 🔥
  await event.edit(text=f"{BOT} REPO AND GROUP LINK",buttons=[[Button.url(f"🔥{BOT} REPO🔥", url="https://github.com/userbotXOP/userbot-BOT"), Button.url(f"⚡{BOT} SUPPORT⚡", url="https://t.me/userbot_USERBOT_SUPPORT")]])

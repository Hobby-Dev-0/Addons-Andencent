"""
(((((((((((((((((((((((@userbotX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@userbotX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@userbotX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@userbotX22)))))))))))))))))))))))))))
           MADE BY @userbotX22 dont kang this plugin
         CREDITS = @userbotX22 @PROBOYX @alain_champion
     Special thanks @alain_champion for this modified version
            if you kang then keep credits
"""
import os
import time
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, StartTime, CMD_HELP
from . import legend
from userbotX import BOT, PHOTO, VERSION
from userbot.utils import admin_cmd
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "userbot BOY"

global kanger #kanger aaya bhaago bc
        
#make by userbot X bht mehnat lag gayi yrr but banhi gaya π           
@borg.on(admin_cmd(pattern=r"awake"))
async def amireallyalive(awake):
   """ For .awake command, check if the bot is running.  """
   global PHOTO
   if PHOTO:
     tag = borg.uid
     uptm = await legend.get_readable_time((time.time() - StartTime))
     ALIVE_MESSAGE= f" β‘οΈ {BOT} β‘οΈ  IS ON π₯ FIRE π₯"
     ALIVE_MESSAGE += "\n\n"
     ALIVE_MESSAGE += "π πππππ΄πΌ πππ°πππ π\n\n"
     ALIVE_MESSAGE += "βοΈ ππ΄π»π΄ππ·πΎπ½ ππ΄πππΈπΎπ½ βοΈ : 1.21\n\n"
     ALIVE_MESSAGE += f"πΆ π»π΄πΆπ΄π½π³ ππ΄πππΈπΎπ½ πΆ :   {VERSION}\n\n"
     ALIVE_MESSAGE += f"π· ππΏππΈπΌπ΄ π· : {uptm}\n\n"
     ALIVE_MESSAGE += f"π  πΌπ π±πΎππ π : [{DEFAULTUSER}](tg://user?id={tag})\n\n"
     ALIVE_MESSAGE += "π° πΆππΎππΏ π° : [SUPPORT](https://t.me/userbot_USERBOT_SUPPORT)\n\n"
     ALIVE_MESSAGE += f"π  [π³π΄πΏπ»πΎπ](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FuserbotXOP%2FLEGEN-BOT&template=https%3A%2F%2Fgithub.com%2FuserbotXOP%2Fuserbot-ROBOT) ππΎππ πΎππ½ πΎπΏ [{BOT}](http://github.com/legendxop/legend-bot)  π \n"   
     await awake.delete() 
     await borg.send_file(awake.chat_id, PHOTO,caption=ALIVE_MESSAGE)
   elif PHOTO == None:
     PHOTO = "https://telegra.ph/file/0ed5f920e8a5e9a7b0029.jpg"
     tag = borg.uid
     uptm = await legend.get_readable_time((time.time() - StartTime))
     ALIVE_MESSAGE= f" β‘οΈ {BOT} β‘οΈ  IS ON π₯ FIRE π₯"
     ALIVE_MESSAGE += "\n\n"
     ALIVE_MESSAGE += "π πππππ΄πΌ πππ°πππ π\n\n"
     ALIVE_MESSAGE += "βοΈ ππ΄π»π΄ππ·πΎπ½ ππ΄πππΈπΎπ½ βοΈ : 1.20\n\n"
     ALIVE_MESSAGE += f"πΆ π»π΄πΆπ΄π½π³ ππ΄πππΈπΎπ½ πΆ :   {VERSION}\n\n"
     ALIVE_MESSAGE += f"π· ππΏππΈπΌπ΄ π· : {uptm}\n\n"
     ALIVE_MESSAGE += f"π  πΌπ π±πΎππ π : [{DEFAULTUSER}](tg://user?id={tag})\n\n"
     ALIVE_MESSAGE += "π° πΆππΎππΏ π° : [SUPPORT](https://t.me/userbot_USERBOT_SUPPORT)\n\n"
     ALIVE_MESSAGE += f"π  [π³π΄πΏπ»πΎπ](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FuserbotXOP%2FLEGEN-BOT&template=https%3A%2F%2Fgithub.com%2FuserbotXOP%2Fuserbot-ROBOT) ππΎππ πΎππ½ πΎπΏ [{BOT}](http://github.com/legendxop/legend-bot)  π \n"   
     await awake.delete() 
     await borg.send_file(awake.chat_id, PHOTO,caption=ALIVE_MESSAGE)
   else:
     await awake.edit("please add right value on ALIVE_PHOTTO var")

CMD_HELP.update(
    {
        "awake": "Plugin : awake\
    \n\nSyntax : .awake\
    \nFunction : you can set here costom alive pic .set var ALIVE_PHOTTO (Telegraph link)"
    }
)

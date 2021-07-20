"""
(((((((((((((((((((((((@userbotX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@userbotX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@userbotX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@userbotX22)))))))))))))))))))))))))))


                  made by @userbotX22
                  credits TEAMuserbot
                  idea by @Alain_Champion 
 ((((((((((((((((((((((((( @userbotX22 AND @PROBOYX)))))))))))))))))))))))))))
"""
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP
from userbot.utils import admin_cmd
from userbotX import MASTER
userbot = MASTER
PROBOY = "@tgscanrobot"
# MADE BY userbotX22 🔥🔥

@borg.on(admin_cmd("ginfo ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    userbotX = event.pattern_match.group(1)
    if "@" in userbotX:
        async with borg.conversation(PROBOY) as conv:
            try:
                
                await event.edit(f"THIS USER DETAILS CHECKING BY {userbot}")
                await conv.send_message("/start")
                await conv.get_response() #made by userbotX22
                await conv.send_message(f"{userbotX}")
                TEAMX = await conv.get_response()
                await borg.send_message(event.chat_id, TEAMX.text)
                await event.delete() #made by userbotX22
            except YouBlockedUserError:
                await event.edit("Error: @tgscanrobot unblock and retry!")
    elif userbotX == "":
        OP = await event.get_reply_message()
        PRO = OP.sender.id 
        async with borg.conversation(PROBOY) as conv:
            try: #made by userbotX22 🔥
              #made by userbotX22 
                await event.edit(f"THIS USER DETAILS CHECKING BY {userbot}")
                await conv.send_message("/start")
                await conv.get_response() #made by userbotX22
                await conv.send_message(f"{PRO}")
                TEAMX = await conv.get_response()
                await borg.send_message(event.chat_id, TEAMX.text)
                await event.delete()
            except YouBlockedUserError: #made by userbotX22
                await event.edit("Error: unblock @tgscanrobot and try again!")
    else:
        async with borg.conversation(PROBOY) as conv:
            try: #made by userbotX22 🔥
                
                await event.edit(f"THIS USER DETAILS CHECKING BY {userbot}") 
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message(f"{PRO}")
                TEAMX = await conv.get_response()
                await borg.send_message(event.chat_id, TEAMX.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: unblock  @tgscanrobot `and try again!")
CMD_HELP.update({
    "ginfo ":"type .ginfo <@username> or tag a user type .ginfo 🔥"})

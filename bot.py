#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


import logging
import functools
from telethon import TelegramClient, events, Button
from decouple import config

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)

bottoken = None
# start the bot
print("Starting...")
apiid = 20781152
apihash = "0781163b5caac00db3268444e688d9e7"
try:
    bottoken = config("BOT_TOKEN")
except:
    print("Environment vars are missing!")
    print("Bot is quiting...")
    exit()

if bottoken != None:
    try:
        SLBotsOfficial = TelegramClient("bot", apiid, apihash).start(bot_token=bottoken)
    except Exception as e:
        print(f"ERROR!\n{str(e)}")
        print("Bot is quiting...")
        exit()
else:
    print("Environment vars are missing! Kindly recheck.")
    print("Bot is quiting...")
    exit()
    

@SLBotsOfficial.on(events.NewMessage(pattern="^/start"))
async def start(event):
    if event.is_private:
       await event.reply("Hey, I'm **Advanced Anonymous forwarder** Bot 👨‍💻\n\nClick on help to find out how to use me\n\n**@SL_BOTS_TM**", 
                         buttons=[[Button.inline("Help", data="help")], 
                                  [Button.url("Channel", url="https://t.me/SLBotsOfficial"), Button.url("Source", url="https://github.com/DARKEMPIRESL/Anonymous-Forwarder")]])
       return
    if event.is_group:
       await event.reply("Hey, I'm **Advanced Anonymous forwarder** Bot 👨‍💻") 
     
 
@SLBotsOfficial.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):
     await event.edit("**Help 📖**\n\nUsing me you can anonymize the sender and add or change caption of a media file\n\n**Available Commands 🧐**\n\n- /send (reply to media): Anonymize the sender\n- /send (caption) (reply to media): Add or change the caption and anonymize the sender\n\n*⃣ This bot works on both groups and private, but only admins can use the bot in groups\n\n**@SL_BOTS_TM**", 
                        buttons=[[Button.inline("Back", data="start")]])
    
@SLBotsOfficial.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
     await event.edit("Hey, I'm **Advanced Anonymous Sender** Bot 👨‍💻\n\nClick on help to find out how to use me\n\n**@SL_BOTS_TM**", 
                       buttons=[[Button.inline("Help", data="help")], 
                                [Button.url("Channel", url="https://t.me/SLBotsOfficial"), Button.url("Source", url="https://github.com/DARKEMPIRESL/Anonymous-Forwarder")]])
         
@SLBotsOfficial.on(events.NewMessage(pattern="^/send ?(.*)"))
async def caption(event):
   if event.is_private:
        return
   a = await event.client.get_permissions(event.chat_id, event.sender_id)
   if a.is_admin:
      try:
        lel = await event.get_reply_message()
        cap = event.pattern_match.group(1)
        await SLBotsOfficial.send_file(event.chat.id, lel, caption=cap)
      except Exception:
         await event.reply("Reply to a media file 🥴")
         return
   if not a.is_admin:
      await event.reply("Only admins can execute this command!")

@SLBotsOfficial.on(events.NewMessage(pattern="^/send ?(.*)"))
async def caption(event):
   if event.is_group:
        return
   try:
     lel = await event.get_reply_message()
     cap = event.pattern_match.group(1)
     await SLBotsOfficial.send_file(event.chat.id, lel, caption=cap)
   except Exception:
      await event.reply("Reply to a media file 🥴")
      return 
      
       
print("Bot has started!")
print("Do visit @trtechguide.")
SLBotsOfficial.run_until_disconnected()
  

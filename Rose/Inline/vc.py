from Rose import bot as app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup


supun = """
✅Admin Commands:

c stands for channel play.

/pause or /cpause - Pause the playing music.
/resume or /cresume- Resume the paused music.
/mute or /cmute- Mute the playing music.
/unmute or /cunmute- Unmute the muted music.
/skip or /cskip- Skip the current playing music.
/stop or /cstop- Stop the playing music.
/shuffle or /cshuffle- Randomly shuffles the queued playlist.
/seek or /cseek - Forward Seek the music to your duration
/seekback or /cseekback - Backward Seek the music to your duration
/restart - Restart bot for your chat .


✅Specific Skip:
/skip or /cskip [Number(example: 3)] 
    - Skips music to a the specified queued number. Example: /skip 3 will skip music to third queued music and will ignore 1 and 2 music in queue.

✅Loop Play:
/loop or /cloop [enable/disable] or [Numbers between 1-10] 
    - When activated, bot loops the current playing music to 1-10 times on voice chat. Default to 10 times.

✅Auth Users:
Auth Users can use admin commands without admin rights in your chat.

/auth [Username] - Add a user to AUTH LIST of the group.
/unauth [Username] - Remove a user from AUTH LIST of the group.
/authusers - Check AUTH LIST of the group.
"""

@app.on_callback_query(filters.regex("_adc"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=supun,
        reply_markup=close,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()

supunm = """
✅Bot Commands:

/stats - Get Top 10 Tracks Global Stats, Top 10 Users of bot, Top 10 Chats on bot, Top 10 Played in a chat etc etc.

/sudolist - Check Sudo Users of Yukki Music Bot

/lyrics [Music Name] - Searches Lyrics for the particular Music on web.

/song [Track Name] or [YT Link] - Download any track from youtube in mp3 or mp4 formats.

/player -  Get a interactive Playing Panel.

c stands for channel play.

/queue or /cqueue- Check Queue List of Music.
"""

@app.on_callback_query(filters.regex("_bcd"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=supunm,
        reply_markup=close,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()


supunma = """
✅Extra  Commands:
/start - Start the Music Bot.
/help  - Get Commands Helper Menu with detailed explanations of commands.
/ping- Ping the Bot and check Ram, Cpu etc stats of Bot.

✅Group Settings:
/settings - Get a complete group's settings with inline buttons

🔗 Options in Settings:

1️⃣ You can set Audio Quality you want to stream on voice chat.

2️⃣ You can set Video Quality you want to stream on voice chat.

3️⃣ Auth Users:- You can change admin commands mode from here to everyone or admins only. If everyone, anyone present in you group will be able to use admin commands(like /skip, /stop etc)

4️⃣ Clean Mode: When enabled deletes the bot's messages after 5 mins from your group to make sure your chat remains clean and good.

5️⃣ Command Clean : When activated, Bot will delete its executed commands (/play, /pause, /shuffle, /stop etc) immediately.

6️⃣ Play Settings:

/playmode - Get a complete play settings panel with buttons where you can set your group's play settings. 

Options in playmode:

1️⃣ Search Mode [Direct or Inline] - Changes your search mode while you give /play mode. 

2️⃣ Admin Commands [Everyone or Admins] - If everyone, anyone present in you group will be able to use admin commands(like /skip, /stop etc)

3️⃣ Play Type [Everyone or Admins] - If admins, only admins present in group can play music on voice chat.
"""
@app.on_callback_query(filters.regex("_ecd"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=supunma,
        reply_markup=close,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()


supunmas = """
✅Play Commands:

Available Commands = play , vplay , cplay

ForcePlay Commands = playforce , vplayforce , cplayforce

c stands for channel play.
v stands for video play.
force stands for force play.

/play or /vplay or /cplay  - Bot will start playing your given query on voice chat or Stream live links on voice chats.

/playforce or /vplayforce or /cplayforce -  Force Play stops the current playing track on voice chat and starts playing the searched track instantly without disturbing/clearing queue.

/channelplay [Chat username or id] or [Disable] - Connect channel to a group and stream music on channel's voice chat from your group.


✅Bot's Server Playlists:
/playlist  - Check Your Saved Playlist On Servers.
/deleteplaylist - Delete any saved music in your playlist
/play  - Start playing Your Saved Playlist from Servers.
"""
@app.on_callback_query(filters.regex("_pcd"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=supunmas,
        reply_markup=close,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()    

supunmasc = """
🔰ADD & REMOVE SUDO USERS :
/addsudo [Username or Reply to a user]
/delsudo [Username or Reply to a user]

🛃HEROKU:
/usage - Dyno Usage.

🌐CONFIG VARS:
/get_var - Get a config var from Heroku or .env.
/del_var - Delete any var on Heroku or .env.
/set_var [Var Name] [Value] - Set a Var or Update a Var on heroku or .env. Seperate Var and its Value with a space.

🤖BOT COMMANDS:
/reboot - Reboot your Bot. 
/update - Update Bot.
/speedtest - Check server speeds
/maintenance [enable / disable] 
/logger [enable / disable] - Bot logs the searched queries in logger group.
/get_log [Number of Lines] - Get log of your bot from heroku or vps. Works for both.
/autoend [enable|disable] - Enable Auto stream end after 3 mins if no one is listening.

📈STATS COMMANDS:
/activevoice - Check active voice chats on bot.
/activevideo - Check active video calls on bot.
/stats - Check Bots Stats

⚠️BLACKLIST CHAT FUNCTION:
/blacklistchat [CHAT_ID] - Blacklist any chat from using Music Bot
/whitelistchat [CHAT_ID] - Whitelist any blacklisted chat from using Music Bot
/blacklistedchat - Check all blacklisted chats.

👤BLOCKED FUNCTION:
/block [Username or Reply to a user] - Prevents a user from using bot commands.
/unblock [Username or Reply to a user] - Remove a user from Bot's Blocked List.
/blockedusers - Check blocked Users Lists

👤GBAN FUNCTION:
/gban [Username or Reply to a user] - Gban a user from bot's served chat and stop him from using your bot.
/ungban [Username or Reply to a user] - Remove a user from Bot's gbanned List and allow him for using your bot
/gbannedusers - Check Gbanned Users Lists

🎥VIDEOCALLS FUNCTION:
/set_video_limit [Number of Chats] - Set a maximum Number of Chats allowed for Video Calls at a time. Default to 3 chats.
/videomode [download|m3u8] - If download mode is enabled, Bot will download videos instead of playing them in M3u8 form. ByDefault to M3u8. You can use download mode when any query doesnt plays in m3u8 mode.

⚡️PRIVATE BOT FUNCTION:
/authorize [CHAT_ID] - Allow a chat for using your bot.
/unauthorize [CHAT_ID] - Disallow a chat from using your bot.
/authorized - Check all allowed chats of your bot.

🌐BROADCAST FUNCTION:
/broadcast [Message or Reply to a Message] - Broadcast any message to Bot's Served Chats.

options for broadcast:
-pin : This will pin your message 
-pinloud : This will pin your message with loud notification
-user : This will broadcast your message to the users who have started your bot.
-assistant : This will broadcast your message from assistant account of your bot.
-nobot : This will force your bot to not broadcast message

Example: /broadcast -user -assistant -pin Hello Testing
"""
@app.on_callback_query(filters.regex("_aci"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=supunmasc,
        reply_markup=close,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete() 

    
close = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('« Back', callback_data='bot_commands')
        ]], 
)


asuttons = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton
                (
                    "Admin Commands", callback_data="_adc"
                ),            
            InlineKeyboardButton
                (
                    "Bot Commands", callback_data="_bcd"
                ) 
        ],
        [
            InlineKeyboardButton
                (
                    "Extra commands", callback_data="_ecd"
                ),            
            InlineKeyboardButton
                (
                    "Play Commands", callback_data="_pcd"
                )  
        ], 
        [
            InlineKeyboardButton
                (
                    "sudo commands", callback_data="_aci"
                )
        ],
        [
            InlineKeyboardButton('« Back', callback_data='bot_commands')
        ], 
    ]
)

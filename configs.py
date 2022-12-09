import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", "15823382"))
    API_HASH = os.getenv("API_HASH", "016d5e115a06ddfb6121823d72ae4d8c")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5918078029:AAFAuWGqmVOIIp2-VtLQNxD9De6vR9NUgm4")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "MdiskRobot")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "1BVtsOHwBuzfE3M039kmYlTP-Pxemeg_qL4L-EAoppuGMHIjfQXEiETO92jaUYIHAT9a0kZ5nsk6cDw969lLvMV6TAVvXJAfd3G_v1C16lUdJAMuGfRQLRqcr_cI4alOHaJar1EH3Utd90z0k931nZs4Fer0_JPR6I60vM4yomo53j3WA9e1trZFwD9bgOYiIAvyqP9mf4zxp9qbnZ7_gtL2PgSZFLDFRo1GRvsoohrHt6hKi6HQH2BoimDXtyHzRId1UGfnCq9SFVfuhlYhrHX4076qnaor6Pue1BgiEFKzYJ3faR2jIXELV818rQyTNcbB3p-zWGoV7os7xzIKT5ITDGxJf9Ao=")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-1001631279048"))
    BOT_USERNAME = os.getenv("BOT_USERNAME", "Mdisk_search_re_bot")
    BOT_OWNER = int(os.getenv("BOT_OWNER", "5104293442"))
    OWNER_USERNAME = os.getenv("OWNER_USERNAME", "tlgbotsowner")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "-1001767857004")
    GROUP_USERNAME = os.getenv("GROUP_USERNAME", "Mdiskmoviesgro")
    START_MSG = os.getenv("START_MSG", "Hᴇʏ👋\n\nIᴍ A Bᴏᴛ Fᴏʀ Sᴇɴᴅɪɴɢ Fʀᴏᴍ Yᴏᴜʀ Cʜᴀɴɴᴇʟ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ.Yᴏᴜ Cᴀɴ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ.Fᴏʀ Mᴏʀᴇ Iɴꜰᴏ Cʟɪᴄᴋ Oɴ Hᴇʟᴘ ✅" )
    START_PHOTO = os.getenv("START_PHOTO", "https://telegra.ph/file/5fb09a22f90bd5eea1642.jpg")
    HOME_TEXT = os.getenv("HOME_TEXT", "Thanks For Using🎁" )
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "-1001767857004")
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://W9Uyj61afEXSw601:W9Uyj61afEXSw601@cluster0.zsxso.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001529577466"))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 20))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "daagffgd")
    FORCE_SUB = os.getenv("FORCE_SUB", "True")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 200))
    MDISK_API = os.getenv("MDISK_API", "UM1dBYJxSu9QO1S9s8Tv")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "31"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", "I ᴏɴʟʏ ꜱʜᴀʀᴇ ᴛʜᴇ ᴘᴏꜱᴛ ꜰʀᴏᴍ ᴘᴇᴏᴘʟᴇ'ꜱ ᴄʜᴀɴɴᴇʟ! ᴡʜᴏ ᴍᴀᴅᴇ ᴍᴇ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ, i ɴᴏᴛ ꜱᴛᴏʀᴇ ᴀɴʏ ꜰɪʟᴇꜱ ᴏʀ ᴛᴇxᴛ ɪɴ  ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ.ᴅᴍ ꜰᴏʀ ᴀɴʏ Qᴜᴇʀʏ @tlgbotsowner 🤖")
    ABOUT_HELP_TEXT = os.getenv("HELP_TEXT", "Available Soon💻" )

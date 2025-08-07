#
# Copyright (C) 2021-2022 by TeamMyMusicBot@Github, < https://github.com/TeamMyMusicBot >.
#
# This file is part of < https://github.com/TeamMyMusicBot/MyMusicBotMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamMyMusicBot/MyMusicBotMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from MyMusicBotMusic.core.bot import MyMusicBotBot
from MyMusicBotMusic.core.dir import dirr
from MyMusicBotMusic.core.git import git
from MyMusicBotMusic.core.userbot import Userbot
from MyMusicBotMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = MyMusicBotBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

#
# Copyright (C) 2021-2022 by TeamMyMusicBot@Github, < https://github.com/TeamMyMusicBot >.
#
# This file is part of < https://github.com/TeamMyMusicBot/MyMusicBotMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamMyMusicBot/MyMusicBotMusicBot/blob/master/LICENSE >
#
# All rights reserved.


class AssistantErr(Exception):
    def __init__(self, errr: str):
        super().__init__(errr)

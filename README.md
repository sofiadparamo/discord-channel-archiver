# Simple Discord Channel Archiver

This is a simple script that will archive all messages from a Discord channel into a folder. It will create a folder for each channel and save all their messages in that folder. It will also save all attachments and embeds.

Warning: Two channels with the same name will overwrite each other.

This bot is not meant to be run public. It will save the files in the host's file system. It is meant to be run locally or on a private cloud.

⚠️ This bot is not maintained and if there are changes to the Discord API it may stop working. You may open a PR if you want to fix it, it should be pretty simple.

## Installation

1. Install Python 3.8 or higher
2. Install the requirements with `pip install -r requirements.txt`
3. [Create a Discord bot and generate a token](https://discordpy.readthedocs.io/en/stable/discord.html)
4. Rename `example.env` to `.env` and fill in the token
5. Run the bot with `python bot.py`

## Usage

1. Invite the bot to your server
2. Give it the permission to read messages and history from the channels you want to archive. Or simply give it administrator permissions
3. Run the command `!scrape` in the channel you want to archive
4. Wait until the bot is done, you'll see a message in the channel when it's done. It may take from some minutes to several hours depending on the ammount of messages in the channel, the size of the attachments and the speed of your internet connection.
5. The files will be saved in the folder with the same name as the channel. These are located in the root folder of the bot.

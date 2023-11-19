import discord
from discord.ext import commands
import os
import json
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def scrape(ctx):
    # Check permission
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("You must be an administrator to use this command.")
        return
    
    channel_name = ctx.channel.name

    if(not(channel_name)):
       channel_name = "output"

    # Create output directory if it doesn't exist
    if not os.path.exists(channel_name):
        os.makedirs(channel_name)

    with open(f'{channel_name}/messages.txt', 'w', encoding='utf-8') as file:
        # Fetch all messages
        async for message in ctx.channel.history(limit=None, oldest_first=True):
            # Writing message content, author, and timestamp to the file
            file.write(f"[{message.created_at}] {message.author}: {message.content}\n")
            
            # Writing embeds in JSON format
            for embed in message.embeds:
                file.write(json.dumps(embed.to_dict()) + '\n')

            # Save attachments
            for attachment in message.attachments:
                # Create a unique file name based on the message ID and original file name
                file_path = f"{channel_name}/{message.id}_{attachment.filename}"
                await attachment.save(file_path)

    await ctx.send(f"Messages, attachments, and embeds have been saved to the {channel_name} folder")

bot.run(token=token)
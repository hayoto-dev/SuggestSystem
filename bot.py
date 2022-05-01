import discord, datetime
from discord.ext import commands


SUGGESTION_CHANNEL = # Put here the Suggestion Channel ID
TOKEN = "Put here a valid Bot Token!"


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_message(message):

    if message.channel.id == SUGGESTION_CHANNEL:
        if message.author.bot:
            return
            
        await message.delete()

        suggestionEmbed = discord.Embed(title=f"Suggestion by {message.author.display_name}!", description=f"{message.content}")
        suggestionEmbed.timestamp = datetime.datetime.utcnow()

        suggest = await message.channel.send(embed=suggestionEmbed)

        await suggest.add_reaction('✅')
        await suggest.add_reaction('❌')
        return


bot.run(TOKEN)

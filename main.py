from discord.utils import get # New import
import discord
from discord.ext import commands # New import
import datetime
client = commands.Bot(command_prefix='!')
		

@client.event
async def on_ready():
	print("Bot is ready")



@client.event
async def on_message(message_before):

	if message_before.author.id == (useridyourtracknig):
	
		channel = client.get_channel() # replace with channel id
	
		embed = discord.Embed(name='Message sent', colour = discord.Color.red())
		embed.add_field(name = f"(nameofuser): ", value=f"{message_before.content}\n\n[Go to message]({message_before.jump_url})")
		embed.timestamp = datetime.datetime.utcnow()
		
    #Optional to add a icon on the bottom
		#embed.set_footer(text='\u200b',icon_url="https://i.imgur.com/HBRGHYm.jpeg")

		await channel.send(embed = embed)
		
		

			
			
		
	else:
				return


client.run("discordtoken")

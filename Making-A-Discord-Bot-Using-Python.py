
import discord
from discord.ext import commands 

TOKEN = "enter you token here"

client = commands.Bot(command_prefix="@")#or anything you want by which you will call this function 

@client.event()
async def on_ready():
	print("Hey there I am ready")#this is just to know that the bot is online 

@client.command()
async def hello(ctx):
	await ctx.send("Hey there how are you doing")#so you can do the same way anything you want 

client.run(TOKEN)#so in the satrting we gave like TOKEN so we are running the bot using this or simply you can just insert your token directly to see how to see the token then see the above things
	

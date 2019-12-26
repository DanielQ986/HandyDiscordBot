import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


bot = commands.Bot(command_prefix='?')



@bot.command(name='speak', help='say nigga')
async def speak(ctx):
    response = 'nigga'
    await ctx.send(response)

@bot.command(name='roll_multiple', help='Rolls multiple virtual dice')
async def roll_multiple(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides+1)))
        for x in range(number_of_dice)
    ]
    response = ', '.join(dice)
    await ctx.send(response)

@bot.command(name='roll', help='Roll a virtual dice')
async def roll(ctx):
    response = str(random.choice(range(1, 7)))
    await ctx.send(response)

@bot.command(name='do-you-care', help='Tells you whether it cares')
async def do_you_care(ctx):
    answers = [
        'Not at all',
        'NO ONE FUCKING ASKED',
        'I guess i care a little bit',
        'KILL YOURSELF'
    ]
    response = random.choice(answers)
    await ctx.send(response)

@bot.command(name='create-channel', help='Allows admins to create channels')
@commands.has_role('Owners')
async def create_channel(ctx, channel_name='new-channel'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating new channel: {channel_name}')
        await guild.create_voice_channel(channel_name)

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.errors.CheckFailure):
        await ctx.send('You do not have the required role for this command.')

@bot.listen('on_message')
async def my_message(message):
    if message.author == bot.user:
        return

    if message.mention_everyone:
        await message.channel.send('Nigga can you not @everyone please')
    ms = str(message.author)
    ms2 = ms[0:-5]
    if 'Smoovv' in ms2.lower():
        await message.channel.send('LE MONK!')
    if 'shane' in message.content.lower():
        msauthor = str(message.author)
        msauthor2 = msauthor[0:-5]
        await message.channel.send(f'{msauthor2} did you mean Le Monk?')



bot.run(TOKEN)




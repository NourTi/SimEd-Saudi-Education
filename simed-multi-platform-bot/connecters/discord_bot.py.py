"""
Discord connector for SimEd Studio Bot
"""

import discord
from core.agent import SimEdAgent
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)
agent = SimEdAgent()


@bot.event
async def on_ready():
    print(f"✅ Discord bot logged in as {bot.user}")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name="teachers design better lessons"
        )
    )


@bot.command(name="start")
async def start(ctx):
    """Start SimEd conversation"""
    response = agent.start_conversation(str(ctx.author.id))
    await ctx.send(response)


@bot.event
async def on_message(message):
    """Handle incoming messages"""
    if message.author == bot.user:
        return

    if message.content.startswith("/"):
        await bot.process_commands(message)
    else:
        user_id = str(message.author.id)
        response = agent.process_message(user_id, message.content)
        await message.reply(response)


def run_discord(token: str):
    """Start Discord bot"""
    bot.run(token)

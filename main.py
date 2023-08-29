import discord
import os

from dotenv import load_dotenv
from discord.ext import commands
from request import *


load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Bot: {bot.user} | ID: {bot.user.id}")


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command()
async def exibir(ctx, *args):
    arguments = ' '.join(args)
    await ctx.send(arguments)


@bot.command()
async def entrou(ctx, member: discord.Member):
    await ctx.send(f'{member.mention} entrou no dia {discord.utils.format_dt(member.joined_at)}')


@bot.command()
async def conta(ctx):
    await ctx.send(f"{ctx.author.mention} Conta aquela")


@bot.command()
async def tapa(ctx, member: discord.Member):
    await ctx.send(f"{ctx.author.mention} deu um tapa no {member.mention}")


@bot.command()
async def kanye(ctx):
    await ctx.send(f"{fetch_kanye()} - Kanye West")


@bot.command()
async def dog(ctx):
    await ctx.send(fetch_dogs())


@bot.command()
async def pk(ctx, name):
    await ctx.send(fetch_pokemon(name))


@bot.command()
async def cep(ctx, cep):
    await ctx.send(fetch_cep(cep))


bot.run(os.getenv("TOKEN"))

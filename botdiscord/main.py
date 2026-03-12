import sqlite3
import discord
from discord.ext import commands, tasks
from datetime import time

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
    enviar_menssagem.start()
    print("Bot inicializado com suscesso")

@bot.event
async def on_message(msg:discord.Message):
    if msg.author.bot:
        return
    await bot.process_commands(msg)
    # await msg.reply(f"O usuario {msg.author.mention} enviou uma mensagem no canal {msg.channel.name}")
@bot.event
async def on_member_join(membro:discord.Member):
    canal = bot.get_channel(1481644925278752921)
    await canal.send(f"{membro.mention} entrou no servidor")
@bot.event
async def on_reaction_add(reacao:discord.Reaction, membro:discord.Member):
    await reacao.message.reply(f"o membro {membro.name} reagiu a menssagem com {reacao.emoji}")

@tasks.loop(time = time(14, 14))
async def enviar_menssagem():
    canal = bot.get_channel(1481654369840533514)
    await canal.send("Menssagem programada")

@bot.command()
async def ola(ctx:commands.Context):
    nome = ctx.author.name
    await ctx.reply(f"Olá, {nome}! Tudo bem?")

@bot.command()
async def txt(ctx:commands.Context, *,texto):
    await ctx.send(texto)

@bot.command()
async def somar(ctx:commands.Context, num1, num2):
    resultado = float(num1) + float(num2)
    await ctx.send(f"O resultado  da soma de {num1} e {num2} é: {resultado}")

@bot.command()
async def enviar_embed(ctx:commands.Context):
    minha_embed = discord.Embed()
    minha_embed.title = "Titulo da embed"
    minha_embed.description = "descrição da embed"

    imagem = discord.File("images.jpg", "images.jpg")
    minha_embed.set_image(url="attachment://images.jpg")



    await ctx.reply(embed=minha_embed)


bot.run("MTQ4MTYyOTk4Mjg3ODA3NzEyMQ.GOBwvv.VFjTlTGYFaZpb5MkgHG5lR2-_ekPO6UKjhIetw")
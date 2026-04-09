import sqlite3
import discord
from discord.ext import commands, tasks
from datetime import time
intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

conexao = sqlite3.connect("Usuarios.db")
CreateTable = "CREATE TABLE IF NOT EXISTS usuarios (user_id INTEGER PRIMARY KEY, senha TEXT, user_name TEXT)"
cursor = conexao.cursor()
cursor.execute(CreateTable)
conexao = sqlite3.connect("Personagem.db")
CreateTable2 = "CREATE TABLE IF NOT EXISTS personagem (user_id INTEGER PRIMARY KEY, faccão TEXT, raca TEXT, classe TEXT, nome TEXT, zona_inicial TEXT, nivel INTEGER, COINS INTEGER)"
cursor = conexao.cursor()
cursor.execute(CreateTable2)


class CriarouDeletarseção(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None) # timeout=None para o botão não parar de funcionar

    @discord.ui.button(label="Criar seção", style=discord.ButtonStyle.success, custom_id="criar_btn")
    async def Criar(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        member = interaction.user
        
        # 1. Localiza ou cria a categoria
        categoria = discord.utils.get(guild.categories, name="Seções temporárias")
        if not categoria:
            categoria = await guild.create_category("Seções temporárias")

        # 2. Verifica se o canal já existe (usando o ID no tópico para ser infalível)
        canal_existente = discord.utils.get(categoria.text_channels, topic=str(member.id))

        if canal_existente:
            return await interaction.response.send_message(f"Você já tem um canal: {canal_existente.mention}", ephemeral=True)

        # 3. Permissões
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            member: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)
        }

        # 4. Cria o canal
        nome_canal = f"seção-{member.name}".lower().replace(" ", "-")
        canal = await guild.create_text_channel(
            name=nome_canal,
            category=categoria,
            overwrites=overwrites,
            topic=str(member.id) # Guardamos o ID aqui para o botão "Deletar" achar depois
        )

        # Embed de boas-vindas dentro do canal novo
        embed_welcome = discord.Embed(title="⚔️ Sua Jornada Começa!", description="Bem-vindo ao seu canal privado. Digite iniciar para começar sua jornada! digite .menu pra iniciar", color=0x00ff00)
        await canal.send(content=member.mention, embed=embed_welcome)

        await interaction.response.send_message(f"Seção criada com sucesso! Acesse: {canal.mention}", ephemeral=True)

    @discord.ui.button(label="Deletar seção", style=discord.ButtonStyle.danger, custom_id="deletar_btn")
    async def Deletar(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        member = interaction.user
        
        # Procura o canal que tem o ID do usuário no tópico
        categoria = discord.utils.get(guild.categories, name="Seções temporárias")
        if categoria:
            canal_para_deletar = discord.utils.get(categoria.text_channels, topic=str(member.id))
            
            if canal_para_deletar:
                await canal_para_deletar.delete(reason="Usuário solicitou exclusão da seção.")
                await interaction.response.send_message("Sua seção foi deletada com sucesso!", ephemeral=True)
            else:
                await interaction.response.send_message("Você não possui nenhuma seção ativa para deletar.", ephemeral=True)
        else:
            await interaction.response.send_message("Nenhuma categoria de seções encontrada.", ephemeral=True)

@bot.event
async def on_ready(): 
    print(f"Bot conectado como {bot.user}")
    
    # Isso faz com que os botões continuem funcionando mesmo se o bot reiniciar
    bot.add_view(CriarouDeletarseção())
    
    channel = bot.get_channel(1483185492848676904)
    if channel:
        embed = discord.Embed(
            title="⚔️ Bem-vindo ao Mundo de Azeroth", 
            description="Escolha uma das opções abaixo para gerenciar sua seção de RPG.",
            color=0x00ff00
        )
        # Nota: Idealmente você envia isso apenas uma vez, ou limpa o canal antes.
        await channel.send(embed=embed, view=CriarouDeletarseção())


#Criação de personagem


class criar_personagem_modal(discord.ui.Modal, title="Criar Personagem"):
    embed_criar = discord.Embed(
        title="Escolha a facção do seu personagem",
        color=0x00ff00
    )
    @discord.ui.button(label="Horda", style=discord.ButtonStyle.danger, custom_id="horda_btn")
    async def horda_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass
    @discord.ui.button(label="Aliança", style=discord.ButtonStyle.primary, custom_id="alianca_btn")
    async def alianca_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass

class CriarPersonagem(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="Criar Personagem", style=discord.ButtonStyle.primary, custom_id="criar_personagem_btn")
    async def criar_personagem(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass
        await interaction.response.send_modal(criar_personagem_modal())
    
    @discord.ui.button(label="Logar Personagem", style=discord.ButtonStyle.secondary, custom_id="logar_personagem_btn")
    async def logar_personagem(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass
        





@bot.command()
async def menu(ctx:commands.Context):
    embed_criar_logar = discord.Embed(
        title="⚔️ Bem-vindo ao Mundo de Azeroth", 
        description="Primeiro, escolha entre jogar com um personagem existente ou criar um novo. Use os comandos abaixo para prosseguir:\n\n",
        color=0x00ff00
    )

    await ctx.send(embed=embed_criar_logar, view=CriarPersonagem())
   

bot.run("MTQ4MTYyOTk4Mjg3ODA3NzEyMQ.GgDULG.n4Ai4mDfxKY3ot72OLOHNV8KX6AVXtaEpz-7yk")
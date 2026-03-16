import sqlite3
import discord
from discord.ext import commands, tasks
from datetime import time
intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

conexao = sqlite3.connect("Usuarios.db")
CreateTable = "CREATE TABLE IF NOT EXISTS usuarios (user_id INTEGER PRIMARY KEY, senha TEXT, nome_personagem TEXT)"
cursor = conexao.cursor()
cursor.execute(CreateTable)

class RegistroModal(discord.ui.Modal, title="Registro"):
    user = discord.ui.TextInput(label="ID do usuário", style=discord.TextStyle.short)
    senha = discord.ui.TextInput(label="Digite a senha", style=discord.TextStyle.short, min_length=6)
    Personagem= discord.ui.TextInput(label="Digite o nome do seu personagem", style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        user_id = self.user.value
        senha = self.senha.value
        nome_personagem = self.Personagem.value

        cursor.execute("INSERT INTO usuarios (user_id, senha, nome_personagem) VALUES (?, ?, ?)", (user_id, senha, nome_personagem))
        conexao.commit()

        await interaction.response.send_message(f"Registro concluído! User: {user_id}, Personagem: {nome_personagem}")
class LoginModal(discord.ui.Modal, title="login"):
    nome_personagem = discord.ui.TextInput(label="Digite o nome do seu personagem", style=discord.TextStyle.short)
    senha = discord.ui.TextInput(label="Digite a senha", style=discord.TextStyle.short, min_length=6)
    async def on_submit(self, interaction: discord.Interaction):
        nome_personagem = self.nome_personagem.value
        senha = self.senha.value

        cursor.execute("SELECT user_id FROM usuarios WHERE nome_personagem = ? AND senha = ?", (nome_personagem, senha))
        result = cursor.fetchone()
        if result:
            user_id = result[0]
            await interaction.response.send_message(f"Login bem-sucedido! User ID: {user_id}, Personagem: {nome_personagem}")
        else:
            await interaction.response.send_message("Login falhou! Verifique seu nome de personagem e senha.")

class MeuBotao(discord.ui.View):
    @discord.ui.button(label="Registrar", style=discord.ButtonStyle.primary)
    async def Register(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = RegistroModal()
        await interaction.response.send_modal(modal) 
    @discord.ui.button(label="Login", style=discord.ButtonStyle.secondary)
    async def Login(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = LoginModal()
        await interaction.response.send_modal(modal)  

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
        embed_welcome = discord.Embed(title="⚔️ Sua Jornada Começa!", description="Bem-vindo ao seu canal privado.", color=0x00ff00)
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
async def on_ready(): # Removi o 'ctx' pois on_ready não recebe argumentos
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
   

bot.run("MTQ4MTYyOTk4Mjg3ODA3NzEyMQ.GJ6jaL.He5GRoBOoLU_0mJ45PzR-SHMcAYAKYr8vHw7Kw")
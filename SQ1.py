import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
import time

# Load DotENV Files
load_dotenv()

mem1 = 100
mem2 = 100

TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix="!")


# Helper Functions / API

def CoinToss():
    poss = ["odd", "even"]
    rng = random.randint(0, 1)
    return poss[rng]


# end


def bodyPartsFunc():
    rng = random.randint(0, 3)
    bodyParts = ["sua yeule", "din schnolles", "sul front", "dans l'anus"]
    return bodyParts[rng]




rngLol = random.randint(1, 25)


PlayerRecords = {}


async def register(Member: discord.Member):
    if not PlayerRecords.get(f"{Member.name}"):
        plywins = 0
        PlayerRecords.update({f"{Member.name}": plywins})
        channel = await Member.create_dm()
        content = "Hey le gros t rendu dans DB que jpuisse compter tes wins."
        await channel.send(content)
    else:
        pass


async def AddWin(Member: discord.Member):
    plywinsC = PlayerRecords.get(f"{Member.name}")
    print(plywinsC)
    plywinsN = int(plywinsC) + 1
    PlayerRecords.update({f"{Member.name}": plywinsN})












async def Attack(ctx, Player1: discord.Member, Player2: discord.Member):
    await register(Player1)
    await register(Player2)
    #Announcment Embed
    rng2 = random.randint(0, 1)
    probabilityCritical = (1/2 + 1/25 - (1/2 * 1/25)) * 100
    names = [Player1.name, Player2.name]
    updated_embed2 = discord.Embed(title="Fight Annoucment", color=0x0000ff)
    updated_embed2.add_field(name="Retard #1", value=f"{Player1.name}")
    updated_embed2.add_field(name="Retard #2", value=f"{Player2.name}")
    updated_embed2.add_field(name="Probabilité", value=f"{probabilityCritical}% pour {names[rng2]}", inline=False)
    updated_embed2.set_author(name="Crybaby", url="https://github.com/Ticass")
    updated_embed2.set_footer(text=f"SQ1 Fight Club")
    await ctx.channel.send(embed=updated_embed2)
    mem1Health = 100
    mem2Health = 100
    rng = random.randint(0, 2)
    AtkStringPlayer1 = [f"```excel\n{Player1.name} criss ça {bodyPartsFunc()} à {Player2.name} ```",
                        f"```yaml\nOUCH! {Player1.name} yeet ça {bodyPartsFunc()} de {Player2.name}```",
                        f"```js\n {Player1.name} regarde {Player2.name} drette din yeux \n  pi y lui criss une claque {bodyPartsFunc()}```"]

    AtkStringsPlayer2 = [f"```excel\n{Player2.name} criss ça {bodyPartsFunc()} à {Player1.name} ```",
                        f"```yaml\nOUCH! {Player2.name} yeet ça {bodyPartsFunc()} de {Player1.name}```",
                        f"```js\n {Player2.name} criss une claque {bodyPartsFunc()} à {Player1.name}```"]
    while mem1Health > 0 and mem2Health > 0:
        if CoinToss() == "odd" and mem1Health > 0 and mem2Health > 0:
            hit = random.randint(1, 25)
            mem2Health = mem2Health - hit
            DamageTextply1 = str(
                f"""```excel\n{Player2.name} - {hit} HP```""")
            Healthtextply1 = str(
                f"""```css\n{Player1.name}: {mem1Health} HP\n{Player2.name}: {mem2Health} HP```""")
            updated_embed = discord.Embed(title="Combât", color=0x0000ff)
            updated_embed.add_field(name="Degâts Infligés", value=DamageTextply1)
            updated_embed.add_field(name="Vie des joueurs", value=Healthtextply1)
            updated_embed.add_field(name="Log", value=AtkStringPlayer1[rng], inline=False)
            updated_embed.set_author(name="Fight Club", url="https://github.com/Ticass")
            updated_embed.set_footer(text=f"Critical Hit Chance {probabilityCritical}%")
            time.sleep(2)
            await ctx.channel.send(embed=updated_embed)
        elif CoinToss() == "even" and mem1Health > 0 and mem2Health > 0:
            hit = random.randint(1, 25)
            mem1Health = mem1Health - hit
            DamageTextply2 = str(
                f"""```excel\n{Player1.name} - {hit}```""")
            Healthtextply2 = str(
                f"""```css\n{Player1.name}: {mem1Health}\n{Player2.name}: {mem2Health}```""")
            updated_embed = discord.Embed(title="Combât", color=0x0000ff)
            updated_embed.add_field(name="Degâts Infligés", value=DamageTextply2)
            updated_embed.add_field(name="Vie des joueurs", value=Healthtextply2)
            updated_embed.add_field(name="Log", value=AtkStringsPlayer2[rng], inline=False)
            updated_embed.set_author(name="Fight Club", url="https://github.com/Ticass")
            updated_embed.set_footer(text=f"Critical Hit Chance {probabilityCritical}%")
            time.sleep(2)
            await ctx.channel.send(embed=updated_embed)
    else:
        if mem1Health < 1 or mem2Health < 1:
            print(f"Vie du joueur 2: {mem1Health} HP")
            print(f"Vie du joueur 2: {mem2Health} HP")
        if mem1Health > mem2Health:
            Fight_end = discord.Embed(title="Résultats du combat", color=0x0000ff)
            Fight_end.add_field(name="Retard #1", value=f"{Player1.name}")
            Fight_end.add_field(name="Retard #2", value=f"{Player2.name}")
            Fight_end.add_field(name="Vainqueur", value=f"{Player1.name}", inline=False)
            Fight_end.set_author(name="Fight Club", url="https://github.com/Ticass")
            Fight_end.set_footer(text=f"SQ1 Fight Club")
            await ctx.channel.send(embed=Fight_end)
            channel = await Player2.create_dm()
            content = f"Vous avez perdu un combat contre {Player1.name}, \n Criss de noob lol"
            channel2 = await Player1.create_dm()
            content2 = f"Vous avez gagné un combat contre {Player2.name}, \n GG"
            await channel.send(content)
            await channel2.send(content2)
            await AddWin(Player1)
            print(PlayerRecords)
        elif mem1Health < mem2Health:
            Fight_end = discord.Embed(title="Résultats du combat", color=0x0000ff)
            Fight_end.add_field(name="Retard #1", value=f"{Player1.name}")
            Fight_end.add_field(name="Retard #2", value=f"{Player2.name}")
            Fight_end.add_field(name="Vainqueur", value=f"{Player2.name}", inline=False)
            Fight_end.set_author(name="Fight Club", url="https://github.com/Ticass")
            Fight_end.set_footer(text=f"SQ1 Fight Club")
            await ctx.channel.send(embed=Fight_end)
            channel = await Player1.create_dm()
            content = f"Vous avez perdu un combat contre {Player2.name}, \n Criss de noob lol"
            channel3 = await Player2.create_dm()
            content3 = f"Vous avez gagné un combat contre {Player1.name}, \n GG"
            await channel.send(content)
            await channel3.send(content3)
            await AddWin(Player2)
            await ctx.channel.send(embed=Fight_end)
            print(PlayerRecords)
            # await Player1.move_to(discord.VoiceChannel.name("TRANSEXUELS #LGBTQ+"))



@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')





@bot.command()
async def fight(ctx, Player1: discord.Member, Player2: discord.Member):
    await Attack(ctx, Player1, Player2)


bot.run(TOKEN)

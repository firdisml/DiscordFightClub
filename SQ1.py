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


# end


def Damage():
    damage = 0
    for x in bodyPartsFunc():
        if x == "sua yeule":
            damage = 25
        elif x == "din schnolles":
            damage = 50
        elif x == "sul front":
            damage = 15
        elif x == "dans l'anus":
            damage = 20
    return [damage, bodyPartsFunc()]


async def Attack(ctx, Player1: discord.Member, Player2: discord.Member):
    mem1Health = 100
    mem2Health = 100
    playerAttacking = 3
    rng = random.randint(0, 2)
    AtkStringPlayer1 = [f"```\n {Player1.name} veut se battre avec {Player2.name} \n y t'y criss ça {bodyPartsFunc()}```",
                        f"```\n {Player1.name} Est en criss, il pogne {Player2.name} \n  pi y te yeet ça {bodyPartsFunc()}```",
                        f"```\n {Player1.name} regarde {Player2.name} drette din yeux \n  pi y lui criss une claque {bodyPartsFunc()}```"]
    AtkStringsPlayer2 = [
        f"```\n {Player2.name} veut se battre avec {Player1.name} \n y t'y criss ça {bodyPartsFunc()}```",
        f"```\n {Player2.name} Est en criss, il pogne {Player1.name} \n  pi y te yeet ça {bodyPartsFunc()}```",
        f"```\n {Player2.name} regarde {Player1.name} drette din yeux \n  pi y lui criss une claque {bodyPartsFunc()}```"]
    while mem1Health != 0 and mem2Health != 0:
        if CoinToss() == "odd" and mem1Health != 0 and mem2Health != 0:
            mem2Health = mem2Health - 25
            embed = discord.Embed(title="Combât en cours")
            DamageTextply1 = str(
                f"""```css\n {Player2.name} - 25 HP```""")
            Healthtextply1 = str(
                f"""```css\n{Player1.name}: {mem1Health} HP\n{Player2.name}: {mem2Health} HP```""")
            embed.add_field(name="Degâts Infligés", value=DamageTextply1)
            embed.add_field(name="Vie des joueurs", value=Healthtextply1)
            embed.add_field(name="Log", value=AtkStringPlayer1[rng], inline=False)
            embed.set_author(name="Crybaby", url="https://github.com/Ticass")
            embed.set_footer(text=f"SQ1 Fight Club")
            await ctx.channel.send(embed = embed)
            time.sleep(1)
        elif CoinToss() == "even" and mem1Health != 0 and mem2Health != 0:
            embed = discord.Embed(title="Fight Club")
            mem1Health = mem1Health - 25
            DamageTextply2 = str(
                f"""```css\n {Player1.name} - 25```""")
            Healthtextply2 = str(
                f"""```css\n{Player1.name}: {mem1Health}\n{Player2.name}: {mem2Health}```""")
            embed.add_field(name="Place your bets", value=DamageTextply2)
            embed.add_field(name="Health", value=Healthtextply2)
            embed.set_footer(text=f"SQ1 Fight Club")
            embed.set_author(name="Crybaby", url="https://github.com/Ticass")
            embed.add_field(name="Log", value=AtkStringsPlayer2[rng], inline=False)
            await ctx.channel.send(embed=embed)
            time.sleep(1)
    else:
        if mem1Health < 1 or mem2Health < 1:
            await ctx.channel.send(f"""```\nyaml {Player1} LE COMBAT EST TERMINÉ```""")
            print(f"Vie du joueur 2: {mem1Health}")
            print(f"Vie du joueur 2: {mem2Health}")
        if mem1Health > mem2Health:
            await ctx.channel.send(
                f"```\n GRAND CHAMPION INTERNATIONAL (de course) @{Player1} AVEC {mem1Health} HP ```")
            channel = await Player2.create_dm()
            content = f"Vous avez perdu un combat contre {Player1.name}, \n Criss de noob lol"
            await channel.send(content)
            # await Player2.move_to(discord.VoiceChannel.name("TRANSEXUELS #LGBTQ+"))
        elif mem1Health < mem2Health:
            await ctx.channel.send(
                f"```\n GRAND CHAMPION INTERNATIONAL (de course) @{Player2} AVEC {mem2Health} HP ```")
            channel = await Player1.create_dm()
            content = f"Vous avez perdu un combat contre {Player2.name}, \n Criss de noob lol"
            await channel.send(content)
            # await Player1.move_to(discord.VoiceChannel.name("TRANSEXUELS #LGBTQ+"))


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hey {member.name}, Vachier criss de gay !'
    )


@bot.command()
async def fight(ctx, Player1: discord.Member, Player2: discord.Member):
    await Attack(ctx, Player1, Player2)


bot.run(TOKEN)

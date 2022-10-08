import RobloxApi, hashlib, requests, discord, hashlib, random, json, os
from discord.ext.commands import has_permissions, CheckFailure
from discord.ext import commands
from discord.utils import get


client = commands.Bot(command_prefix=".", intents=discord.Intents.all())
token = ""

@client.command(pass_context=True)
async def mines(ctx, gameid, mines=3):
    if not len(gameid) == 36:
        await ctx.send("Invalid gameid.")
        return

    elif mines > 24:
        await ctx.send("Too many mines!")
        return

    hash = str(int(hashlib.sha256(gameid.encode('utf-8')).hexdigest(), 16))[1:]
    print(ctx.message.content, ctx.message.author, ctx.message.author.id)
    choices = list(range(25))
    msg = ["❓❓❓❓❓","❓❓❓❓❓","❓❓❓❓❓","❓❓❓❓❓","❓❓❓❓❓"]
    print("Ok")
    for x in range(0, int(mines)*2, 2):
        print(x, x+2)
        if not x:
            n = int(hash[x : x+2])
        else:
            n = int(hash[x-2 : x])

        n = choices[n % len(choices)]
        choices.remove(n)


        print(n, n // 5, n % 5)

        t = [* msg[n // 5]]
        t[n % 5] = "✅"
        msg[n // 5] = ''.join(t)
        print(msg)

    msg = '\n'.join(msg)

    

    try:
        e = discord.Embed(title=f'Your Prediction', description=msg, color=0x206694)
        e.set_footer(text='BF Smart Bet • https://discord.gg/gcgRMzd8')
        await ctx.send(ctx.message.author.mention, embed=e)
    except:
        pass




client.run(token, bot=True)
import requests
import discord
from discord.ext import commands


client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Bot is ready')


@client.command()
async def price(ctx):
    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {
        "from_currency": "BTC",
        "function": "CURRENCY_EXCHANGE_RATE",
        "to_currency": "INR"
    }

    headers = {
        'x-rapidapi-key': "0b57da549bmshd45808ec9a14981p1ea4d6jsn08d8d2edba0d",
        'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    rate = response.json()[
        'Realtime Currency Exchange Rate']['5. Exchange Rate']

    await ctx.send(f'Bitcoin Exchange Rate in INR: {rate}')

client.run('ODk3NzYzNjM3MjkxMjUzNzYx.YWaZig.xRAgcoJUMjZgvnELu9ogua3ztRk')

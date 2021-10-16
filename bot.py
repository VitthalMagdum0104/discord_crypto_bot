import os

from discord.ext import commands
from pycoingecko import CoinGeckoAPI
from dotenv import load_dotenv


load_dotenv('.env', '')
api_key = os.getenv('API_KEY', '')
client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Bot is ready')


@client.command()
async def price(ctx, symbol, currency):
    coinGecko_client = CoinGeckoAPI()
    rate = coinGecko_client.get_price(
        ids=['bitcoin', 'litecoin', 'ethereum'], vs_currencies=['usd', 'eur'])
    await ctx.send(f'{symbol} in {currency}: {rate[symbol][currency]}')


client.run(api_key)

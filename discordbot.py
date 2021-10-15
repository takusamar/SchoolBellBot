import discord
import asyncio
import sys
import os
from logging import getLogger, StreamHandler, Formatter, INFO
logger = getLogger(__name__)
handler = StreamHandler()
formatter = Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
handler.setLevel(INFO)
logger.setLevel(INFO)
logger.addHandler(handler)
logger.propagate = False

if len(sys.argv) < 3:
    logger.info('Usage: {0} <audio_file> <channel_name>'.format(
        os.path.basename(__file__)))
    sys.exit(0)

AUDIO_FILE = sys.argv[1]
CHANNEL_ID = int(sys.argv[2])

TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

client = discord.Client()
voice_channel = None


async def stop_bot():
    global voice_channel
    if voice_channel:
        await voice_channel.disconnect()
        logger.info('disconnected')
    sys.exit(0)


def on_after(error=None):
    fut = asyncio.run_coroutine_threadsafe(stop_bot(), client.loop)
    try:
        fut.result()
    except:
        pass


async def ring():
    global voice_channel
    logger.info("connecting channel id: {0}".format(CHANNEL_ID))
    channel = client.get_channel(CHANNEL_ID)
    if channel is None:
        logger.error("channel not found: {0}".format(CHANNEL_ID))
        on_after()
    else:
        voice_channel = await channel.connect()
        logger.info("connected {0}".format(channel.name))
        audio_path = os.path.join(os.path.dirname(__file__), AUDIO_FILE)
        audio = discord.FFmpegPCMAudio(audio_path)
        source = discord.PCMVolumeTransformer(audio, volume=0.1)
        logger.info("ring {0}".format(AUDIO_FILE))
        voice_channel.play(source, after=on_after)


@client.event
async def on_ready():
    logger.info('school-bell bot')
    await ring()

client.run(TOKEN)

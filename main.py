import discord
import time
from discord.ext import commands
client = discord.Client()


token = "ODgzNjI2MTg0NzI0ODQwNDk4.YTNYAQ.UYm2VqnhlmPFER4Mltekr0ix_rc" # Insert your 0auth token here
start = "Sex With Social404" # What is the trigger command
megage = "YES" # What message to spam
amount = 69 # How many times should the message repeated
delay = 0.5 # Delay between messages


@client.event
async def on_ready():
    print(f'Ready! Start spamming with {start} \n Go Give Social404 A Sub If You Dont Mind: \n https://www.youtube.com/channel/UCXk0klxbjcVgGvYyKWLgtLg/')

@client.event
async def on_message(message):

    message_number = 0
    if message.content.startswith(f'{start}'):

       while message_number < amount: 
        await message.channel.send(megage)
        message_number += 1
        print(f"Sent message number {str(message_number)}")
        time.sleep(delay)
        
    if message_number == amount: 
        print("Done spamming.")
client.run(token, bot=False)

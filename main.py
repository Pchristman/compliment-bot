import random

import discord
import os

bot = discord.Client()

@bot.event
async def on_message(message):
    message.content = message.content.lower()
    if (str(message.author) == "pootie-tang#1395" or "chappy" in message.content) and str(message.author) != 'Guacamole-Del-Taco#0190':
        x = random.randint(1, 11)
        if x == 1:
            await message.channel.send("Wow Chappy! What have you done to get your body in such good shape? I'm "
                                       "curious to know more about your workout routine. ")
        elif x == 2:
            await message.channel.send("I like the look of Chappy's eyes. It is easy for me to get lost in them. It "
                                       "really makes him look like he has something deep to think about.")
        elif x == 3:
            await message.channel.send("I really appreciate how Chappy is always a gentleman. He is proof that "
                                       "chivalry is not dead. ")
        elif x == 4:
            await message.channel.send("I really appreciate how kind Chappy is. It can be difficult to find a man who "
                                       "is kind. ")
        elif x == 5:
            await message.channel.send("Chappy is the best. He always has an open mind and does not judge people.")
        elif x == 6:
            await message.channel.send("Chappy reminds me of a search engine! I'm always impressed with how much he "
                                       "seems to know about just about everything. ")
        elif x == 7:
            await message.channel.send("Just the sound of Chappy's voice makes me feel safe.")
        elif x == 8:
            await message.channel.send("Chappy always knows how to put a smile on my face, even if I have had a "
                                       "difficult day!")
        elif x == 9:
            await message.channel.send("Has anyone ever met someone as inspiring as Chappy?")
        else:
            await message.channel.send("I'm really impressed with Chappy's self-confidence, particularly in difficult "
                                       "situations. I hope I can learn from that one day. ")

# bot.run(os.getenv("TOKEN"))
bot.run('OTc4NDU0MDYwOTk2ODg2NTg5.GDSKC5.K_El1UdX8VVR4IvLudER7bo2T0BnUiHoJJHnH8')
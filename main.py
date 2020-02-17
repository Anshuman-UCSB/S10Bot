from keep_alive import keep_alive
import discord
import os
from time import time

client = discord.Client()

nuke_last = time()
NUKELIMIT = 240

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

async def printMessage(message):
  print(" > {} sent: {}".format(message.author.name, message.content))

async def commandz(message):#if a command is recognized
  channel = message.channel
  content = message.content
  author = message.author

  #<@!678753562226065437> (command)
  
  command = content[23:]
  if command == "":
    await channel.send("What?")
    return  
  command = command.lower()
  command = command.split()
  if command[0] == "ping":
    await channel.send("Pong!")
  try:
    if command[0] == "nuke":
      target = message.mentions[1]
      print("Nuke activated on {}".format(target))
      command[2] = int(command[2])
      print(command)
      if command[2] < 1 or command[2] > 5:
        raise Exception("Fuck")
      prnit("Valid num")
      if time()-nuke_last < NUKELIMIT:
        await channel.send("Nuke on cooldown...")
        return
      nuke_last = time()
      for i in range(int(command[2])):
        msg = await channel.send(target.mention)
        await msg.delete()
  except:
    await channel.send("Invalid use of message, proper use:")
    await channel.send("{} nuke (target) (count max 5)".format(client.user.mention))
    



@client.event
async def on_message(message):
  await printMessage(message)
  
  if(message.author == client.user):
    return

  if message.content.find(str(client.user.id)) == 3:
    print("Command recognized")
    await commandz(message) #run above method


  channel = message.channel
  #await channel.send("Fuck you, stupid bird.")

  

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)


from keep_alive import keep_alive
import discord
import os
from time import time

client = discord.Client()

nuke_last = -1
NUKELIMIT = 60

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    nuke_last = time()

async def printMessage(message):
  print(" > {} sent: {}".format(message.author.name, message.content))

async def commandz(message):#if a command is recognized
  global nuke_last
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
  print(nuke_last)
  try:
    if command[0] == "nuke":
      target = message.mentions[1]
      print("Nuke activated on {}".format(target))
      command[2] = int(command[2])
      print(command)
      print(command[2])
      if command[2] < 1 or command[2] > 5:
        raise Exception("Fuck")
      
      print(nuke_last)
      print(time())
      elapsed = time()-nuke_last
      print("Elapsed: {}".format(elapsed))
      print("Bruh")
      if time()-nuke_last < NUKELIMIT:
        await channel.send("Nuke on cooldown... {} remaining".format(round(NUKELIMIT-elapsed,1)))
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


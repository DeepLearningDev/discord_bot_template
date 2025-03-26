import os
import crescent, hikari

bot = hikari.GatewayBot(os.environ["TOKEN"], intents=hikari.Intents.ALL)
client = crescent.Client(bot)
# Location of the plugins folder for external bot commands
client.plugins.load_folder("botname.plugins")

# Example in command in main file
@client.include
@crescent.command(description="Ping Value")
async def ping(ctx:crescent.Context) -> None:
  await ctx.respond("Pong")


# Updates the commands
if __name__ == "__main__":
  if os.name != "nt":
    import asynchio
    
    import winloop
    
    asyncio.set_event_loop_policy(winloop.EventLoopPolicy())
    
  bot.run()

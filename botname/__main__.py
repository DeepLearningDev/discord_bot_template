import os
import crescent, hikari

bot = hikari.GatewayBot(os.environ["TOKEN"], intents=hikari.Intents.All)
client = crescent.Client(bot)


@client.include
@client.command(description="Ping Value")
async def ping(ctx:crescent.Context) -> None:
  await ctx.respond("Pong")


if __name__ == "__main__":
  if os.name != "nt":
    import _asyncio
    
    import uvloop
    
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    
  bot.run()

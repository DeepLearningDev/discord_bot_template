# any imports exclusive to the command up here

import crescent
import crescent.plugin
import hikari

plugin = crescent.Plugin[hikari.GatewayBot, None]()

@plugin.include
@crescent.command(name="test", description="This is a test command to add two numbers")
class Hello:
  option1 = crescent.option(
    int,
    description="Select a numeber between 1-10",
    min_value=1,
    max_value=10,
   )
  bonus = crescent.option(
    int,
    description="This is a second non-default option"
    )
  
  async def callback(self, ctx: crescent.Context) -> None:
    output = [self.option1 + self.bonus]
    await ctx.respond(f"{self.option1} + {self.bonus} = {output}")

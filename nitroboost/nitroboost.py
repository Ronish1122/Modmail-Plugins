import discord
from discord.ext import commands
class BoostPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        print(message.type)
        if message.type == discord.MessageType.premium_guild_subscription:
            embed = discord.Embed(title=f"**Nitro Boost**", description=f"Thank you so much for boosting <a:gifhb_nitro:756561976020172910> !", color=0xff0000)
            m = await message.channel.send(embed=embed)
            await m.add_reaction("<a:gifhb_heart:756561858705752134>")
            
def setup(bot):
    bot.add_cog(BoostPlugin(bot))

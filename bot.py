import discord
from discord.ext import commands
from PIL import Image
import io

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def gifify(ctx):
    if not ctx.message.attachments:
        await ctx.send("Attach an image!")
        return

    attachment = ctx.message.attachments[0]
    if not attachment.filename.lower().endswith((".png", ".jpg", ".jpeg")):
        await ctx.send("Please upload a PNG or JPG image.")
        return

    image_data = await attachment.read()
    image = Image.open(io.BytesIO(image_data)).convert("RGBA")

    output = io.BytesIO()
    image.save(output, format="GIF")
    output.seek(0)

    await ctx.send(file=discord.File(fp=output, filename="converted.gif"))

bot.run("YOUR_BOT_TOKEN")

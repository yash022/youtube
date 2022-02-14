// script for youtube discord bot
import pyshorteners
from discord.ext import commands
from pytube import YouTube
import discord
from discord_slash import SlashCommand
import os

bot = commands.Bot(command_prefix = "/")
slash = SlashCommand(bot,sync_commands=True)

@slash.slash(description="with this command you can convert youtbe video into a mp4 video")
async def yt2mp4(ctx, *, videolink):
    try:
        video_parse = YouTube(videolink)
        shorten = pyshorteners.Shortener()
        video_with_audio_hd  = str(video_parse.vid_info).split("'itag': 22,")[1].split(", 'mimeType':")[0].removeprefix(" 'url': '").removesuffix("'")
        embedVar = discord.Embed(title="Your video is ready to be downloaded", description=f"{ctx.author.mention} visit this link to download the video 👇 \n {shorten.tinyurl.short(video_with_audio_hd)}", color=0xf80404)
        await ctx.send(embed=embedVar)
    except Exception as e:
        embedVar = discord.Embed(title="💀 error", description=e, color=0xf80404)
        await ctx.channel.send(embed=embedVar)

@slash.slash(description="with this command you can convert youtbe video into a mp3 audio")
async def yt2mp3(ctx, *, videolink):
    try:
        video_parse = YouTube(videolink)
        shorten = pyshorteners.Shortener()
        video_audio = video_parse.streams.filter(only_audio=True).first().url
        embedVar = discord.Embed(title="Your audio is ready to be downloaded", description=f"{ctx.author.mention} visit this link to download the video 👇 \n {shorten.tinyurl.short(video_audio)}", color=0xf80404)
        await ctx.send(embed=embedVar)

    except Exception as e:
        embedVar = discord.Embed(title="💀 error", description=e, color=0xf80404)
        await ctx.send(embed=embedVar)

@slash.slash(description="with this command you can convert youtbe video information" )
async def videoinfo(ctx, *, videolink):
    try:
        video_parse = YouTube(videolink)
        video_info = f"❇️Title: {video_parse.title} \n👀Views: {video_parse.views}\n⏰Published Time: {video_parse.publish_date}\n🎥Channel Name: {video_parse.author}\n📎Channel Link: {video_parse.channel_url} \n🔗Video Link:{video_parse.watch_url}\n\n⚡️ Searched Powered By Youtube downloader bot"
        embedVar = discord.Embed(title="🔍Video Track Information", description=video_info, color=0xf80404)
        await ctx.send(embed=embedVar)
    except Exception as e:
        embedVar = discord.Embed(title="💀 error", description=e, color=0xf80404)
        await ctx.send(embed=embedVar)
        
        
@slash.slash(description="help" )
async def help(ctx):
    try:
        embedVar = discord.Embed(title="🔍List of all the commands", description="yt2mp4 - with this command you can convert YouTube video into a mp4 video \n yt2mp3 - with this command you can convert YouTube video into a mp3 audio \n videoinfo - with this command you can convert YouTube video information \n", color=0xf80404)
        await ctx.send(embed=embedVar)
    except Exception as e:
        embedVar = discord.Embed(title="💀 error", description=e, color=0xf80404)
        await ctx.send(embed=embedVar)
        
bot.run(os.environ["Token"])

import discord
from discord.ext import commands
from urllib.request import urlopen
import json
import urllib

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=",", intents = intents)



# Get api key from last.fm
apiKey = ""




@bot.command(aliases = ['np'])
async def nowplaying(ctx, lastfmname):
         url_song = f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&nowplaying="true"&user={lastfmname}&api_key={apiKey}&format=json'
         data_song = urllib.request.urlopen(url_song).read().decode()
         obj_song = json.loads(data_song)

         song_image = obj_song['recenttracks']['track'][0]['image'][3]['#text'] # Could be none
         song_artist = obj_song['recenttracks']['track'][0]['artist']['#text']
         song_artist_url = f"https://www.last.fm/music/" + song_artist.replace(" ", "+")
         song_name = obj_song['recenttracks']['track'][0]['name']
         song_album = obj_song['recenttracks']['track'][0]['album']['#text'] # Could be none
         song_url = obj_song['recenttracks']['track'][0]['url']
 


         url_user = f'https://ws.audioscrobbler.com/2.0/?method=user.getinfo&user={lastfmname}&api_key={apiKey}&format=json'
         data_user = urllib.request.urlopen(url_user).read().decode()
         obj_user = json.loads(data_user)

         user_profilepic= obj_user['user']['image'][0]['#text']
         user_playcount = obj_user['user']['playcount']


         embed = discord.Embed(color = ctx.author.color)
         embed.set_author(name = f"Last.fm: {lastfmname}", icon_url=user_profilepic, url = f"https://www.last.fm/user/{lastfmname}")
         embed.set_thumbnail(url = song_image)
         embed.add_field(name = "Track", value = f"[{song_name}]({song_url})", inline = True)
         embed.add_field(name = "Artist", value = f"[{song_artist}]({song_artist_url})", inline= True)
         embed.set_footer(text = f"Total playcount: {user_playcount}/ Album: {song_album}")

         await ctx.send(embed = embed)


bot.run("")

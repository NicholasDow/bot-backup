import os
import random
import time
import discord
import pickle
#maybe use chinese to go into a website and scrape it for something
#import googletrans
import urllib.request
from bs4 import BeautifulSoup

with open("pickled_jokes.txt","rb") as fp:
    jokes = pickle.load(fp)
finra = {' 3 ': 'National Commodities Futures Exam*',
' 5 ': 'Interest Rate Options Exams',
' 6 ': 'Investment Company and Variable Contracts Exam (Mutual Funds Broker/Variable Annuities)',
' 7 ': 'General Securities Representative Exam (Stockbroker)',
' 11 ': 'Assistant Representative Order Processing',
' 15 ': 'Foreign Currency Options Exam',
' 17 ': 'United Kingdom Securities Representative Exam',
' 22 ': 'Direct Participation (Limited partnerships) Exam',
' 30 ': 'NFA Branch Manager Exam',
' 31 ': 'Futures Managed Funds Exam*',
' 32 ': 'Limited Futures Exam - Regulations',
' 37 ': 'Canada Securities Representative Exam - With Options',
' 38 ': 'Canada Securities Representative Exam - No Options',
' 42 ': 'Registered Options Representative Exam',
' 44 ': 'NYSE Arca Options Market Maker Exam',
' 47 ': 'Japanese Module of the General Securities Exam',
' 52 ': 'Municipal Securities Representative Exam',
' 55 ': 'Equity Trader Limited Representative Exam',
' 56 ': 'Proprietary Trader Qualification Exam',
' 57 ': 'Securities Trader Qualification Exam[1]',
' 62 ': 'Corporate Securities Limited Representative Exam',
' 63 ': 'Uniform Securities Agent State Law Exam*',
' 65 ': 'Uniform Registered Investment Adviser Law Exam (RIA)*',
' 66 ': 'Uniform Investment Adviser Combined State Laws Exam (Combined  63  and  65 )',
' 72 ': 'Government Securities Limited Representative',
' 79 ': 'Investment Banking Exam',
' 68 ': '–',
' 82 ': 'Private Securities Offerings Limited Representative',
' 86 ': 'Research Analyst Securities Analysis',
' 87 ': 'Research Analyst Regulations',
' 99 ': 'Operations Professional',
' 4 ': 'Registered Options Principal Exam',
' 9 ': 'General Securities Sales Supervisor Exam Options',
' 10 ': 'General Securities Sales Supervisor Exam General Module',
' 12 ': 'NYSE Branch Manager',
' 14 ': 'NYSE DMM Compliance Official Examination',
' 16 ': 'NYSE Supervisory Analyst',
' 23 ': 'General Securities Principal (Upgrade from 9 and  10 )',
' 24 ': 'General Securities Principal Exam',
' 26 ': 'Investment Company and Variable Contracts Products Principal Exam',
' 27 ': 'Financial and Operations Principal Exam',
' 28 ': 'Financial and Operations Principal Introducing Broker Exam',
' 39 ': 'Direct Participation Programs Principal Exam',
' 51 ': 'Municipal Fund Securities Limited Principal',
' 53 ': 'Municipal Securities Principal Exam'}

client = discord.Client()

first_word = ['purple','sexy', 'pickle', 'cat', 'dog', 'bean', 'burrito', 'italian', 'suasage', 'rhinoceros', 'cheese','Grigorii','Rasputin','dank','shotgun','wang','fucking','fuck','shit','shit for brains','boot','boot-licking','shitty','max','I want to die, ']
second_word = ['wolf', 'platypus', 'cat', 'rick', 'bob', 'steve', 'hamster', 'koala','cheetah', 'dick', 'prawn', 'panther', 'cheese', 'squirrel','Grigorii','Rasputin','penis','shotgun','wang','rick','chicken','addiction','max', 'pokemon', 'dinkel','dingleberg','dongbomp','woop','whip','fwomp','koopa','troopa','dick spaget','yankee','whore','slut']

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, fuck you!'
    )
@client.event
async def on_message_edit(before,after):
    await after.guild.channels.send("edit")

yank = ['the yankee\'s suck', 'You know what\'s great, the Red Sox', 'Why are the New York Yankees starting pitchers like orphans? \n\nBecause they don\'t know where home is!', 'Why do people like driving a car with a Yankees fan?\n\nBecause you can park in the handicap spot!', 'What\'s the difference between a Yankees fan and a baby? \n\nThe baby will stop whining after awhile.']
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    x = str.lower(message.content)
    y = message.channel.send

    with open("stats.txt","a") as f:
        f.write(f"{int(time.time())}\n")

    if 'god bless' in x and ('nick' in x or 'nicholas' in x):
        response = ':man_mage_tone5: ~ Wooosh'
        random.seed()
        name = random.choice(first_word) + ' ' + random.choice(second_word)
        await y(response)
        await message.author.edit(nick=name)
    elif any(i in x for i in finra.keys()):
        output = ''
        for i in finra.keys():
            if i in x:
                output = output + i + " - " + finra[i] + "\n"
        await y(output)
    
    elif 'yankee' in x:
        u = random.choice(yank)
        await y(f"@{message.author},\n{u}")
    
    elif 'csgo' in x: 
        await y("Not to brag, but I'm master in csgo")
    
    elif 'osu' in x: 
        await y("osu, oh my gosu, u play osu")
    elif 'harvard' in x: 
        await y(random.choice(["Not to brag, but I goto Harvard","Non-Harvard people just wouldn't understand", "Peasants", "You would have to go to Harvard to understand", "HE GOES TO HARVARD!!!", "HARVARD?", "Hey, Thomas"]))
    elif 'tufts' in x: 
        await y("I'm sorry")
    elif 'legends' in x or 'leauge' in x: 
        await y(random.choice(["I only play zed mid", "VEEEYYN", "Jack's kidney plays league better than you", "Jeffery could beat you in league on a track pad", "All yasuo mains should burn in hell", "One v One me", "Would Jesus approve"]))
    elif 'ireland' in x or "irish" in x or "trinity" in x:
        await y("The irish are basically just english people with potatoes, right?")
    elif 'jay\'s twitter' in x: 
        await y("Jesus had 12 disciples, not followers. If u knew anything about christianity you’d know Jesus influenced MANY people during his life. Second, population at 0AD was <300mil, which means his ratio was INSANE. kinda like an 8digit follower account rn. pick up a book dumbass")
    elif 'archeage' in x: 
        await y("I would ruin my life to play that game")
    elif 'thomas is a god' in x:
        await y("kys")
    elif 'mental stamina' in x:
        await y("fuck you too")
    elif 'food' in x:
        await y(":dog2:")
    elif 'worms' in x:
        await y("https://preview.redd.it/memc3vbhyb251.gif?format=mp4&s=cbb5aabe1b9e22b382ce00d1b01fe5a2ddaf6110")
    elif 'cops' in x or 'liberals' in x or 'lego' in x:
        await y("https://preview.redd.it/ub8z26wxec251.jpg?width=640&crop=smart&auto=webp&s=345af396bcc92a51206288877cbc2c8071878561")
    elif 'gaming culture' in x or 'gamers unite' in x or 'watch my stream' in x:
        await y("https://i.redd.it/48739m0hkx151.jpg")
    elif 'religion' in x or 'goodness' in x or 'friends' in x:
        await y("https://preview.redd.it/jql1ikbewbz41.png?width=640&crop=smart&auto=webp&s=fa1a854ac608c195ff0a6419d3f1d0fef351f350")
    elif 'wra' in x or 'western reserve' in x or 'reserve academy' in x:
        await y(":clown:")
    elif 'alaska' in x:
        await y(':otter:')
    elif '油腻' in x:
        html_doc = urllib.request.urlopen('https://www.reddit.com/r/okbuddyretard/top/?t=hour').read()
        soup = BeautifulSoup(html_doc)
        random.seed()
        randomLink = random.choice(soup.findAll('img', alt = 'Post image')).get('src')
        await y(randomLink)
    elif 'margret' in x or 'dairy' in x or 'london dairy' in x or 'thatcher' in x or ' ira ' in x:
        await y('https://i.imgur.com/qeO5OeR.jpg')
    elif '米饭' in x:
        usa = []
        html_doc = urllib.request.urlopen('https://www.reuters.com/news/us').read()
        soup = BeautifulSoup(html_doc)
        data = soup.findAll('div', attrs = {'class':'story-content'})
        for div in data:
            links = div.findAll('a')
            for a in links:
                usa.append("https://www.reuters.com/" + a['href'])
        await y(random.choice(usa))
    elif '炒饭' in x:
        tech = []
        html_doc = urllib.request.urlopen('https://www.reuters.com/news/technology').read()
        soup = BeautifulSoup(html_doc)
        data = soup.findAll('div',attrs = {'class':'story-content'})
        for div in data:
            links = div.findAll('a')
            for a in links:
                tech.append("https://www.reuters.com/" + a['href'])
        await y(random.choice(tech))
    elif '医生' in x:
        await y(random.choice(jokes))
    elif 'space' in x:
        await y("We should go to space")
@client.event 
async def on_member_update(before, after):
    if before != after:
        for channel in after.guild.channels:
            if str(channel) == "general":
                await channel.send(f"{before.nick} has changed their name to {after.nick}")
client.run(str(os.environ.get('TOKEN')))
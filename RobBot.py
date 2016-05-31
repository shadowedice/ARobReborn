import discord
import re
import urllib.request as ur
import MagicCard
import Token

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
			
    if message.content.startswith('$alex'):
         await client.send_message(message.channel, 'Alex does suck dick legit.')
		 
	#Magic card parsing portion	 
    cards = re.findall("\[\[([^\[\]]*)\]\]", message.content)
    
    if len(cards) > 10: cards = cards[0:10]
    for i in set(cards):
        print (i);
        j = ur.quote(i)
        card_id = MagicCard.card_check(j)
        if card_id:
            # Builds the post
            imgurl = "http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=%s&type=card&.jpg" % (card_id)
            #imgname = "mtgimgs/" + card_id + ".jpg"
            imgname = "mtgcard.jpg"
            ur.urlretrieve(imgurl, imgname)
            reply = MagicCard.card_text("http://gatherer.wizards.com/Pages/Card/Details.aspx?name=%s" % j)
            await client.send_file(message.channel, imgname, content=reply)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
	
client.run(Token.get_token())
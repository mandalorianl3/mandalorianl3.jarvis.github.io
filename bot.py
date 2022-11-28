import discord
import responses
import classes

# sends message to response handler
async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(message.author, user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

# runs in real time when bot is active
def run_discord_bot():
    # this is all bot set up. DO NOT TOUCH !!!
    TOKEN = 'MTA0MDY3MTAxOTgzNDI4MjAyNA.GU_gh9.B0pjBsUBCPSnJmhOCyRXJ1tUTQbdk_sVsEW6Z0'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    # bot init
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    # event = message being sent in the server
    @client.event
    async def on_message(message):
        # makes sure the bot doesn't respond to itself
        if message.author == client.user:
            return

        # message contents and attributes
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # prints message in pycharm console
        print(f'{username} said: "{user_message}" ({channel})')

        # checks to see if message is for bot. need to add more for bot_channel
        if user_message[0] == '%':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=False)

    # tells the bot to go online. DON'T TOUCH !!
    client.run(TOKEN)
import discord
import responses

import stoic

if __name__ == '__main__':
    stoic.run_discord_bot()

# This is the unique identifier for the bot
TOKEN = ''

# Function that handles sending the user a message
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        # This line sends the response to the user who sent the message
        # Depending on the boolean parameter, it will send public message or private
        await message.author.send(response) if is_private else await message.channel.send(response)

    # If there are any errors, this is just prints an exception message in the console for debugging
    except Exception as e:
        print(e)


def run_discord_bot():

    TOKEN = ''

    # This just allows/permits the bot to handle the messages
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    # Once the bot is running, sends message to console and a welcome message in the channel
    async def on_ready():
        print(f'{client.user} is running!')
        channel = client.get_channel(1118577601565429941)
        await channel.send("Hello, I am the Stoic bot. Type '!help' to learn more about me.")

    @client.event
    async def on_message(message):
        # Checks the author of the message received is the bot itself. If it is, the function immediately returns,
        # effectively ignoring messages sent by the bot. This prevents the bot from responding to its own messages
        # and getting stuck in a loop
        if message.author == client.user:
            return

        # These lines extract relevant information from the received message, such as the username of the author,
        # the content of the message, and the channel where it was sent. This information can then be used for
        # further processing or responding to the message.
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # This stuff will be in the console
        print(f'{username} said: "{user_message}" ({channel})')

        # Puts the message in private DM if the prefix requirement is met
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)

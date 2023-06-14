import random

quotes = ['"The more we value things outside our control, the less control we have."  - Marcus Aurelius',
          '"You have power over your mind – not outside events. Realize this, and you will find strength."  - Marcus Aurelius',
          '"The best revenge is not to be like your enemy."  - Marcus Aurelius',
          '"External things are not the problem. It’s your assessment of them. Which you can erase right now"  - Marcus Aurelius',
          '"When you arise in the morning, think of what a precious privilege it is to be alive – to breathe, to think, to enjoy, to love."  - Marcus Aurelius',
          '"Waste no more time arguing about what a good man should be. Be one."  - Marcus Aurelius',
          '"We suffer more often in imagination than in reality."  - Seneca',
          '"How does it help…to make troubles heavier by bemoaning them?"  - Seneca',
          '"While we wait for life, life passes."  - Seneca',
          '"A ship should not ride on a single anchor, nor life on a single hope."  - Epictetus',
          '"It is the nature of the wise to resist pleasures, but the foolish to be a slave to them"  - Epictetus',
          '"We have two ears and one mouth so that we can listen twice as much as we speak."  - Epictetus',
          '"Any person capable of angering you becomes your master; he can anger you only when you permit yourself to be disturbed by him"  - Epictetus',
          '"He is a wise man who does not grieve for the things which he has not, but rejoices for those which he has"  - Epictetus',
          '"Man conquers the world by conquering himself."  - Zeno'
          ]

used_quotes = []

def handle_response(message: str) -> str:
    p_message = message.lower()

    global used_quotes

    if message == 'roll':
        # So if all the quotes are used, it will empty the used quotes list
        if len(used_quotes) == len(quotes):
            used_quotes = []

        # Makes a new list by taking the difference between the two arrays. The random.choice selects from this list
        # and adds it to the used quotes list.
        remaining_quotes = list(set(quotes) - set(used_quotes))
        random_quote = random.choice(remaining_quotes)
        used_quotes.append(random_quote)
        return random_quote

    if p_message == '!help':
        return "`To get a random quote from a stoic philosopher, type 'roll'. Want your quotes to be in a private DM? Put a question mark before roll!`"


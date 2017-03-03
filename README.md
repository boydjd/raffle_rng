Summary:
========
raffle_rng is a reddit bot created with the praw 4 api wrapper that replies to mentions with a random integer within the limits defined by the comment that calls the bot. 

If the bot is mentioned like this: /u/botname 30 it will reply with a number between 1 and 30.
By default that text is: "The winner is: N"
  
Setup Instructions:
========

1. Install python (I used 2.75)
1. Install PRAW 4 via pip: https://praw.readthedocs.io/en/latest/getting_started/installation.html
1. Create reddit app here: https://www.reddit.com/prefs/apps/
1. Write down client_id, client_secret
1. Create praw.ini file, define [botname] section: http://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html
1. Input client_id, client_secret, username and password in [botname] section within praw.ini
1. Modify user_agent line to be unique
1. Modify raffle_reply text as necessary
1. Create a scheduled task to run the raffle_rng.py script as necessary. Be mindful of Reddit's 10 minute throttle for low-karma accounts.

#!/usr/bin/python

import time
import praw
import random
import math
import hashlib
import platform

print "STARTING RAFFLE-BOT..."

# Current version
version = "2.0.2"

# Repository URL
url = "https://github.com/diversionmary/raffle_rng"

# Instructions on how to verify
verify_url = "https://github.com/diversionmary/raffle_rng/blob/master/VERIFY.md"

# Modify the user agent string to something unique
user_agent = "raffle_rng bot {} by diversionmary".format(version)

# Define a section for this bot within your local copy of praw.ini: 
# http://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html
reddit = praw.Reddit('botname', user_agent=user_agent)

# Automatically grabs the username of the bot
username = "/u/{}".format(reddit.user.me())

# Error reply message
error_reply = """Call the bot with total slots greater than 0 like this: {} 20 

*View the {} source code at {}*""".format(username, version, url)

def parse_to_integer(string):
    num_slots = 0
    try:
        num_slots = int(string)
    except ValueError:
        pass
    return num_slots

# Get random number with seed
def get_random_value(eventual_max, seed):
    # Minimum value
    min = 0
    # Maximum value
    max = (eventual_max * math.pow(10, 6)) - 1
    print "min: {}, max: {}".format(min, max)
    # Set our random seed
    random.seed(seed)
    # Get our random number
    return random.randint(min, max)

# turn larger random number into a slot number
def reduce_random_number(slots, num):
    # We want the number to start at 1
    # and go to equal the number of slots
    # and not 0 to SLOTS-1
    # The +1 gives us that
    return num % slots + 1

def get_seed():
    # This will get our random seed
    # It is the current time in ms
    # plus a random number hashed with SHA1
    preseed = str(time.time() + random.random())
    return hashlib.sha1(preseed).hexdigest()
    
# Get unread mentions
for mention in reddit.inbox.unread(limit=None):
    
    # Get first two words from body of message if available
    comment_word_list = mention.body.split(" ")
    word1 = str(comment_word_list[0])
    total_slots = 0
    if word1 == username and len(comment_word_list) == 2:
        total_slots = parse_to_integer(comment_word_list[1])
    
    # If less than two words, or if the first word isn't our bot's reddit 
    # username, mark message read and move on
    elif word1 != username:
        print "Not a raffle call, ignore"
        mention.mark_read()
        break

    # If the first item in the list is only the bot's name reply with 
    # instructions
    if word1 == username and len(comment_word_list) < 2:
        print "Bad raffle call, reply"
        mention.reply(error_reply)
        mention.mark_read()
        break

    # If the first item in the list is the bot's name, and the slot number is 
    # invalid, reply with instructions
    elif word1 == username and total_slots <= 0:
        print "Bad raffle call, reply"
        mention.reply(error_reply)
        mention.mark_read()
        break
    
    # Randomly determine a winner from the slot range and reply
    if total_slots > 0:
        # Get our seed
        seed = get_seed()
        # Get that large random number using the seed
        large_random = get_random_value(total_slots, seed)
        # Modulus the large random number to give us our winner
        winner_index = reduce_random_number(total_slots, large_random)
        winner = str(winner_index)
        direct_verify = "http://verify.diversionmary.com/index.py?slots={}&seed={}".format(total_slots, seed)
        raffle_reply = """# The winner is: {}
        
^^Seed: ^^[{}]({})    
^^Random ^^Number: ^^{} ^^| 
^^Modulus: ^^{} ^^| 
^^Python: ^^{}    
View the {} source code on [github]({})
""".format(winner, 
            seed, direct_verify, 
            large_random, 
            total_slots, 
            platform.python_version(),
            version, url)
            
        mention.reply(raffle_reply)
        print(winner)
        mention.mark_read()

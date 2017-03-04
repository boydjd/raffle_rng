#!/usr/bin/python
import time
import praw
import random

print "STARTING RAFFLE-BOT..."

# Current version
version = "1.5"

# Modify the user agent string to something unique
user_agent="raffle_rng bot" + version + " by diversionmary make this part unique"

# Define a section for this bot within your local copy of praw.ini: http://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html
reddit = praw.Reddit('raffle_rng', user_agent=user_agent)

# Automatically grabs the username of the bot
username = "/u/" + str(reddit.user.me())

# Error reply message
error_reply = "Call the bot with total slots greater than 0 like this: " + username + " 20 \n \n *View the " + version + " source code at https://github.com/diversionmary/raffle_rng*"

def parse_to_integer(string):
    num_slots = 0
    try:
        num_slots = int(string)
    except ValueError:
        pass
    return num_slots

# Get unread mentions
for mention in reddit.inbox.unread(limit=None):
	
	# Get first two words from body of message if available
	comment_word_list = mention.body.split(" ")
	word1 = str(comment_word_list[0])
	if len(comment_word_list) >= 2:
		word2 = parse_to_integer(comment_word_list[1])
	
	# If less than two words, or if the first word isn't our bot's reddit username, mark message read and move on
	elif word1 != username:
		print "Not a raffle call, ignore"
		mention.mark_read()
                break

        # If the first item in the list is the bot's name and that's it reply with instructions
        if word1 == username and len(comment_word_list) < 2:
                print "Bad raffle call, reply"
                mention.reply(error_reply)
                mention.mark_read()
                break

	# If the first item in the list is the bot's name, and the slot number is invalid reply with instructions
	elif word1 == username and word2 <= 0:
		print "Bad raffle call, reply"
		mention.reply(error_reply)
		mention.mark_read()
		break
	
	# If we made it this far, turn word2 into total slots
	total_slots = 0
	total_slots = word2
	
	# Randomly determine a winner from the slot range and reply
	if total_slots > 0:
		winner = str(random.randint(1, total_slots))
		raffle_reply = "The winner is: " + winner + "\n \n *View the " + version + " source code at https://github.com/diversionmary/raffle_rng*"
		mention.reply(raffle_reply)
		print(winner)
		mention.mark_read()
	

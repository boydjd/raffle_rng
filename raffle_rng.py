#!/usr/bin/python
import time
import praw
import random

print "STARTING RAFFLE-BOT..."

# Current version
version = "1.4"

# Modify the user agent string to something unique
user_agent='raffle_rng bot 1.0 by diversionmary make this unique'

# If you're authenticating using praw.ini uncomment the next line:
reddit = praw.Reddit('botname', user_agent=user_agent)

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
	
	# Get first two words from body of message
	comment_word_list = mention.body.split(" ")
	word1 = str(comment_word_list[0])
	word2 = parse_to_integer(comment_word_list[1])
	
	# If the first item in the list is the bot's name, and the second item isn't an int reply with instructions
	if word1 == username and word2 <= 0:
		print "Bad raffle call, reply"
		print str(mention.body)
		print word1
		print username
		print word2
		print isinstance(word2, (int, long))
		mention.reply(error_reply)
		mention.mark_read()
		break

	# If the first item in the list isn't the bot's name, ignore
	elif word1 != username:
		print "Not a raffle call, ignore"
		print str(mention.body)
		print word1
		print username
		print word2
                mention.mark_read()
                break
	
	# If we made it this far, turn the second item into an integer
	total_slots = 0
	total_slots = word2
	
	# Randomly determine a winner from the slot range and reply
	if total_slots > 0:
		winner = str(random.randint(1, total_slots))
		raffle_reply = "The winner is: " + winner + "\n \n *View the " + version + " source code at https://github.com/diversionmary/raffle_rng*"
		mention.reply(raffle_reply)
		print(winner)
		mention.mark_read()
	

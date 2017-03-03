#!/usr/bin/python
import time
import praw
import random

print "STARTING RAFFLE-BOT..."

# Current version
version = "1.3"

# Modify the user agent string to something unique
user_agent='raffle_rng bot 1.0 by diversionmary make this unique'

# If you're authenticating using praw.ini uncomment the next line:
reddit = praw.Reddit('botname', user_agent=user_agent)

# Automatically grabs the username of the bot
username = str(reddit.user.me())

# Error reply message
error_reply = "Call the bot with total slots greater than 0 like this: " + username + " 20 \n \n *View the " + version + " source code at https://github.com/diversionmary/raffle_rng*"

# parse_to_integer turns strings into integers
def parse_to_integer(string):
    num_slots = 0
    try:
        num_slots = int(string)
    except ValueError:
	pass
    return num_slots

# Get unread mentions
for mention in reddit.inbox.unread(limit=None):
	# Turn the body of the message  into a list of strings
	comment_word_list = mention.body.split(" ")
	# If the first item in the list isn't the bot's name, and the second item isn't an integer, break and mark as read
	if len(comment_word_list) >2 or comment_word_list[0] !=username and parse_to_integer(comment_word_list[1]) <= 0:
		print "Not a raffle call"
		print comment_word_list[1]
		mention.mark_read()
		break
	total_slots = 0
	for word in comment_word_list:
	# Parses any number strings in the comment to integers
		slots = parse_to_integer(word)
		if slots > 0 and total_slots == 0:
			total_slots = slots
		else:
			pass
	# Randomly determine a winner from the slot range and reply
	if total_slots != 0:
		winner = str(random.randint(1, total_slots))
		raffle_reply = "The winner is: " + winner + "\n \n *View the " + version + " source code at https://github.com/diversionmary/raffle_rng*"
		mention.reply(raffle_reply)
		print(winner)
		mention.mark_read()

#!/usr/bin/python
import time
import praw
import random

print "STARTING RAFFLE-BOT..."

botname="/u/raffle_rng_test"
user_agent='raffle_rng bot 1.0 by diversionmary make this unique'

#If you're authenticating using praw.ini uncomment the next line:
reddit = praw.Reddit('botname', user_agent=user_agent)

#If you're not using praw.ini uncomment the next line and fill in the authentication values:
#reddit = praw.Reddit(user_agent=user_agent, client_id='put client_id here', client_secret='put client_secret here', username='put reddit username here', password='put password here')
			
#Reply if error
error_reply = "Call the bot with total slots greater than 0 like this: " + botname + " 20 \n \n *View the source code at https://github.com/diversionmary/raffle_rng*"

test_reply = "This is an unread item, but not a mention"

#parse_to_integer turns strings into integers
def parse_to_integer(string):
    num_slots = 0
    try:
        num_slots = int(string)
    except ValueError:
        pass
    return num_slots

#If you want this script to be TSR uncomment the next line. If you do, add another indent to lines 32 through 60
#while True:

#Get unread mentions
for mention in reddit.inbox.unread(limit=None):
	comment_word_list = mention.body.split(" ")
	if mention.body.split(" ")[0] <> botname:
		break
	elif len(comment_word_list) !=2:
		mention.reply(error_reply)
		mention.mark_read()
		break
	total_slots = 0
	for word in comment_word_list:
	# Parses any number strings in the comment to positive integers
		slots = parse_to_integer(word)
		if slots > 0 and total_slots == 0:
			total_slots = slots
		elif slots <= 0 and total_slots == 0:
			mention.reply(error_reply)
                	mention.mark_read()
                	break 
		else:
			pass
	# If a slot total was included, randomly determines a winner from the slot range
		if total_slots != 0:
			winner = random.randint(1, total_slots)
			raffle_reply = "The winner is: " + str(winner) + "\n \n *View the source code at https://github.com/diversionmary/raffle_rng*"
			mention.reply(raffle_reply)
			print(raffle_reply)
			mention.mark_read()

#If you want this script to be a TSR uncomment the next two lines and indent them once as noted above.
#print "Starting 10 minute sleep before next run."
# time.sleep(600)

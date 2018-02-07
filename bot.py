from __future__ import print_function
import os
import time
import re
import datetime
from slackclient import SlackClient
from pytz import timezone

# Tutorials
# https://www.fullstackpython.com/blog/build-first-slack-bot-python.html
# http://pfertyk.me/2016/11/automatically-respond-to-slack-messages-containing-specific-text/

# instantiate Slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None


def remind():
    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel='test-coffee-break-bot',
        text='@channel It is time for coffee break!',
        link_names=True
    )

# constants
RTM_READ_DELAY = 20 # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]

        # remind when?
        # It is Tuesday, Wednesday, Thursday, or Friday
        amsterdam = timezone('Europe/Amsterdam')
        correct_day = False
        now = datetime.datetime.now()
        weekday = amsterdam.localize(now).strftime('%w')
        if weekday in (2, 3, 4, 5):
            correct_day = True

        # It is about three o'clock
        correct_time = False
        hour = int(amsterdam.localize(now).strftime('%H'))
        minutes = int(amsterdam.localize(now).strftime('%M'))
        if (hour == 14 and minutes >= 55) or (hour == 15 and minutes <= 5):
            correct_time = True

        if correct_day and correct_time:
            print('Reminding!')
            remind()
        else:
            print ('Not reminding!')

    else:
        print("Connection failed. Exception traceback printed above.")

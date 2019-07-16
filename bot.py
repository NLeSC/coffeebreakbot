from __future__ import print_function
import os
import time
import re
import datetime
from slackclient import SlackClient
from pytz import timezone
import pytz

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
        channel='general',
        text='@here It is time for a coffee break!',
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

        # timezone conversion solution from https://stackoverflow.com/questions/4563272/convert-a-python-utc-datetime-to-a-local-datetime-using-only-python-standard-lib
        amsterdam = timezone('Europe/Amsterdam')
        now = datetime.datetime.utcnow()
        amsterdam_now = now.replace(tzinfo=pytz.utc).astimezone(amsterdam)

        print('The utc time is {}'.format(now.strftime('%H:%M:%S')))
        print('The time in Amsterdam is {}'.format(amsterdam_now.strftime('%H:%M:%S')))

        # remind when?
        # It is Tuesday, Wednesday, Thursday, or Friday
        correct_day = False
        weekday = int(amsterdam_now.strftime('%w'))
        if weekday in (1, 2, 3, 4, 5):
            correct_day = True

        if correct_day:
            print('The day is correct for reminding')

        # It is about three o'clock
        correct_time = False
        hour = int(amsterdam_now.strftime('%H'))
        minutes = int(amsterdam_now.strftime('%M'))
        if (hour == 14 and minutes >= 25) or (hour == 14 and minutes <= 35):
            correct_time = True

        if correct_time:
            print('The time is correct for reminding')

        if correct_day and correct_time:
            print('Reminding!')
            remind()
        else:
            print ('Not reminding!')

    else:
        print("Connection failed. Exception traceback printed above.")

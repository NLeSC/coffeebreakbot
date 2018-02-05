import os
import time
import re
from slackclient import SlackClient

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
        while True:
            #command, channel = parse_bot_commands(slack_client.rtm_read())
            #if command:
            #    handle_command(command, channel)
            print starterbot_id
            remind()
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
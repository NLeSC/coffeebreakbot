# Coffee Break Bot

A very simple slack bot that reminds you to have a coffee break (at 14:30 Mondays until Fridays).
Editing
## Using on Heroku

* [Add config var](https://devcenter.heroku.com/articles/config-vars) for the SLACK_BOT_TOKEN (`export SLACK_BOT_TOKEN=xxxxxxxxx`)
* Deploy: `git push heroku master`
* Test bot: `heroku run python bot.py`
* [Add scheduled task](https://devcenter.heroku.com/articles/scheduler) (using the heroku dahsboard) (you have to do this once to start, and then every time the clock is adjusted from summer to winter time or vice versa)
* Check the logs: `heroku logs`

[What to put in the Procfile](https://github.com/michaelkrukov/heroku-python-script).

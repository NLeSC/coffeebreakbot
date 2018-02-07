# Coffee Break Bot

A very simple slack bot that reminds you to have a coffee break (at 15:00 Tuesdays until Fridays).

## Deploying on Heroku

* [Add config var](https://devcenter.heroku.com/articles/config-vars) for the SLACK_BOT_TOKEN
* Deploy: `git push heroku master`
* Test bot: `heroku run python bot.py`
* [Add scheduled task](https://devcenter.heroku.com/articles/scheduler) (using the heroku dahsboard) (you have to do this only once)

[What to put in the Procfile](https://github.com/michaelkrukov/heroku-python-script).

# Seriniteabot
Angry Tubby?
<p align="center">
  <img src="./images/angly_tubby.png" width="350" title="angry tubby?">
</p>

# How it works
There are 2 main files in this repository: `main.py` and `main.yml`.
The `main.py` file contains the logic of the bot and the `main.yml` contains instructions to setup the CI pipeline for github.
The `main.yml` is based on the standard template provided by GitHub.
```
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
```
The above code indicates that the set of instructions provided will trigger on every push and an accepted pull__request.
```
workflow_dispatch:
  schedule:
    - cron: '0 */6 * * *'
```
This peice of code indicates that the workflow dispatch is scheduled for every six hours.
For more information on cron visit https://crontab.guru/.
This part of code basically helps keep the bot up 24x7. The base code is under a event loop, so it doesn't terminate and Github tends to kill any processes that run for more than 6hrs, so this code retriggers the CI pipline after every six hours.
```
env: # Or as an environment variable
  BOT_TOKEN: ${{ secrets.BOT_TOKEN }}
run: |
  echo Add other actions to build,
  echo test, and deploy your project.
  echo "$BOT_TOKEN"
  pip install discord
  pip install python-dotenv
  python main.py
```
The above code are the main set of instructions that are to be run by the bot.
First the `BOT_TOKEN`, the repo secret(provided by discord), has to be loaded as an enviroment variable so that the python program can have access to it.

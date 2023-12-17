# discord.py-boilerplate

## About
This is a boilerplate for discord.py bots. It has a basic command handler and a basic event handler. It also has a basic ping command. This is meant to be a starting point for discord.py bots.

## Features
- cog system
- basic ping command
- hot reload(dont have to restart bot on each change)
- jishaku debugging cog
- comments for easy explenation
## How to use
1. Clone repo with `git clone https://github.com/CloudyDaKing/discord.py-boilerplate.git`
2. Install requirements with `pip install -r requirements.txt`
3. Create file named .env
4. Add `TOKEN=your_token` to .env file
5. Run bot with `py main.py` for windows or `python3 main.py` for linux
6. when you create a new command it will need to be synced to discord with !jsk sync
7. Enjoy your new bot!

## How to add commands
Multiple commands can be added to the same file for commands under the same category. If you want to make a new cog make a new file in the cogs folder, copy ping.py over and change acordingly


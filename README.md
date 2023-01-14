# mandalorianl3.jarvis.github.io

Hi :] This code was made entirely by Megan Lang!

If you try to run this code as is, it won't work because the token is outdated! This is a safety feature employed by Discord. If you are viewing this and wish
to run this code, please email me and I will send you the current token. If you do not have my email already, please do not contact me.

A basic description of this program: 
1. The main.py code calls the run_bot function, which is stored in bot.py. This is the active run-time function.
2. Every time a message is sent in a text channel, it is logged, and scanned for the '%' sign at position 0, which signals a bot command. All other messages are ignored.
3. The command is then sent to responses.py and is parsed through. Based on command contents, the response will vary. 
4. A response is eventually determined and returned back to the bot.py function, wherein the bot will respond in the text channel.

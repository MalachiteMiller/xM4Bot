import re

HOST = "irc.twitch.tv"
PORT = 6667
NICK = "xm4bot"
PASS = "oauth:yehjncqvxs8g5dvzm2bfl8w5lderte"
CHAN = "#pandahusky1"
CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
RATE = (80/30)

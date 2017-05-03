#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telebot import TeleBot
from esource import ESource
from boorucmd import BooruCommand
from staticcmd import StaticCommand
from gbsource import GelbooruSource
import socket

bot = TeleBot(
	'YOUR TELEGRAM API KEY',
	'YOUR TELEGRAM BOT NAME/PREFIX',
	{
		'yiff': BooruCommand(ESource('https://e621.net', None, None, 6)),
		'furry': BooruCommand(ESource('https://e926.net', None, None, 6)),
		'agnph': StaticCommand('AGNPH is upgrading their gallery, and the API is not yet available. Therefore this command has been temporarily disabled.'),
		'r34': BooruCommand(GelbooruSource('http://rule34.xxx')),
		'kona': BooruCommand(ESource('http://konachan.com')),
		# From RaithSphere's PawPad bot - thanks!
		'sakuga': BooruCommand(ESource('https://sakuga.yshi.org')),
		'fbooru': BooruCommand(GelbooruSource('http://furry.booru.org/')),
		'sbooru': BooruCommand(GelbooruSource('http://safebooru.org/')),
		'ping': StaticCommand(['Rawr~', 'Meow!', 'Woof woof!', 'Murr~', 'o///o', 'pong' '*poke*', 'Se... senpai!']),
		'about': StaticCommand('e621bot by @socram8888.\n\nFull source code available at [GitHub](https://github.com/socram8888/e621bot/).'),
		'e621botserver': StaticCommand('Bot is running at %s' % socket.getfqdn())
	}
)

bot.run_main()

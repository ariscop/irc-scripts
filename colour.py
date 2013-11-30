import xchat
import random
import shelve
import sys
import os

#Xchat stuff
__module_name__ = "colour"
__module_version__ = "0.2"
__module_description__ = "Colour Script"

xchatdir = xchat.get_info("xchatdir");
storepath = xchatdir + os.sep
sys.path.append(storepath + "scripts")

#local modules
#import flip

store = shelve.open(storepath + "colour.db")

def onUnload(arg):
	store.close()

def colour(fore, back):
	return "\x03%02d,%02d" % (fore, back)

def onMessage(word, word_eol, userdata):
	chan = xchat.get_info("channel")
	
	if not (chan in store) or \
			store[chan+"_on"] != True or \
			word_eol[0].find('\x03') != -1:
		return xchat.EAT_NONE
		
	xchat.command("msg " + chan + " " + colour(*store[chan]) + word_eol[0])
	return xchat.EAT_XCHAT

def onMe(word, word_eol, userdata):
	chan = xchat.get_info("channel")
	
	if not (chan in store) or \
			store[chan+"_on"] != True or \
			word_eol[0].find('\x03') != -1:
		return xchat.EAT_NONE
	
	xchat.command("me " + colour(*store[chan]) + word_eol[1])
	return xchat.EAT_XCHAT

def onColour(word, word_eol, userdata):
	chan = xchat.get_info("channel")
	
	if word[1] == "set":
		store[chan] = [int(word[2]), int(word[3])]
		store[chan+"_on"] = True
	
	elif word[1] == "unset":
		del store[chan]
		del store[chan+"_on"]
	
	elif word[1] == "on":
		store[chan+"_on"] = True
	
	elif word[1] == "off":
		store[chan+"_on"] = False
	
	elif word[1] == "get":
		xchat.prnt(store(chan))
	
	elif word[1] == "list":
		keys = store.keys()
		keys.sort()
		for x in keys:
			xchat.prnt(str(x)+": "+str(store[x]))
	
	else:
		xchat.prnt("valid commands are set get and list")
	
	store.sync()


def onRainbow(word, word_eol, userdata):
	chan = xchat.get_info("channel")

	out = "msg " + chan + " "
	word.remove(word[0])
	fore = int(round(random.uniform(1, 16)))

	for x in word:
		if fore == 1:
			fore = 2;

		out += colour(fore, 1) + x + " "
		fore = (fore + 1) % 16
	
	xchat.command(out)
	return xchat.EAT_XCHAT


def onRainbowChar(word, word_eol, userdata):
	chan = xchat.get_info("channel")

	out = "msg " + chan + " "
	word.remove(word[0])
	fore = int(round(random.uniform(1, 16)))

	for x in word_eol[1]:
		if fore == 1:
			fore = 2;
		out += colour(fore, 1) + x
		fore = (fore + 1) % 16
	
	xchat.command(out)
	return xchat.EAT_XCHAT


def onRainbowDash(word, word_eol, userdata):
	chan = xchat.get_info("channel")
	
		 #4, 7, 8, 9, 11, 6, 13
	rd = [4, 7, 8, 9, 3, 6]
	bg = 2;
	
	out = "msg " + chan + " "
	word.remove(word[0])
	i = int(round(random.uniform(0, 5)))

	for x in word_eol[1]:
		out += colour(rd[i], bg) + x
		i = (i + 1) % len(rd)
		if i == 0:
			col = rd[len(rd)-1]
			#minimum distance of 2 betwene random colours
			while col == rd[0]:
				random.shuffle(rd)
	
	xchat.command(out)
	return xchat.EAT_XCHAT

def onRainbowDashMe(word, word_eol, userdata):
	chan = xchat.get_info("channel")
	
		 #4, 7, 8, 9, 11, 6, 13
	rd = [4, 7, 8, 9, 3, 6]
	bg = 2;
	
	out = "me "
	word.remove(word[0])
	i = int(round(random.uniform(0, 5)))

	for x in word_eol[1]:
		out += colour(rd[i], bg) + x
		i = (i + 1) % len(rd)
		if i == 0:
			col = rd[len(rd)-1]
			#minimum distance of 2 betwene random colours
			while col == rd[0]:
				random.shuffle(rd)
	
	xchat.command(out)
	return xchat.EAT_XCHAT


def onRainbowBackground(word, word_eol, userdata):
	chan = xchat.get_info("channel")
	
		 #4, 7, 8, 9, 11, 6, 13
	rd = [4, 7, 8, 9, 3, 6]
	bg = 0;
	
	out = "msg " + chan + " "
	word.remove(word[0])
	i = int(round(random.uniform(0, 5)))

	for x in word_eol[1]:
		out += colour(bg, rd[i]) + x
		i = (i + 1) % len(rd)
		if i == 0:
			col = rd[len(rd)-1]
			#minimum distance of 2 betwene random colours
			while col == rd[0]:
				random.shuffle(rd)
	
	xchat.command(out)
	return xchat.EAT_XCHAT

"""
def onFlip(word, word_eol, userdata):
	sirFlip = u" (\u256F\u00B0\u25A1\u00B0\uFF09\u256F\uFE35 "

	out = u"msg " + xchat.get_info("channel") + sirFlip
	if word[1] == "table":
		out += u"\u253B\u2501\u253B"
	else:
		out += flip.flipText(word_eol[1], rev=True)
	xchat.command(out.encode("utf8"))
	return xchat.EAT_NONE
"""


#handle normal messages
xchat.hook_command("", onMessage)
xchat.hook_command("me", onMe)

#random colours
xchat.hook_command("rainbow", onRainbow)
xchat.hook_command("rainbowchar", onRainbowChar)

#RAINBOW DASH :D
xchat.hook_command("rainbowdash", onRainbowDash)
xchat.hook_command("rd", onRainbowDash)
xchat.hook_command("rdme", onRainbowDashMe)

#RAINBOW BACKGROUND :D
xchat.hook_command("rb", onRainbowBackground)

#Colour managment
xchat.hook_command("colour", onColour)

#Flip text
#xchat.hook_command("flip", onFlip)

xchat.hook_unload(onUnload)

xchat.prnt("Colour script started")

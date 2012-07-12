#FLIPTABLES

flipTable={ u"a": u"\u0250", \
			u"b": u"q", \
			u"c": u"\u0254", \
			u"d": u"p", \
			u"e": u"\u01DD", \
			u"f": u"\u025F", \
			u"g": u"\u0183", \
			u"h": u"\u0265", \
			u"i": u"\u0131", \
			u"j": u"\u027E", \
			u"k": u"\u029E", \
			u"m": u"\u026F", \
			u"n": u"u", \
			u"r": u"\u0279", \
			u"t": u"\u0287", \
			u"v": u"\u028C", \
			u"w": u"\u028D", \
			u"y": u"\u028E", \
			u"A": u"\u2200", \
			u"C": u"\u0186", \
			u"E": u"\u018E", \
			u"F": u"\u2132", \
			u"G": u"\u05E4", \
			u"H": u"H", \
			u"I": u"I", \
			u"J": u"\u017F", \
			u"L": u"\u02E5", \
			u"M": u"W", \
			u"N": u"N", \
			u"P": u"\u0500", \
			u"T": u"\u2534", \
			u"U": u"\u2229", \
			u"V": u"\u039B", \
			u"Y": u"\u2144", \
			u"1": u"\u0196", \
			u"2": u"\u1105", \
			u"3": u"\u0190", \
			u"4": u"\u3123", \
			u"5": u"\u03DB", \
			u"6": u"9", \
			u"7": u"\u3125", \
			u"8": u"8", \
			u"9": u"6", \
			u"0": u"0", \
			u".": u"\u02D9", \
			u",": u"'", \
			u"'": u",", \
			u"\"": u",,", \
			u"`": u",", \
			u"?": u"\xBF", \
			u"!": u"\xA1", \
			u"[": u"]", \
			u"]": u"[", \
			u"(": u")", \
			u")": u"(", \
			u"{": u"}", \
			u"}": u"{", \
			u"<": u">", \
			u">": u"<", \
			u"&": u"\u214B", \
			u"_": u"\u203E", \
			u"\u2234": u"\u2235", \
			u"\u2045": u"\u2046" }
	

def flipText(text, reverse=False):
	out = u""
	for c in text:
		if c in flipTable:
			out += flipTable[c]
		else:
			out += c
	if reverse:
		return out[::-1]
	else:
		return out

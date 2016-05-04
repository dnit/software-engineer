
def dehash(num):
	"""
	dehash algorithm  for loktra hash problem
	"""

	letters = "acdegilmnoprstuw"
	out = ""
	while(num != 7 and num > 0):
		pos = num % 37
		if pos < len(letters):
			out = letters[pos] + out
		else:
			return "Not possible"	
		num = (num -pos) / 37

	if(num == 7):
		return out
	else:
	    return "Not possible"		

print dehash(930846109532517)
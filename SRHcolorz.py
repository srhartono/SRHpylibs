from colored import fg, bg, attr

def LCY(text):
	colored_text = f"{fg('light_cyan')}{attr('bold')}{text}{attr('reset')}"
	return(colored_text)

def LGN(text):
	colored_text = f"{fg('light_green')}{attr('bold')}{text}{attr('reset')}"
	return(colored_text)

def YW(text):
	colored_text = f"{fg('yellow')}{attr('bold')}{text}{attr('reset')}"
	return(colored_text)

def LRD(text):
	colored_text = f"{fg('light_red')}{attr('bold')}{text}{attr('reset')}"
	return(colored_text)

def LPR(text):
	colored_text = f"{fg('light_magenta')}{attr('bold')}{text}{attr('reset')}"
	return(colored_text)

def BLU(text):
	colored_text = f"{fg('light_blue')}{attr('bold')}{text}{attr('reset')}"
	return(colored_text)

def LGY(text):
	colored_text = f"{fg('light_gray')}{attr('bold')}{text}{attr('reset')}"
	return(colored_text)


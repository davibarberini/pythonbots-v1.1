import gamefile
def name():
        return "VINCENT"
def colour():
	return (255,20,147)
def commands():
        gamefile.move(200)
	gamefile.turn_left(90)
	gamefile.fire()
	gamefile.turn_left(90)
        gamefile.fire()
	gamefile.turn_left(90)
	gamefile.fire()
	gamefile.turn_left(90)
	gamefile.fire()
	gamefile.done()

def target_spotted(direction):
        gamefile.pointgun(direction*1.0)
        gamefile.fire()
        gamefile.fire()

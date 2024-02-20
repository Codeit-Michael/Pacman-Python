MAP = [
	["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
	["1"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","1"],
	["1"," ","1","1","1","1"," ","1","1","1","1","1","1","1"," ","1","1","1","1","1","1","1"," ","1","1","1","1"," ","1"],
	["1","b","1","1","1","1"," ","1","1","1","1","1","1","1"," ","1","1","1","1","1","1","1"," ","1","1","1","1","b","1"],
	["1"," "," "," "," "," "," ","1","1"," "," "," "," "," "," "," "," "," "," "," ","1","1"," "," "," "," "," "," ","1"],
	["1","1","1"," ","1","1"," ","1","1"," ","1","1"," ","1","1","1"," ","1","1"," ","1","1"," ","1","1"," ","1","1","1"],
	["1","1","1"," ","1","1"," ","1","1"," ","1","1"," ","1","1","1"," ","1","1"," ","1","1"," ","1","1"," ","1","1","1"],
	["1"," "," "," ","1","1"," "," "," "," ","1","1"," "," "," "," "," ","1","1"," "," "," "," ","1","1"," "," "," ","1"],
	["1"," ","1","1","1","1","1","1","1"," ","1","1","1","1","1","1","1","1","1"," ","1","1","1","1","1","1","1"," ","1"],
	["1"," ","1","1","1","1","1","1","1"," ","1","1","1","1","1","1","1","1","1"," ","1","1","1","1","1","1","1"," ","1"],
	["1"," "," "," "," "," "," "," "," "," "," "," "," "," ","g"," "," "," "," "," "," "," "," "," "," "," "," "," ","1"],
	["1","1","1"," ","1","1","1","1","1"," ","1","1","1","n","n","n","1","1","1"," ","1","1","1","1","1"," ","1","1","1"],
	["1","1","1"," ","1","1","1","1","1"," ","1","n","n","n","n","n","n","n","1"," ","1","1","1","1","1"," ","1","1","1"],
	[" "," "," "," "," "," "," ","1","1"," ","1","n","g","n","g","n","g","n","1"," ","1","1"," "," "," "," "," "," "," "],
	["1","1","1"," ","1","1"," ","1","1"," ","1","n","n","n","n","n","n","n","1"," ","1","1"," ","1","1"," ","1","1","1"],
	["1","1","1"," ","1","1"," ","1","1"," ","1","1","1","1","1","1","1","1","1"," ","1","1"," ","1","1"," ","1","1","1"],
	["1"," "," "," ","1","1"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","1","1"," "," "," ","1"],
	["1"," ","1","1","1","1","1","1","1"," ","1","1","1","1","1","1","1","1","1"," ","1","1","1","1","1","1","1"," ","1"],
	["1"," ","1","1","1","1","1","1","1"," ","1","1","1","1","1","1","1","1","1"," ","1","1","1","1","1","1","1"," ","1"],
	["1"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","1"],
	["1","1","1","1","1"," ","1","1","1","1","1","1"," ","1","1","1"," ","1","1","1","1","1","1"," ","1","1","1","1","1"],
	["1","1","1","1","1"," ","1","1","1","1","1","1"," ","1","1","1"," ","1","1","1","1","1","1"," ","1","1","1","1","1"],
	["1"," "," "," "," "," ","1","1"," "," "," "," "," "," ","p"," "," "," "," "," "," ","1","1"," "," "," "," "," ","1"],
	["1","b","1","1"," ","1","1","1"," ","1","1"," ","1","1","1","1","1"," ","1","1"," ","1","1","1"," ","1","1","b","1"],
	["1"," ","1","1"," ","1","1","1"," ","1","1"," ","1","1","1","1","1"," ","1","1"," ","1","1","1"," ","1","1"," ","1"],
	["1"," ","1","1"," "," "," "," "," ","1","1"," "," "," "," "," "," "," ","1","1"," "," "," "," "," ","1","1"," ","1"],
	["1"," ","1","1","1","1"," ","1","1","1","1","1","1","1"," ","1","1","1","1","1","1","1"," ","1","1","1","1"," ","1"],
	["1"," ","1","1","1","1"," ","1","1","1","1","1","1","1"," ","1","1","1","1","1","1","1"," ","1","1","1","1"," ","1"],
	["1"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","1"],
	["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]
]

BOARD_RATIO = (len(MAP[0]), len(MAP))
CHAR_SIZE = 20

WIDTH, HEIGHT = (BOARD_RATIO[0] * CHAR_SIZE, BOARD_RATIO[1] * CHAR_SIZE)

PLAYER_SPEED = CHAR_SIZE // 4
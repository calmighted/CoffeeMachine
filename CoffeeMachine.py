
def_water = 400
def_milk = 540
def_beans = 120
def_cups = 9
def_money = 550

water_fill = 0
milk_fill = 0
beans_fill = 0
cups_fill = 0
filled_water = def_water + water_fill
filled_milk = def_milk + milk_fill
filled_beans = def_beans + beans_fill
filled_cups = def_cups + cups_fill

#def_ == water in coffee machine
#actual_ == water coffee requires

def buy():
	global def_money
	coffeetype = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
	print("")
	global actual_water
	global actual_beans
	global actual_money
	global actual_milk
	# if coffeetype == "back":
	# 	mainmenu()
	if coffeetype == "back":
		mainmenu()
	else:
		if coffeetype == "1":
			actual_water = 250
			actual_milk = 0
			actual_beans = 16
			actual_money = 4
		elif coffeetype == "2":
			actual_water = 350
			actual_milk = 75
			actual_beans = 20
			actual_money = 7
		elif coffeetype == "3":
			actual_water = 200
			actual_milk = 100
			actual_beans = 12
			actual_money = 6
		# elif coffeetype == "back":
		# 	Mainmenu()

		global filled_water
		global filled_beans
		global filled_milk
		global filled_cups
		if filled_water <= actual_water:
			print("Sorry, not enough water!")
		elif filled_milk <= actual_milk:
			print("Sorry, not enough milk!")
		elif filled_beans <= actual_beans:
			print("Sorry, not enough coffee beans!")
		elif filled_cups == 0:
			print("Sorry, not enough disposable cups!")
		else:
			print("I have enough resources, making you a coffee!")
			filled_cups = filled_cups - 1
			filled_water = filled_water - actual_water
			filled_milk = filled_milk - actual_milk
			filled_beans = filled_beans - actual_beans
			def_money = def_money + actual_money
		#print(filled_water)
		print("")

def take():
	global def_money
	print("I gave you ${}".format(def_money))
	def_money = 0
	print("")


def fill():
	global filled_water
	global filled_beans
	global filled_milk
	global filled_cups
	global water_fill
	global milk_fill
	global beans_fill
	global cups_fill
	water_fill = int(input("Write how many ml of water do you want to add:"))
	milk_fill = int(input("Write how many ml of milk do you want to add:"))
	beans_fill = int(input("Write how many grams of coffee beans do you want to add:"))
	cups_fill = int(input("Write how many disposable cups of coffee do you want to add:"))
	filled_water = filled_water + water_fill
	filled_milk = filled_milk + milk_fill
	filled_beans = filled_beans + beans_fill
	filled_cups = filled_cups + cups_fill
	#print(filled_water)




def remaining():
	print("The coffee machine has:")
	print(filled_water, "of water")
	print(filled_milk, "of milk")
	print(filled_beans, "of coffee beans")
	print(filled_cups, "of disposable cups")
	print("${} of money".format(def_money))


def mainmenu():
	while True:
		action = input("Write action (buy, fill, take, remaining, exit):")
		if action == "buy":
			buy()
		elif action == "fill":
			fill()
		elif action == "take":
			take()
		elif action == "remaining":
			remaining()
		elif action == "exit":
			break


try:
	mainmenu()
except EOFError:
	pass

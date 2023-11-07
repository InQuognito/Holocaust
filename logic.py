import chapters

import sys, time, random

name_localized = 'Walk in Berlin'

speed_1 = ["Slow", 200]
speed_2 = ["Normal", 300]
speed_3 = ["Fast", 400]
speed_4 = ["Very Fast", 500]

debug = False
if (debug == False):
	typing_speed = speed_2[1]
else:
	typing_speed = 99999

def encode_memory(memory):
	with open('brain.txt', "a") as file:
		file.write(memory + "\n")

def recall_memory(memory):
	with open('brain.txt') as file:
		for line in file:
			if line == (memory + "\n"):
				return True

def print_text(text):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(random.random()*10.0/typing_speed)

	time.sleep(0.5)

	print("\n")

def print_options(text):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(random.random()*10.0/typing_speed)
	print('')
	time.sleep(0.25)

def question(num, q1, q2, q3="", q4="", prompt="What will you do?"):
	print_text(prompt)
	print_options("1) " + q1)
	print_options("2) " + q2)
	if (num >= 3): print_options("3) " + q3)
	if (num == 4): print_options("4) " + q4)

	valid = False
	while (valid == False):
		choice = input(">>> ")
		if (choice == "1"):
			valid = True
			r = 1
		elif (choice == "2"):
			valid = True
			r = 2
		elif (num >= 3) and (choice == "3"):
			valid = True
			r = 3
		elif (num == 4) and (choice == "4"):
			valid = True
			r = 4
		else:
			print_text("That is not a valid choice. Please try again.")

	print()

	return r

def main():

	print()
	if recall_memory("Completed Game"):
		print()
		print_text("####  ####%### #####   #")
		print_text("#                      #")
		print_text("[    WA K 1N  ER IN    #")
		print_text("#    P@tri k C\%ter    |")
		print_text("#                      #")
		print_text("#@####  ## ## #### #%###")
		print()

	else:
		print()
		print("########################")
		print("#                      #")
		print("#    " + name_localized.upper() + "    #")
		print("#    Patrick Cotter    #")
		print("#                      #")
		print("########################")
		print()

		chapters.tutorial()

	chapters.intro()

	chapters.walk()

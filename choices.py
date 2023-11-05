import logic

def get_ready_for_the_day():
	logic.print_text("As the voices of the soldiers fade away outside, you try your best to prepare yourself for the following day.\nYou had the day off from work, so you decided to go for a walk. The weather isn't ideal, but there isn't much else to do.\nAfter a quick shower, a groan from your stomach tells you that you should probably eat something.")
	logic.time.sleep(0.5)

	choice = logic.question(2, "Search the fridge", "Tough it out")

	if (choice == 1):
		logic.print_text("You rummage through the contents of your fridge, trying to find anything edible. However, most of the food is expired; you had been neglecting the state of it for some time now.\nYou managed to find a half-eaten sandwich from the day previous; it would have to do.\n\nAfter forcing down the stale sandwich, you grab your keys and head for the door.")

		logic.encode_memory("Ate Food")

	elif (choice == 2):
		logic.print_text("After a quick look through the fridge, you decide that you might not be able to classify anything in your fridge as food; at least, nothing you are hungry enough to eat right now.\nYou grab your keys, and head for the door.")

	logic.time.sleep(1.0)

def examine_your_room():
	logic.print_text("You look around your room. You realize sadly that there isn't much to it; the cream-colored walls of your apartment have little adornments of note.\nThe bed in front of you, barely large enough to sleep on, sits on a flimsy metal frame.\nIn the corner to your left, there is a desk as notable as it is durable. On it rests a few documents you had just finished signing the previous night.\nBehind you sits the door, which you feel an urge to walk through in order to avoid being reminded of the state of your room any longer.\nPerhaps it's time to buy a painting or two.")
	logic.time.sleep(1.0)

	get_ready_for_the_day()

def go_back_to_sleep():
	logic.print_text("You decide to ignore that voice in your head; you are much too tired to be dealing with any responsibilities right now. Surely a bit more sleep couldn't hurt?\n\nUnfortunately, toss and turn as you might, you cannot seem to get back to sleep. Oh, well. Maybe it's best to get up anyways.")

	return logic.question(2, "Get ready for the day", "Examine your room")

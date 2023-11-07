import logic
import choices

def tutorial():
	logic.print_text("Welcome to " + logic.name_localized + "! This is a text-based adventure game that takes place in the early stages of the Holocaust. This project aims to replicate the style of some of the first video games ever made.\nIn this game, you will get to choose your own path and decide your own fate. It also contains some very light puzzle-solving elements.")

	logic.print_text("It is also important to keep in mind that this is an interpretive experience.\nMuch of the content is metaphorical in nature, and in no way reflects real experiences of German citizens or Jewish people during this time.")
	logic.time.sleep(0.5)

	logic.print_text("The story will provide you with a prompt and give you choices on how to respond. It will look something like this:")

	logic.print_options("This is a question")
	logic.print_options("1) This is a choice")
	logic.print_options("2) This is another choice\n")

	logic.print_text("In order to progress, you will type the number corresponding with the choice you wish to follow.")

	choice = logic.question(4, logic.speed_1[0], logic.speed_2[0], logic.speed_3[0], logic.speed_4[0], "How fast would you like the text to scroll?")

	if (choice == 1):
		logic.print_text("Great! Your text speed has been set to '" + logic.speed_1[0] + "'.")
		logic.typing_speed = logic.speed_1[1]

	elif (choice == 2):
		logic.print_text("Great! Your text speed has been set to '" + logic.speed_2[0] + "'.")
		logic.typing_speed = logic.speed_2[1]

	elif (choice == 3):
		logic.print_text("Great! Your text speed has been set to '" + logic.speed_3[0] + "'.")
		logic.typing_speed = logic.speed_3[1]

	elif (choice == 4):
		logic.print_text("Great! Your text speed has been set to '" + logic.speed_4[0] + "'.")
		logic.typing_speed = logic.speed_4[1]

	logic.print_text("Now that that is out of the way, it is time to get started.")

	choice = logic.question(2, "Yes", "No", "", "", "Are you ready?")

	if (choice == 1):
		logic.print_text("Great! Let's begin.")

	elif (choice == 2):
		logic.print_text("That is unfortunate, but time waits for no one. Let's begin.")

	logic.time.sleep(0.5)

def intro():
	if logic.recall_memory("Completed Game"):
		logic.print_text("You wake up in your room to the sounds of commotion outside. You had the strangest dream; in fact, this all feels very familiar. You try your best to shake off the strange feeling, and take a look out the window.\nThe weather seems the same as tod-- no, as yesterday. What is this? It's as though you've been through this before.")

	else:
		logic.print_text("You wake up in your room to the sounds of commotion outside. As the grogginess of sleep wears off, you take a look out the window.\nThe sun struggles to shine through a blanket of gray clouds, and it appears as though rain might burst through at any moment. Same as yesterday, it seems.")

	logic.print_text("As you take a look down at the drab street below, you notice some soldiers shepherding some people into a nearby building, but you are too high up to notice much else.\nIt seems like forever ago when you didn't see soldiers walking the streets.\nAs you begin to feel a tiny presence in the back of your mind, urging you to get on with your day, you can't help but wonder what you need protecting from.")
	logic.time.sleep(0.5)

	choice = logic.question(3, "Get ready for the day", "Examine your room", "Go back to sleep")

	if (choice == 3):
		choice = choices.go_back_to_sleep()

	if (choice == 1):
		choices.get_ready_for_the_day()

	elif (choice == 2):
		choices.examine_your_room()

def walk():
	food_notice = ""
	if not logic.recall_memory("Ate Food"):
		food_notice = " You notice an incredible aroma hit your nose; it smells like freshly baked bread."

	logic.print_text("As you step outside your apartment, you are struck by a most unusual sensation; you feel uneasy, as though you are being watched.")

	logic.print_text("As you look around, though, nothing seems cause for alarm; across the street from your flat, you see a father and his son walking together.\nAs you look down the street to your right, you notice a few shops, people mulling about the storefronts." + food_notice)

	logic.print_text("To your left, you see a few children playing in a small clearing outside the apartment complex adjacent to your own.")

	if logic.recall_memory("Completed Game"):
		logic.print_text("As you look further down the street in that direction, you notice two soldiers idling near an alleyway, STARING RIGHT AT YOU/-ERROR/-but even they seem uninterested in your presence; so why is your skin crawling?\nYou try your best to shake off the feeling, and continue on your walk.")

	else:
		logic.print_text("As you look further down the street in that direction, you notice two soldiers idling near an alleyway, seemingly chatting with one another.")

		logic.print_text("But even they seem uninterested in your presence; so why is your skin crawling?\nYou try your best to shake off the feeling, and continue on your walk.")

	temp = "Despite the liveliness of it all, you can't help but notice the subtle differences compared to before the patrols started.\nThe looks of unease as soldiers walk by, the random searches for contraband; it feels difficult to remember a time before."

	if logic.recall_memory("Completed Game"):
		logic.print_text("As you walk further into town, you are enveloped by the droning noise of conversation; it is almost painful, and you begin to develop a POUNDING HEADACHE.\nSOMETHING IS WRONG/-ERROR/-children playing tag scurry by, not noticing as they push past you.\nAs you walk down the bustling street, you take in the sights around you.")

		logic.print_text(temp)

		logic.print_text("You take a look through the windows of the nearby stores, and reflect on how things have changed.\nThe local bookstore is, for lack of a better term, pitiful; you aren't sure if even half of the shelves are full.\nYou recall the soldiers coming through a few months back and stripped the place of any \"degenerate\" material.\nEven the manager of the store, a kind, meek man who would always recommend new material and give the children free material, had been BEATEN TO A PULP/-ERROR/-relieved of his post.\nYou linger in front of it momentarily, deciding what to do next.")

	else:
		logic.print_text("As you walk further into town, you are enveloped by the droning noise of conversation; despite the overcast, the town couldn't be any more alive.\nSome children playing tag scurry by, not noticing as they push past you.\nAs you walk down the bustling street, you take in the sights around you.")

		logic.print_text(temp)

		logic.print_text("You take a look through the windows of the nearby stores, and reflect on how things have changed.\nThe local bookstore is, for lack of a better term, pitiful; you aren't sure if even half of the shelves are full.\nYou recall the soldiers coming through a few months back and stripped the place of any \"degenerate\" material.\nEven the manager of the store, a kind, meek man who would always recommend new material and give the children free material, had been relieved of his post.\nYou linger in front of it momentarily, deciding what to do next.")

	choice = logic.question(2, "Go inside", "Continue walking")

	# Go inside
	if (choice == 1):
		logic.print_text("As you walk into the bookstore, you're hit by the distinct smell of paper, but were not greeted by the comforting sound of flitting pages; The shop was depressingly empty, as was the usual the past few months.\nAs you walk among the shelves, you can't help but feel a pang of frustration at the removal of so many books. Fantasy titles you used to love reading have been replaced by political nonfictions about the Nazi party and the importance of family and work.\nIt's as if a storm came through and blew all of the life out of the place.")

		logic.print_text("As you approach the front counter, even the new manager seemed uninterested. He barely looked up to acknowledge you, despite you being the only person in the store.\nYou begin to realize there's nothing here for you anymore; you turn around to leave, and continue onward.")

	# Continue walking
	elif (choice == 2):
		logic.print_text("You carry forward.")

	if not logic.recall_memory("Ate Food"):
		logic.print_text("If there's one thing that hasn't changed, it's the local bakery; as you approach, an aroma of fresh bread, cinnamon, and newly ground coffee enters your nose.\nA family of four exits the shop, various pastries in hand. As you eye the food, you can't help but feel an intense growling in your stomach.\nYou're getting so hungry now that it's starting to become painful.")

		choice = logic.question(2, "Go inside", "Continue walking")

		# Go inside
		if (choice == 1):
			logic.print_text("As you enter the bakery, your mouth begins to water as you eye all of the food in the displays around you.\nTo your left, you see rows and rows of breads and pastries; on the right, there are some bigger items like cakes and pies.\nAn employee idles behind the counter, waiting expectantly.")

			choice = logic.question(2, "Buy food", "Leave and continue walking")

			if (choice == 1):
				logic.encode_memory("Ate Food")

				logic.print_text("You can't stave off the hunger anymore; you decide to purchase a delicious-looking pastry.\nYou devour it quickly, relishing in the taste of food; you didn't realize just how bad the feeling had been.")

				logic.print_text("You find it funny how eating sometimes makes you feel hungrier.")

				logic.print_text("After you finish your food, you exit the bakery and continue on your walk.")

			if (choice == 2):
				logic.print_text("You reflect on your thin wallet, deciding that the prices here are just a bit too steep. You reluctantly exit the bakery, wondering why in the world you turned away food when you feel this hungry.")

	else:
		logic.print_text("As you walk, you take notice of the local bakery.\nThe food smells delicious, but you just ate; there wouldn't be any point in going inside.")

	temp = "You try to take stock of the situation; is someone being mugged?\nYou have no weapons to defend yourself with, and you consider turning back.\nHowever, your concern gets the best of you, and you try to approach as quietly as possible to take stock of the situation."

	if logic.recall_memory("Completed Game"):
		logic.print_text("As you approach the edge of town, your headache grows unbearable. You feel as though something terrible waits ahead for you, and you consider turning back and concluding your walk when you hear faint noises coming from the alleyway up ahead.\nAs you approach, you become increasingly worried; it sounds as if someone is in trouble.")


		logic.print_text(temp)

		logic.print_text("You weren't prepared for the sight in front of you as you peered around the corner.\nOn the ground lay a man, cowering, covered in blood; he makes little noise besides the occasional whimpering and pleading.\nHis lip has been split open, and his face is covered in dirt from the ground.\nSurrounding him were two larger men, who refused to let him off the ground. Any attempt at diplomacy or retaliation were swiftly thwarted.\nThe sight in front of you makes you sick to your stomach; never before had you witnessed such brutality.\nAs you look closer, you begin to understand better; the man on the ground is unmistakably PATHETIC.")

	else:
		logic.print_text("As you approach the edge of town, you consider turning back and concluding your walk when you hear faint noises coming from the alleyway up ahead.\nAs you approach, you become increasingly worried; it sounds as if someone is in trouble.")

		logic.print_text(temp)

		logic.print_text("You weren't prepared for the sight in front of you as you peered around the corner.\nOn the ground lay a man, cowering, covered in blood; he makes little noise besides the occasional whimpering and pleading.\nHis lip has been split open, and his face is covered in dirt from the ground.\nSurrounding him were two larger men, who refused to let him off the ground. Any attempt at diplomacy or retaliation were swiftly thwarted.\nThe sight in front of you makes you sick to your stomach; never before had you witnessed such brutality.\nAs you look closer, you begin to understand better; the man on the ground is unmistakably Jewish.")

	logic.print_text("You have no idea what you should do in this situation; you can't leave him like this. The police won't help, certainly, and you have no way to defend yourself.\nBut should you try anyways?")

	choice = logic.question(2, "Step in and help", "Continue walking")

	if (choice == 1):
		if logic.recall_memory("Completed Game"):
			logic.print_text("As you begin to approach the men, your head feels like it's splitting in two.\nYour feet freeze in place, and you get an overwhelming sense of fear, as though intervening would be the worst decision you would ever make. The thought of approaching makes you feel like a rodent beneath the tread of a tire.")

			logic.print_text("Try as you might, you cannot make your feet march into the alley; is it fear? Intuition? Self-preservation? Whatever it may be, your gut gets the best of you and you turn to leave. As you walk away, you hear the man muster all of his strength to plead for someone to help one final time.")

		else:
			logic.print_text("You stick with your gut and decide to do what is right. As you examine your surroundings for anything that can help, you notice a piece of metal pipe laying on the ground.\nAt this point, neither of the men have seen you; this should be easy. You continue sneaking up, careful not to alert the men ahead.\nYou pick up the pipe as quietly as possible and continue moving forward. Soon, you are right behing the men who still are not aware of your presence.")

			logic.print_text("You hesitate for a moment; you have never hurt anyone before, and you aren't excited to do it now. However, you know this needs to be done; the man on the ground has it a lot worse than you right now.\nYou raise the pipe over your head and slam it down on top of the man on your left, who drops instantly. Before the other man can fully acknowledge what is happening, you swing the pipe sideways as it connects with a sickening crack into the mans' nose.")

			logic.print_text("Time slows to a crawl as you stand there holding the pipe for what feels like an eternity. Eventually, you come to your senses as the realization of what you have just done sets in.\nYou had never been in a fight before, let alone nearly killed two people. You bring your attention to the man on the ground in front of you, whose eyes contain a mix of fear and astonishment. You imagine for a moment that, to him, you must surely look like a madman.")

			logic.print_text("As you open your mouth to speak to him, you hear several sets of heavy footsteps behind you; it sounds like they are running.\nYou both turn towards the noise, and you see two soldiers rounding the corner; it appears to be the same two from the alleyway earlier.\nIt is apparent after a few brief moments that they are entirely unhappy about the situation in front of them, and they begin shouting frantically at you, ordering you to put the weapon down and get on the ground.\nAs you drop the pipe and attempt to explain the situation, it is clear that the two soldiers are not at all interested in what you have to say.")

			logic.print_text("You must have taken slightly too long to get on the ground, because the last thing you see is a soldier running towards you before connecting a baton to the side of your skull.")

	if (choice == 2):
		logic.print_text("A little voice in the back of your head tells you that you shouldn't interfere; those who try to help the Jews tend to go on to tell few stories.\nAnd besides, what can you do? It's two against one, not to mention their size; it's an impossible task.\nYou avert your gaze, unable to look at the situation any longer.")

		logic.print_text("You turn around and begin to slowly walk away, but you can't cull that gnawing in your conscience. Was there more you could've done to help? Drawn attention to it? You wonder if that man may live. You can't shake the feeling that you might as well have killed him yourself.")

	logic.time.sleep(1.0)

	if logic.recall_memory("Completed Game"):
		logic.print_text("You continue walking.")
		logic.time.sleep(0.5)

		logic.print_text("THE END.")

	else:
		logic.encode_memory("Completed Game")

		logic.print_text("THE END...")
		logic.time.sleep(0.5)

		logic.main()

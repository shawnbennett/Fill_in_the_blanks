# IPND Stage 2 Final Project
# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

###Start My Notes on Project###
###what does this project have to do?

	# 1. open and ask 'Who do I have the pleasure of speaking with today? - assign this as NAME 
		# respond with "Hello NAME would you like to play a game?" provide the response options 'yes/no'
		# if yes - then - 'Excellent, I was hoping you would say that. Lets begin'
		# if no - then  - 'Did you really think you could get out of this? Let's begin!
	# 2. the next thing to do is to ask "Do you feel lucky? Well, do ya?" and provide the user with three options to select from
		# Show "Please place your Quiz order" - "Tall", "Grande", or "Venti"
		# Tall Quiz - 
		# Grande Quiz - 
		# Venti Quiz - 

		#The proper Quiz will need to display with 1-4 listed as blanks
			#if the first answer is correct then print the quiz with that answer filled in and ask for the next response...repeat until complete.
			#if all answers are correct then give some kind of congrats message
			#when a wrong response is given then have some kind of wrong response and end the quiz


#what are the variables that I need to create?
	#Def user name

	#tall_quiz - """What's my favorite movie? The first film was released in 1977, and was directed by George Lucas. 
			#This was the first installment in a series of films, even though it was first moview released it was actually the fourth episode in the series. 
			#The movie had a two friendly droids. A blue and white one named ___1___-D2, and one that was all gold named ___2___-PO. The movie uses the 
			#Force and ___3___ sabers. You guessed it, my favorite is Star ___4___ Episode IV: A New Hope"""
	#grande_quiz - """The Star Wars prequel trilogy, Episodes 1 through 3, began to release in 1999. The movies consisted of The ___1___ Menace, 
			#Attack of the Clones, and ___2___ of the Sith. The films are set 32 years before the origonal series and show the growth of young Anikin 
			#___3___ . The series progresses throuhg the life of Anikin and the films end showing his transition into Darth ___4___."""     
	#venti_quiz - """ It's exciting to see that there will be a new set of Star Wars films for the next generations to enjoy. I have two girls that are 
			#able to watch the same storyline that I loved. My loved the two most recent films The ___1___ Awakens, and the side story in 
			#Rogue ___2___: A Star Wars Story. The new droids in the movies have been a huge wit with my children just like the droids did in the early versions for 
			#me. There is an orange round ball of a droid in The Force awakens names ___3___-8, and a comical K-___4___ in Rogue One.     
	#tall_answers  ["R2", "C3", "light", "Wars"]
	#grande_answers ["Phantom", "Revenge", "Skywalker", "Vader"]
	#venti_answers ["Force", "One", "BB", "2SO"]
	#answers = ["___1___', "___2___", "___3___", "___4___"]


tall_quiz = """What's my favorite movie? The first film was released in 1977, and was directed by George Lucas. 
			#This was the first installment in a series of films, even though it was first moview released it was actually the fourth episode in the series. 
			#The movie had a two friendly droids. A blue and white one named ___1___-D2, and one that was all gold named ___2___-PO. The movie uses the 
			#Force and ___3___ sabers. You guessed it, my favorite is Star ___4___ Episode IV: A New Hope"""
	
grande_quiz = """The Star Wars prequel trilogy, Episodes 1 through 3, began to release in 1999. The movies consisted of The ___1___ Menace, 
			#Attack of the Clones, and ___2___ of the Sith. The films are set 32 years before the origonal series and show the growth of young Anikin 
			#___3___ . The series progresses throuhg the life of Anikin and the films end showing his transition into Darth ___4___."""     
	
venti_quiz = """ It's exciting to see that there will be a new set of Star Wars films for the next generations to enjoy. I have two girls that are 
			#able to watch the same storyline that I loved. My loved the two most recent films The ___1___ Awakens, and the side story in 
			#Rogue ___2___: A Star Wars Story. The new droids in the movies have been a huge wit with my children just like the droids did in the early versions for 
			#me. There is an orange round ball of a droid in The Force awakens names ___3___-8, and a comical K-___4___ in Rogue One."""     


###here are the answers
tall_answers = ["R2", "C3", "light", "Wars"]
grande_answers = ["Phantom", "Revenge", "Skywalker", "Vader"]
venti_answers = ["Force", "One", "BB", "2SO"]

###this is the answer layout 
answers = ["___1___", "___2___", "___3___", "___4___"]


###Outline the things that need defined and then add the code###

###define introduction or define a username?

def intro(name):    #this function will open the quiz by asking the user for a name and doing a meet and greet	
	user_name = raw_input("Hello, who do I have the pleasure of speaking with today?")
	print "Hello "+user_name+", I am very glad to meet you. I am going to test your knowledge with some movie trivia."


def place_order(): ###this function will ask the user to select the level of the quiz and then populate the proper quiz level for the user to start guessing
	user_selection = raw_input('Do you feel lucky, well do ya? :) Please select your level of comfort "Tall", "Grande", or "Venti"')
	if user_selection == "Tall":
			print "\nThank you for placing your order, the first trivia quiz is coming right up\n"
			return tall_quiz, tall_answers
	elif user_selection == "Grande":
			print "\nThank you for placing your order, the second trivia quiz is coming right up\n"
			return grande_quiz, grande_answers
	elif user_selection == "Venti":
			print "\nThank you for placing your order, the final trivia quiz is coming right up\n"
			return venti_quiz, grande_answers
	elif user_selection != "Tall" or "Grande" or "Venti":
			print "\nPlease place your order from the options provided\n"



def check_answert(): #what goes here in the parenth??? #This function should begin by asking the user what they think is the
#answer to ___1___ then roll into the next... If the answe is right it goes on if the answetr is wrong it should ask 
#for the another_guess function



def another_guess():
	user_prompt = raw_input"Would you like to guess again"
		if user_prompt == 'yes' or 'y'
			return
		elif user_prompt == 'no' or 'n'
			return "Game over, thank you for playing"


def game_play():
		







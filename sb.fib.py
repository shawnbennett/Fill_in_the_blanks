# IPND Stage 2 Final Project
# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/
#I need to start by outlining the inputs iI will need to run a quiz. 

##Here are my quizzes. I made them one long line so that the formatting looked better. When I seperated the lines, it didnt look very good running in python. 
padawan_quiz = """What's my favorite movie series? The first film was released in 1977, and was directed by George Lucas. This was the first installment in a series of films, even though it was first movie released it was actually the fourth episode in the series. The movie had a two friendly droids. A blue and white one named ___1___-D2, and one that was all gold named ___2___-PO. The movie uses the Force and ___3___ sabers. You guessed it, my favorite is Star ___4___ Episode IV: A New Hope"""
jedi_quiz = """The Star Wars prequel trilogy, Episodes 1 through 3, began to release in 1999. The movies consisted of The ___1___ Menace, Attack of the Clones, and ___2___ of the Sith. The films are set 32 years before the origonal series and show the growth of young Anikin ___3___ . The series progresses throuhg the life of Anikin and the films end showing his transition into Darth ___4___."""     
master_quiz = """It's exciting to see that there will be a new set of Star Wars films for the next generations to enjoy. I have two daughters that are able to watch the same storyline that I loved. My daughters loved the two most recent films The ___1___ Awakens, and the side story in Rogue ___2___: A Star Wars Story. The new droids in the movies have been a huge hit with my children just like the droids did in the early versions for me. There is an orange round ball of a droid in The Force awakens names ___3___-8, and a comical K-___4___ in Rogue One."""     
##Here are my answers. These are pretty straight forward
padawan_answers = ["r2", "c3", "light", "wars"]
jedi_answers = ["phantom", "revenge", "skywalker", "vader"]
master_answers = ["force", "one", "bb", "2so"]
##Here are the blanks that I will use to do the replacement
numbers_to_replace = ["___1___", "___2___", "___3___", "___4___"] ###this is the answer layout needed to fill in the options
##Here is my intro that will begin by asking the users name and providing a greeting. This will open my quiz. 
def intro(): 
    user_name = raw_input("Hello, who do I have the pleasure of speaking with today?")
    print "\nHello " + user_name + ", I am very glad to meet you. I am going to test your knowledge with some movie trivia.\n"
introduction = intro()
##Here is the part where the user will select the level they want to play by answering the user selection question. 
#This will then bring back the proper quiz and answers to be used later in the program.
def quiz_selection(): 
    user_selection = raw_input("\nYou have three skill levels to select from: 'Padawan', 'Jedi', or 'Master'\n  \nPlease select the level you would like to play! \n") 
    if user_selection == "Padawan":
        print "\nThank you for selecting your skill level, the first trivia quiz is coming right up!\n"
        return padawan_quiz, padawan_answers
    elif user_selection == "Jedi":
        print "\nThank you for selecting your skill level, the second trivia quiz is coming right up!\n"
        return jedi_quiz, jedi_answers
    elif user_selection == "Master":
        print "\nThank you for selecting your skill level, the final trivia quiz is coming right up!\n"
        return master_quiz, master_answers
    elif user_selection != "Padawan" or  "Jedi" or "Master":
        print "\nPlease place your order from the options provided\n"
        return quiz_selection()
selected_level, selected_answers = quiz_selection()
##Here is the part where i take the user sumitted answer and compare it to my answer. If it does not match, I'll ask the use if they would 
#like another guess. This continues a loop until the users decides that they are done by selecting N. Selecting N ends the loop and closes 
#the program. Answering correctly and/or selecting continue and then answerig correctly will take you through the quiz. 
def response(correct_answer, new_quiz, index, new_answer):
    user_response = ""
    while user_response != correct_answer:
        print ""
        print new_quiz
        question_number = numbers_to_replace[index]
        user_response = raw_input("\n(Please answer in lowercase.) \nWhat do you think the answer is for:" + question_number + ") \n")
        if user_response == correct_answer:
            return True 
        else:
            user_prompt = raw_input("I'm sorry that is not correct. Would you like to guess again? Your options are: 'y' or 'n' ")
            if user_prompt == "n":
                print "\nGame over, thank you for playing"  
                break 
            else:
                print "\nExcellent, let's try again" 
                return response(correct_answer, new_quiz, index, new_answer)

##this is the function wich does the replacement of the numeric blank with the correct answer. Uses the for loop. 
def play(new_quiz, new_answer): #this is the function that will lay out the game play. Once through thw
    for index in range(len(numbers_to_replace)):
        correct_answer = new_answer[index]  
        if response(correct_answer, new_quiz, index, new_answer) == True:
            new_quiz = new_quiz.replace(numbers_to_replace[index], correct_answer)
            print "\nGreat Job! You know your trivia!\n"
    print new_quiz

    # print "\nGreat Job! You Successfully completed the Trivia" 

play(selected_level, selected_answers)

# IPND Stage 2 Final Project
# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

##Here are my quizzes. I changed back and forth between long lines that wrap in python and attempting to space myself. Not sure yet which is more appropriate. 
#1:1 session asked that I make these lists of lists instead of 3 individually named and assigned strings
all_quizzes = [["What's my favorite movie series? The first film was released in 1977, and was directed by George Lucas. This was the first installment in a series of films, even though it was the first movie released it was actually the fourth episode in the series. The movie had a two friendly droids. A blue and white one named ___1___-D2, and one that was all gold named ___2___-PO. The movie uses the Force and ___3___ sabers. You guessed it, my favorite is Star ___4___ Episode IV: A New Hope"] ,
["The Star Wars prequel trilogy, Episodes 1 through 3, began to release in 1999. The movies consisted of The ___1___ Menace, Attack of the Clones, and ___2___ of the Sith. The films are set 32 years before the original series and show the growth of young Anikin ___3___ . The series progresses through the life of Anikin and the films end showing his transition into Darth ___4___."] ,     
["It's exciting to see that there will be a new set of Star Wars films for the next generations to enjoy. I have two daughters that are able to watch the same storyline that I loved. My daughters loved the two most recent films The ___1___ Awakens, and the side story in Rogue ___2___: A Star Wars Story. The new droids in the movies have been a huge hit with my children just like the droids did in the early versions for me. There is an orange round ball of a droid in The Force Awakens named ___3___-8, and a comical K-___4___ in Rogue One."]]     
##Here are my answers. These are pretty straight forward. I made a list of each set of correct answers. 
#1:1 asked that I combine these too. Make 1 list of list instead of 3 individual lists
all_answers = [["r2", "c3", "light", "wars"], ["phantom", "revenge", "skywalker", "vader"], ["force", "one", "bb", "2so"]]
##Here are the numbers that I will need to replace 
numbers_to_replace = ["___1___", "___2___", "___3___", "___4___"]


#Here is my intro that will begin by asking the users name and providing a personal greeting. This will open my quiz.
def intro(): 
    user_name = raw_input("Hello, who do I have the pleasure of speaking with today?") 
##the EOFError: EOF when reading a line, is VERY annoying. I researched a bit but did not find a decent answer to get past this. 
#I did figure out that if I have sublime open first - then open my .py file - I receive this error. But if i right click the .py file and select - open with sublime tect - that this error goes away and helps me with my debugging. 
    print "\nHello " + user_name + ", I am very glad to meet you. I am going to test your knowledge with some movie trivia.\n"
intro()

##Here is the part where the user will select the level they want to play by answering the user selection question. 
#This will then bring back the proper quiz and answers to be used later.
def quiz_selection(): 
    user_selection = raw_input("""You have three skill levels to select from: 'padawan', 'jedi', or 'master'
    	Please select the level you would like to play!""") #Automatetheboringstuff - the three quotes and hitting enter does the same as adding the \n's
    if user_selection == "padawan":
        print "\nThank you for selecting your skill level, the first trivia quiz is coming right up!\n"
        return str(all_quizzes[0]), all_answers[0] #verified this return with the 1:1 
    elif user_selection == "jedi":
        print "\nThank you for selecting your skill level, the second trivia quiz is coming right up!\n"
        return str(all_quizzes[1]), all_answers[1]
    elif user_selection == "master":
        print "\nThank you for selecting your skill level, the final trivia quiz is coming right up!\n"
        return str(all_quizzes[2]), all_answers[2]
    elif user_selection != "padawan" or  "jedi" or "master":
        print "\nPlease place your order from the options provided\n"
        return quiz_selection()
selected_level, selected_answers = quiz_selection() #I could not get this funtion to work as intended until I found a post in the Udacity IPND 
#forum with a similar question. This assignment completes what i was wanting to do, but I was unable to get to this on my own without the support of the forum.

##Here is the part where I take the user submitted answer and compare it to my answer. If it does not match, I'll ask the user if they would 
#like another guess. This continues until the users decides that they are done by selecting 'n'. Selecting 'n' ends the loop and closes 
#the program. I couldnt figure this part out until I found the answer in stackoverflow. Answering correctly and/or selecting continue and then answering correctly will take you through the quiz. 
def response(correct_answer, new_quiz, index):
    user_response = ""
    while user_response != correct_answer:
        print "" #I struggled with this code. I had to find a respond inside the forums to figure out that i needed this to work with the loop
        print new_quiz #need this in order to print the new quiz again after it loops.
        question_number = numbers_to_replace[index]
        user_response = raw_input("\n(Please answer in lowercase.) What do you think the answer is for: " + question_number + ") \n")
        if user_response == correct_answer:
            return True #this has to return True in order to start the loop again
        else:
            user_prompt = raw_input("I'm sorry that is not correct. Would you like to guess again? Your options are: 'y' or 'n' ")
            if user_prompt == "n":
                return quit()  #stackoverflow and ATBS are a must in order to get anywhere in this class. Took me a long time to find out how to end this properly. 
            else:
                print "\nExcellent, let's try again. Here is the quiz:" 
                return response(correct_answer, new_quiz, index)

##this is the function which does the replacement of the numeric blank with the correct answer. I had to sign up for a 1:1 session,
#use stackoverflow and ATBS in order to get this function working. I really struggled with this one. I could write it out on paper, but could not seem to 
#complete it without guidence. After the 1:1 session I also required a lot of help from the Udacity forums to get this 
#simplified. Side note - I liked the use of .upper to place attention to the replaced word, I thought about bolding or underlining, but 
#could not seem to find coding to do this. I assume that we will use HTML and CSS to change this after we use Python to create the code...
def play(new_quiz, new_answer): 
    for index in range(len(numbers_to_replace)): #stackoverflow for range(len(list)), ATBS for range(len(somelist))
        correct_answer = new_answer[index]  
        if response(correct_answer, new_quiz, index) == True:
            new_quiz = new_quiz.replace(numbers_to_replace[index], correct_answer)
            print "\nGreat Job! You know your trivia!\n"
    print new_quiz

play(selected_level, selected_answers)


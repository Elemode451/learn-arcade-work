import random
import sys
def main():
    #This function just makes the program work. Everything is run from here. Think of this as a domino -
    #Main will run question_setup, which creates the random list for question_selection, which will
    #always run the next_question function until final_step is ready.
    answer = 0
    score = 0
    question_number = 0
    question_asked = 0
    print("\033[1;30;47m Welcome to Daniel's Quiz Game! \n Prepare to answer the first question!")
    question_setup(answer, score, question_number, question_asked)
def question_setup(answer, score, question_number, question_asked):
    # This function essentially creates a list of questions that will be asked, setting up the program.
    global rand
    rand = random.sample(range(1, 25), 5)
    question_asked = rand[question_number]
    question_selection(rand, answer, score, question_number, question_asked)
def question_selection(rand, answer, score, question_number, question_asked):
    # This function selects what question is going to be chosen, using the random list generated earlier as a way to
    # dictate what questions will be asked. answer is a variable used to make sure the player typed the correct one in,
    # score is used to keep track of the score, question number keeps track of what number in the list we are on, and
    # question asked will actually physically ask the question.
    if question_asked == 1:
        answer = str(input("\033[1;37;40m What game studio developed Fallout 4?"))
        answer = answer.lstrip()
        answer = answer.lower()
        if answer == "bethesda" or answer == "bethesda game studios" or answer == "bethesda softworks":
            print("\033[1;42;40m Correct! The answer was", answer + "!")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            print("\033[1;41;40m Sorry, but your answer was incorrect. The correct answer is Bethesda Game Studios.")
            next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 2:
        answer = str(input("\033[1;37;40m Who discovered the concept of vaccination?"))
        answer = answer.lstrip()
        answer = answer.lower()
        if answer == "jenner" or answer == "edward jenner"or answer == "ed jenner":
            print("Correct! The answer was", answer + "!")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            learn_more = str(input(
                "Sorry, but your answer was incorrect. The correct answer is Edward Jenner. "
                "Would you like to hear more?"))
            learn_more = learn_more.lower()
            if learn_more == "yes" or learn_more == "Yes":
                print("\033[1;41;40m Thank you for selecting yes! Edward Jenner was a prominent"
                      "\nscientific figure in the field of immunology, most well known for his discovery of the smallpox vaccine."
                      "\nAt the time, Smallpox was rampant in small towns, and Jenner was anxious to find a cure."
                      "\nHe noticed that milkmaids who had been infected with cowpox previously "
                      "\nhad not ever showed signs of the disease, so he decided to test his theory"
                      "\nthat cowpox causes immunity against smallpox. He grabbed an eight year old boy"
                      "\nnamed James Phipps,and put a cowpox blister in his skin. Two months later, he exposed"
                      "\nthe boy to smallpox directly through the bloodstream, and he was not infected. "
                      "\nJenner invented the concept of modern vaccinations and immunizations.")
                next_question(rand, answer, score, question_number, question_asked)
            else:
                print("\033[1;40;40m Alright, moving on to the next question.")
                next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 3:
        answer = str(input("\033[1;37;40m What game studio developed Minecraft originally?"))
        answer = answer.lstrip()
        answer = answer.lower()
        if answer == "mojang" or answer == "mojang studios":
            print("\033[1;42;40m Correct! The answer was", answer + "!")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            print("\033[1;41;40m Sorry, but your answer was incorrect. The correct answer is Mojang.")
            next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 4:
        answer = str(input("\033[1;37;40m Who wrote the song Welcome to the Machine?"))
        answer = answer.lstrip()
        answer = answer.lower()
        if answer == "pink floyd":
            print("\033[1;42;40m Correct! The answer was", answer + "! I sense a cultured music fan")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            print(
                "\033[1;41;40m WRONG. Go listen to Wish You Were Here by Pink Floyd. I can't tolerate this disrespect.")
            next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 5:
        answer = str(input("\033[1;37;40m Why is there no cure for the common cold? "
                           "\n A. There are over 200 viruses that cause it, so it's hard to create a vaccine"
                           "\n B. The common cold is very resistant to antibiotics"
                           "\n C. The common cold is very insignificant so there is no need for a cure"
                           "\n D. All of the above"
                           "\n"))
        answer = answer.lstrip()
        answer = answer.upper()
        if answer == "A":
            print("Correct! The answer was", answer + "!")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            print("Sorry, but your answer was incorrect. The correct answer is A.")
            next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 6:
        answer = str(input("\033[1;37;40m Who wrote Don Quixote? "
                           "\n A. Miguel de Unamuno"
                           "\n B. Julio Cortázar"
                           "\n C. Miguel de Cervantes Saavedra"
                           "\n D. Tirso de Molina"
                           "\n "))
        answer = answer.lstrip()
        answer = answer.upper()
        if answer == "C":
            print("Correct! The answer was", answer + "!")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            print("Sorry, but your answer was incorrect. The correct answer is C.")
            next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 7:
        answer = str(input("\033[1;37;40m Never gonna "
                           "\n A. give you up,"
                           "\n B. never gonna"
                           "\n C. let you down"
                           "\n D. never gonna wander off"
                           "\n E. and desert you"
                           "\n"))
        answer = answer.lstrip()
        answer = answer.upper()
        if answer == "A" or answer == "B" or answer == "C" or answer == "D" or answer == "E":
            print("Get rickrolled, nerd. Have a freebie.")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 8:
        answer = str(input("\033[1;37;40m Who wrote The Maze Runner? "
                           "\n A. Gordon Korman"
                           "\n B. James Dashner"
                           "\n C. Neil Shusterman"
                           "\n D. Arthur C. Clarke"
                           "\n "))
        answer = answer.lstrip()
        answer = answer.upper()
        if answer == "B":
            print("Correct! The answer was", answer + "!")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            print("Sorry, but your answer was incorrect. The correct answer is B.")
            next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 9:
        answer = str(input("\033[1;37;40m What year was the Emancipation Proclamation signed? "
                           "\n A. 1776"
                           "\n B. 1861"
                           "\n C. 1862"
                           "\n D. 1863"
                           "\n "))
        answer = answer.lstrip()
        answer = answer.upper()
        if answer == "D":
            print("Correct! The answer was", answer + "!")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            print("Sorry, but your answer was incorrect. The correct answer is D.")
            next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 10:
        answer = str(input("\033[1;37;40m What is the capitol of Argentina? "
                           "\n A. Cordoba"
                           "\n B. Buenos Aires"
                           "\n C. Mar de Plata"
                           "\n D. San Juan"
                           ))
        answer = answer.lstrip()
        answer = answer.upper()
        if answer == "B":
            print("Correct! The answer was", answer + "!")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            print("Sorry, but your answer was incorrect. The correct answer is B.")
            next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 11:
        answer = str(input("\033[1;37;40m Who wrote Big Nate? "
                           "\n A. Lincoln Pierce"
                           "\n B. Jeff Kinney"
                           "\n C. Dav Pilkey"
                           "\n D. James Patterson"
                           "\n "))
        answer = answer.lstrip()
        answer = answer.upper()
        if answer == "A":
            print("Correct! The answer was", answer + "!")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            print("Sorry, but your answer was incorrect. The correct answer is A.")
            next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 12:
        answer = str(
            input("\033[1;37;40m Simplify this equation, and choose the choice that best represents the answer."
                  "\n > 4x + 11 = 3"
                  "\n A. x = -2"
                  "\n B. x = 2"
                  "\n C. x = 7/2"
                  "\n D. x = - 14/4 \n"))
        answer = answer.lstrip()
        answer = answer.upper()
        if answer == "A":
            print("Correct! The answer was", answer + "!")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            print(
                "Sorry, but your answer was incorrect. The correct answer is A.")
            next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 13:
        answer = str(input("\033[1;37;40m Simplify this equation, and choose the choice that best represents the answer."
                  "\n > 8x + 5 = 45"
                  "\n A. x = - 12"
                  "\n B. x = 5"
                  "\n C. x = -5"
                  "\n D. x = 50/8 \n"))
        answer = answer.lstrip()
        answer = answer.upper()
        if answer == "B":
            print("Correct! The answer was", answer + "!")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            print("Sorry, but your answer was incorrect. The correct answer is B.")
            next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 14:
        answer = str(input("\033[1;37;40m What is the top selling record of all time?"
                           "\n A. Dark Side of the Moon - Pink Floyd"
                           "\n B. Thriller - Michael Jackson"
                           "\n C. Back in Black - AC/DC"
                           "\n D. Led Zeppelin IV - Led Zeppelin"))
        answer = answer.lstrip()
        answer = answer.upper()
        if answer == "B":
            print("Correct! The answer was", answer + "!")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            print("Sorry, but your answer was incorrect. The correct answer is B.")
            next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 15:
        answer = str(input("\033[1;37;40m What is the most downloaded Minecraft mod of all time?"
                           "\n A. Just Enough Items"
                           "\n B. Mutant Mobs"
                           "\n C. WAILIA"
                           "\n D. Optifine \n"))
        answer = answer.lstrip()
        answer = answer.upper()
        if answer == "D":
            print("Correct! The answer was", answer + "!")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            print("Sorry, but your answer was incorrect. The correct answer is D.")
            next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 16:
        answer = str(input("\033[1;37;40m Who is the author of Scythe?"
                           "\n A. Neil Shusterman"
                           "\n B. Chris D'Lacey"
                           "\n C. Michael Grant"
                           "\n D. A.J Michaels \n"))
        answer = answer.lstrip()
        answer = answer.upper()
        if answer == "A":
            print("Correct! The answer was", answer + "!")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            print("Sorry, but your answer was incorrect. The correct answer is A.")
            next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 17:
        answer = str(input("\033[1;37;40m Who is the author of 1984?"
                           "\n A. George Orwell"
                           "\n B. Arthur C. Clarke"
                           "\n C. Orson Scott Card"
                           "\n D. H.G Wells \n"))
        answer = answer.lstrip()
        answer = answer.upper()
        if answer == "A":
            print("Correct! The answer was", answer + "!")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            print("Sorry, but your answer was incorrect. The correct answer is A.")
            next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 18:
        answer = str(input("\033[1;37;40m Who is the author of War of the Worlds?"
                           "\n A. George Orwell"
                           "\n B. Arthur C. Clarke"
                           "\n C. Orson Scott Card"
                           "\n D. H.G Wells \n"))
        answer = answer.lstrip()
        answer = answer.upper()
        if answer == "D":
            print("Correct! The answer was", answer + "!")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            print("Sorry, but your answer was incorrect. The correct answer is D.")
            next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 19:
        answer = str(input("\033[1;37;40m Who is the author of Rendezvous with Rama?"
                           "\n A. Arthur C. Clarke"
                           "\n B. Ray Bradbury"
                           "\n C. Aldous Huxley"
                           "\n D. Kurt Vonnegut \n"))
        answer = answer.lstrip()
        answer = answer.upper()
        if answer == "A":
            print("Correct! The answer was", answer + "!")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            print("Sorry, but your answer was incorrect. The correct answer is A.")
            next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 20:
        answer = str(input("\033[1;37;40m Who directed The Martian?"
                           "\n A. Ridley Scott"
                           "\n B. Christohper Nolan"
                           "\n C. Francis Ford Coppola"
                           "\n D. George Lucas \n"))
        answer = answer.lstrip()
        answer = answer.upper()
        if answer == "A":
            print("Correct! The answer was", answer + "!")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            print("Sorry, but your answer was incorrect. The correct answer is A.")
            next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 21:
        answer = str(input("\033[1;37;40m How many standalone novels has Andy Weir written?"
                           "\n A. 1"
                           "\n B. 2"
                           "\n C. 3"
                           "\n D. 4 \n"))
        answer = answer.lstrip()
        answer = answer.upper()
        if answer == "C":
            print("Correct! The answer was", answer + "!")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            print("Sorry, but your answer was incorrect. The correct answer is C.")
            next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 22:
        answer = str(input("\033[1;37;40m What is Pink Floyd's top most sold album?"
                           "\n A. Dark Side of the Moon"
                           "\n B. The Wall"
                           "\n C. A Saucerful of Secrets"
                           "\n D. Wish You Were Here \n"))
        answer = answer.lstrip()
        answer = answer.upper()
        if answer == "A":
            print("Correct! The answer was", answer + "!")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            print("Sorry, but your answer was incorrect. The correct answer is A.")
            next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 23:
        answer = str(input("\033[1;37;40m Who killed Jabba the Hutt in Star Wars?"
                           "\n A. His own soldiers"
                           "\n B. Boba Fett"
                           "\n C. Darth Vader"
                           "\n D. Princess Leia \n"))
        answer = answer.lstrip()
        answer = answer.upper()
        if answer == "D":
            print("Correct! The answer was", answer + "!")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            print("Sorry, but your answer was incorrect. The correct answer is D.")
            next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 24:
        answer = str(input("\033[1;37;40m Who created THX 1138 - Electronic Labyrinth?"
                           "\n A. Francis Ford Coppola"
                           "\n B. Quentin Tarantino"
                           "\n C. George Lucas"
                           "\n D. Steven Spielberg \n"))
        answer = answer.lstrip()
        answer = answer.upper()
        if answer == "C":
            print("Correct! The answer was", answer + "!")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            print("Sorry, but your answer was incorrect. The correct answer is C.")
            next_question(rand, answer, score, question_number, question_asked)
    if question_asked == 25:
        answer = str(input("\033[1;37;40m What was the first Halo game?"
                           "\n A. Halo - Guardians"
                           "\n B. Halo - Combat Evolved"
                           "\n C. Halo - Wars"
                           "\n D. Halo - Ring \n"))
        answer = answer.lstrip()
        answer = answer.upper()
        if answer == "B":
            print("Correct! The answer was", answer + "!")
            score = score + 1
            next_question(rand, answer, score, question_number, question_asked)
        else:
            print("Sorry, but your answer was incorrect. The correct answer is B.")
            next_question(rand, answer, score, question_number, question_asked)
def next_question(rand, answer, score, question_number, question_asked):
    # This uses question number and rand in order to move to the next question, and plugs
    # it back in to the question selection function.
    if question_number < 4:
        question_number = question_number + 1
        display_question_number = question_number + 1
        print(f"\033[1;41;40m Question {display_question_number}:")
        question_asked = rand[question_number]
        question_selection(rand, answer, score, question_number, question_asked)
    if question_number == 4:
        percentage = score / 5 * 100
        final_step(score, percentage)
def final_step(score, percentage):
    # Score calculation and replay encouragement. Gives percentages. The reason that I used various statements rather
    # than one constant one that just says "Good work! Your score was {percentage}" was because I wanted to have each
    # score give a different result. I promise this choice is intentional and not a way to avoid doing one line, I just
    # wanted the game to have some more personality :)
    if score == 0:
        print("Good try! Practice makes perfect, you know! You got zero correct, equating to 0% accuracy.")
        print("Thanks so much for participating in my quiz game!"
              " If you enjoyed it, go ahead and play it again! The game is built with a special function that"
              "\nessentially makes it so every playthrough is different. There are 25 total questions "
              "possible - see if you can get all of them right!")
        sys.exit()
    if score == 1 or score == 2:
        print(f"Nice try! You got a {score}/5, which is exactly {percentage}%.",
              "Not bad, but there is always room for practice!")
        print("Thanks so much for participating in my quiz game!"
              " If you enjoyed it, go ahead and play it again! The game is built with a special function that"
              "\nessentially makes it so every playthrough is different. There are 25 total questions "
              "possible - see if you can get all of them right!")
        sys.exit()
    if score == 3 or score == 4:
        print(f"This time, you did very well! Your score was a {score}/5, or {percentage}%.")
        print("Thanks so much for participating in my quiz game!"
              " If you enjoyed it, go ahead and play it again! The game is built with a special function that"
              "\nessentially makes it so every playthrough is different. There are 25 total questions "
              "possible - see if you can get all of them right!")
        sys.exit()
    if score == 5:
        print("Congratulations, quizmaster! You got a 5/5, which equates to 100 percent! See if you can keep "
              "the streak up!")
        print("Thanks so much for participating in my quiz game!"
              " If you enjoyed it, go ahead and play it again! The game is built with a special function that"
              "\nessentially makes it so every playthrough is different. There are 25 total questions "
              "possible - see if you can get all of them right!")
        sys.exit()
main()
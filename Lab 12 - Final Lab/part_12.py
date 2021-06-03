import random
import arcade
import math

# I clarify this later on, but I wanted to make it explicitly clear from the start that I have one weak warning. This
# warning is not my fault, as it is merely saying that I do not use the delta_time parameter. I have to put it in
# the code, or else it will not run, but it's use is not actually required so the IDE is getting mad at me.


def main():
    # Main function, code starts from here
    on_draw.new_x = 10
    on_draw.new_x2 = 790
    wrong_answers = []
    question_count = int(input("Hello, and welcome to Daniel's Quiz Game! How many questions would you like to "
                               "be quizzed on? (Max is 20, and only numbers will be accepted) "))
    if question_count not in range(1, 21) or question_count == str:
        print("Sorry, that's not a choice. The amount of questions must be above zero, and below twenty-one. "
              "As a result, you will be doing five questions.")
        question_count = 5
    question_number = 0
    random_list = random.sample(range(1, 21), question_count)
    score = 0
    questions_selection(question_number, random_list, score, question_count, wrong_answers)


def questions_selection(question_number, random_list, score, question_count, wrong_answers):
    # Creates a list with all of the questions, and pulls out which one will be asked accordingly
    question1 = Question("Who created Fallout 4?\n"
                         "A. Bethesda\n"
                         "B. Gearworks\n"
                         "C. 343 Studios\n"
                         "D. Bungie\n", "A")
    question2 = Question("Who discovered vaccination?\n"
                         "A. Edward Jenner\n"
                         "B. John F. Kennedy\n"
                         "C. Jordan Terrell Carter\n"
                         "D. Albert Einstein\n", "A")
    question3 = Question("Who originally developed Minecraft?\n"
                         "A. Rockstar Games\n"
                         "B. Sony Games\n"
                         "C. 343 Studios\n"
                         "D. Mojang Studios\n", "D")
    question4 = Question("Who made the song Welcome to the Machine?\n"
                         "A. Metallica\n"
                         "B. Pink Floyd\n"
                         "C. AC/DC\n"
                         "D. Izall\n", "B")
    question5 = Question("Who made the song Kon Queso?\n"
                         "A. MF DOOM\n"
                         "B. Polo G\n"
                         "C. YBN Nahmir\n"
                         "D. Lil Uzi Vert\n", "A")
    question6 = Question("Who wrote the classic novel Don Quijote de la Mancha?\n"
                         "A. Miguel Cervantes\n"
                         "B. Franz Kafka\n"
                         "C. William Shakespeare\n"
                         "D. J.K Rowling\n", "A")
    question7 = Question("Who wrote The Maze Runner?\n"
                         "A. Gordon Korman\n"
                         "B. James Dashner\n"
                         "C. Neil Shusterman\n"
                         "D. Arthur C. Clarke\n", "B")
    question8 = Question("What year was the Emancipation Proclamation signed?\n"
                         "A. 1776\n"
                         "B. 1861\n"
                         "C. 1862\n"
                         "D. 1863\n", "D")
    question9 = Question("What is the capitol of Argentina?\n"
                         "A. Puerto Madero\n"
                         "B. Cordoba\n"
                         "C. Buenos Aires\n"
                         "D. Seville\n", "C")
    question10 = Question(
                            "Who wrote Big Nate?\n"
                            "A. Lincoln Pierce\n"
                            "B. Jeff Kinney\n"
                            "C. Dav Pilkey\n"
                            "D. James Patterson\n", "A")
    question11 = Question("4x + 11 = 3?\n"
                          "A. x = -2\n"
                          "B. x = 2\n"
                          "C. x = 7/2\n"
                          "D. x = - 14/4 \n", "A")
    question12 = Question("What is the top most selling record of all time?\n"
                          "A. Dark Side of the Moon - Pink Floyd\n"
                          "B. Thriller - Michael Jackson\n"
                          "C. Whole Lotta Red - Playboi Carti\n"
                          "D. Back in Black - Metallica\n", "B")
    question13 = Question("Who is the author of 1984?\n"
                          "A. Neil Shusterman\n"
                          "B. Richmond Clark\n"
                          "C. Kazuo Ishiguro\n"
                          "D. George Orwell\n", "D")
    question14 = Question("Where is Apple Headquarters?\n"
                          "A. Redmond, WA\n"
                          "B. Cupertino, CA\n"
                          "C. New York, NY\n"
                          "D. Miami, FL\n", "B")
    question15 = Question("Where is Microsoft Headquarters?\n"
                          "A. San Francisco, CA\n"
                          "B. Redmond, WA\n"
                          "C. Tampa, FL\n"
                          "D. Houston, TX\n", "B")
    question16 = Question("Who authored and illustrated Berserk?\n"
                          "A. Kentaro Miura\n"
                          "B. Tame Impala\n"
                          "C. Eiichiro Oda\n"
                          "D. Hajime Isayama\n", "A")
    question17 = Question("Who wrote the song 'Beat It'?\n"
                          "A. Michael Phelps\n"
                          "B. Michael Jordan\n"
                          "C. Michael Jackson\n"
                          "D. Michael Reeves\n", "C")
    question18 = Question("Who won the 2014 Soccer World Cup?\n"
                          "A. Argentina\n"
                          "B. Croatia\n"
                          "C. Italy\n"
                          "D. Germany\n", "D")
    question19 = Question("Who won the 2018 Soccer World Cup?\n"
                          "A. English\n"
                          "B. Croatia\n"
                          "C. Belgium\n"
                          "D. France\n", "D")
    question20 = Question("What was the top most streamed song of 2019? (On Spotify)\n"
                          "A. Señorita by Camilla Cabello and Shaun Mendes\n"
                          "B. Bad Guy by Billie Eilish\n"
                          "C. Sunflower by Post Malone and Swae Lee\n"
                          "D. Sicko Mode by Travis Scott\n", "A")
    if question_number < question_count:
        item_from_question_list = random_list[question_number]
        questions_list = [question1, question2, question3, question4, question5, question6, question7, question8,
                          question9, question10, question11, question12, question13, question14, question15,
                          question16, question17, question18, question19, question20]
        ask_question(questions_list[item_from_question_list-1], question_number, random_list, score, question_count,
                     wrong_answers, item_from_question_list)
    else:
        if len(wrong_answers) > 0:
            print(f"Better luck next time! Shoot for the 100%!")
        else:
            print("Congratulations on your high score!")
        draw_window(score, question_count)


def ask_question(self, question_number, random_list, score, question_count, wrong_answers, item_from_question_list):
    # Actually asks the question
    player_answer = str(input(self.question)).lstrip()
    player_answer = player_answer.upper()
    if player_answer == self.answer:
        print(f"Correct! The answer was {self.answer}!")
        question_number += 1
        score += 1
    else:
        print(f"Sorry, but your answer was incorrect. The correct answer is {self.answer}.")
        question_number += 1
        wrong_answers.append(item_from_question_list)
    questions_selection(question_number, random_list, score, question_count, wrong_answers)


def on_draw(delta_time):
    # Animates a circle
    # Please note that this function causes a yellow line to appear saying that delta_time is not used, but it is
    # required in order for the program to run. I have tried removing it but on_draw() is a built in method
    # and it requires delta_time to be used.
    for i in range(1, 10):
        for y in range(1, 16):
            if y == 7 or y == 8 or y == 9:
                pass
            else:
                arcade.draw_circle_filled((i * 80), (y * 50), 5, [255, 255, 255])
    on_draw.new_x = on_draw.new_x + 20
    on_draw.new_x2 = on_draw.new_x2 - 20
    draw_super_circle(on_draw.new_x2, 80, 255)
    draw_super_circle(on_draw.new_x, 160, 0)
    draw_super_circle(on_draw.new_x2, 240, 255)
    draw_super_circle(on_draw.new_x, 320, 0)
    draw_super_circle(on_draw.new_x2, 560, 255)
    draw_super_circle(on_draw.new_x, 640, 0)
    draw_super_circle(on_draw.new_x2, 720, 255)
    arcade.finish_render()


def draw_super_circle(x, y, color):
    # Draws a circle. Isn't the name great?
    arcade.draw_circle_filled(x, y, 15, [0, 255, color])


def draw_window(score, question_count):
    # Actaully draws the window.
    arcade.open_window(800, 800, "Thanks for playing Quiz Game Ultra!")
    arcade.set_background_color([0, 0, 0])
    arcade.start_render()
    percentage = math.trunc(score / question_count * 100)

    arcade.draw_text(f"Thanks so much for playing! You scored {percentage}%, which is exactly {score}/"
                     f"{question_count} correct.", 0, 420, (255, 255, 255), 15, 800, "center")
    if percentage == 100:
        arcade.draw_text("Impressive! Nice job on the 100!", 0, 385, (255, 255, 255), 15, 800, "center")
    if percentage < 100:
        arcade.draw_text("Nice try! Keep going!", 0, 390, (255, 255, 255), 15, 800, "center")
    if percentage == 0:
        arcade.draw_text("Everyone makes mistakes! But yours was way worse than I thought possible. Try again.",
                         0, 355, (255, 255, 255), 15, 800, "center")
    arcade.schedule(on_draw, 1/60)

    arcade.finish_render()
    arcade.run()


class Question:
    """
    This class defines a question and it's properties, taking the question to be asked as the first parameter, and the
    answer as the second.
    """
    def __init__(self, question, answer):
        # Defines what the question that will be asked actually is
        self.question = question
        # Defines the answer to the question
        self.answer = answer.upper()


main()

from turtle import *
import time
import random
screen = Screen()
image1 = "image1.gif"
image2 = "image2.gif"
image3 = "image3.gif"
image4 = "image4.gif"
image5 = "image5.gif"
image6 = "image6.gif"
image7 = "image7.gif"
image8 = "image8.gif"
image9 = "image9.gif"
image10 = "image10.gif"
image11 = "image11.gif"
image12 = "image12.gif"
image13 = "image13.gif"
image14 = "image14.gif"
image15 = "image15.gif"
image16 = "image16.gif"
image17 = "image17.gif"
image18 = "image18.gif"
image19 = "image19.gif"
image20 = "image20.gif"
image21 = "image21.gif"
image22 = "image22.gif"
screen.addshape(image1)
shape(image1)
time.sleep(3)
print("Welcome To My Quiz!")
questionlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
while True:
    score = 0
    random.shuffle(questionlist)
    for i in range(21):
        if questionlist[i] == 1:
            while True:
                screen.addshape(image2)
                shape(image2)
                print ("On the screen beside you their is a picture of a badge of one of the four houses. Which one is it ")
                print ("A) Ravenclaw")
                print ("B) Griffindor")
                print ("C) Slytherin")
                print ("D) Hufflepuff")
                print ("E) TurtleVon")
                question1 = input("")
                if question1 == "A" or question1 == "a":
                    print ("Correct! This is a picture of Ravenclaw.")
                    break
                elif question1 == "B" or question1 == "b":
                    print ("Sorry, that's wrong. However your answer is close as they do look the similar")
                    break
                elif question1 == "C" or question1 == "c":
                    print ("Nope that is incorrect.")
                    break
                elif question1 == "D" or question1 == "d":
                    print("Sorry that was not the right anwser")
                    break
                elif question1 == "E" or question1 == "e":
                    print ("Nice try but this is not one of the 4 houses.")
                    break
                else:
                    print ("Invalid choice")
                    clearscreen()
        if questionlist[i] == 2:
            while True:
                screen.addshape(image3)
                shape(image3)
                print ("The picture on the right is the name of a what hogwarts house ")
                print ("A) Trailblazers")
                print ("B) Slytherin")
                print ("C) Ravenclaw")
                print ("D) Hufflepuff")
                print ("E) Gryffindor")
                question1 = input("")
                if question1 == "A" or question1 == "a":
                    print ("Nice try but the trailblazers are not a house at Hogwarts! .")
                    break;
                elif question1 == "B" or question1 == "b":
                    print ("Correct great job!")
                    score = score + 1
                    break;
                elif question1 == "C" or question1 == "c":
                    print ("Nope, Hufflepuff is similiar but not the same.")
                    break;
                elif question1 == "D" or question1 == "d":
                    print ("Nice try Slytherin is actually green with a diffent logo.")
                    break;
                elif question1 == "E" or question1 == "e":
                    print ("Sorry, this is not the correct answer.")
                    break;
                else:
                    print ("Invalid choice")
                    clearscreen()
        if questionlist[i] == 3:
            while True:
                screen.addshape(image4)
                shape(image4)
                print ("What is the name of the charecter in this picture: ")
                print ("A) Harry Potter")
                print ("B) A Rowley")
                print ("C) Peeves")
                print ("D) Neville")
                print ("E) Fred Weasley")
                question1 = input("")
                if question1 == "A" or question1 == "a":
                    print ("Sorry Harry Potter looks different.")
                    break;
                elif question1 == "B" or question1 == "b":
                    print ("Rowley is not a charecter in Harry Potter")
                    break;
                elif question1 == "C" or question1 == "c":
                    print ("Nope that is incorrect.")
                    break;
                elif question1 == "D" or question1 == "d":
                    print ("Yes you are correct")
                    score = score + 1
                    break;
                elif question1 == "E" or question1 == "e":
                    print ("Nice try but you are incorrect")
                    break;
                else:
                    print ("Invalid choice")
                    clearscreen()
        if questionlist[i] == 4:
            while True:
                screen.addshape(image5)
                shape(image5)
                print ("The picture on the left shows a person that was not in the Harry Potter movie: ")
                print ("A) Peeves")
                print ("B) Professor Serpent")
                print ("C) Hermoine")
                print ("D) Harry Potter")
                print ("E) Dumbledore")
                question1 = input("")
                if question1 == "A" or question1 == "a":
                    print ("Correct! ")
                    break;
                elif question1 == "B" or question1 == "b":
                    print ("Sorry, that's wrong.")
                    break;
                elif question1 == "C" or question1 == "c":
                    print ("Nope that is incorrect.")
                    break;
                elif question1 == "D" or question1 == "d":
                    print ("Nice try but it is incorrect.")
                    break;
                elif question1 == "E" or question1 == "e":
                    print ("Dumblemore is a main charecter and was in the movie.")
                    break;
                else:
                    print ("Invalid choice")
                    clearscreen()
        if questionlist[i] == 5:                    
            while True:
                screen.addshape(image6)
                shape(image6)
                print ("This beautiful picture in the pop up window shows one champions for the triwizard tournament: ")
                print ("A) Viktor Krum ")
                print ("B) Ron Weasley")
                print ("C) A Cedric Diggory")
                print ("D) Hemoine")
                print ("E) Harry Potter")
                question1 = input("")
                if question1 == "A" or question1 == "a":
                    print ("Incorrect, nice try.")
                    break;
                elif question1 == "B" or question1 == "b":
                    print ("Sorry, that's wrong. However your answer is close as they do look the similar")
                    break;
                elif question1 == "C" or question1 == "c":
                    print ("Great job, you are correct.")
                    score = score + 1
                    break;
                elif question1 == "D" or question1 == "d":
                    print ("Nice try but it is incorrect.")
                    break;
                elif question1 == "E" or question1 == "e":
                    print ("Sorry that anwser is wrong.")
                    break;
                else:
                    print ("Invalid choice")
                    clearscreen()
        if questionlist[i] == 6:
            while True:
                screen.addshape(image7)
                shape(image7)
                
                print ("This beautiful picture in the pop up window, is an example of a house that a main charecter in the movie lived in: ")
                print ("A) Weasley's House")
                print ("B) Malfoy's manor")
                print ("C) The dursley's house")
                print ("D) The lestranges manor")
                print ("E) Hogwarts")
                question1 = input("")
                if question1 == "A" or question1 == "a":
                    print ("Correct! .")
                    break;
                elif question1 == "B" or question1 == "b":
                    print ("Sorry, that's wrong.")
                    break;
                elif question1 == "C" or question1 == "c":
                    print ("Nope that is incorrect.")
                    break;
                elif question1 == "D" or question1 == "d":
                    print ("Nice try but it is incorrect.")
                    break;
                elif question1 == "E" or question1 == "e":
                    print ("Sorry, this is not the correct answer.")
                    break;
                else:
                    print ("Invalid choice")
                    clearscreen()
        if questionlist[i] == 7:
            while True:
                screen.addshape(image8)
                shape(image8)
                print ("The picture on the right is the name of a Candy served on the train to Hogwarts ")
                print ("A) Chocolate Frogs")
                print ("B) Hersheys")
                print ("C) Maynards")
                print ("D) Sour patch kids")
                print ("E) Licorice Wands")
                question1 = input("")
                if question1 == "A" or question1 == "a":
                    print ("Correct! .")
                    score = score + 1
                    break;
                elif question1 == "B" or question1 == "b":
                    print ("Sorry, hershey's was not in Harry Potter.")
                    break;
                elif question1 == "C" or question1 == "c":
                    print ("Nope that is incorrect. Maynards will is also not in Harry Potter.")
                    break;
                elif question1 == "D" or question1 == "d":
                    print ("Nice try, I see why you chosed this tho.")
                    break;
                elif question1 == "E" or question1 == "e":
                    print ("Sorry, this is not the correct answer.")
                    break;
                else:
                    print ("Invalid choice")
                    clearscreen()

        if questionlist[i] == 8:
            while True:
                screen.addshape(image9)
                shape(image9)
                print ("The picture on the right is the name of the Defence Against Dark Arts Teacher in the 3rd movie ")
                print ("A) Severus Snape")
                print ("B) Remus Lupin")
                print ("C) Gilderoy Lockhart")
                print ("D) Ms.Young")
                print ("E) Albus Dumbledore")
                question1 = input("")
                if question1 == "A" or question1 == "a":
                    print ("Nice try Snape was a teacher but in the 6th movie! .")
                    break;
                elif question1 == "B" or question1 == "b":
                    print ("Correct great job!")
                    score = score + 1
                    break;
                elif question1 == "C" or question1 == "c":
                    print ("Nope, He was a teacher in the 2nd film.")
                    break;
                elif question1 == "D" or question1 == "d":
                    print ("Nice try but Ms.Young wasn't in Harry Potter.")
                    break;
                elif question1 == "E" or question1 == "e":
                    print ("Sorry, this is not the correct answer.")
                    break;
                else:
                    print ("Invalid choice")
                    clearscreen()
        if questionlist[i] == 9:
            while True:
                screen.addshape(image10)
                shape(image10)
                print ("The picture on the right is the name of a house elf ")
                print ("A) Dobby")
                print ("B) Ginny")
                print ("C) Wunky")
                print ("D) Kreacher")
                print ("E) Jimmy")
                question1 = input("")
                if question1 == "A" or question1 == "a":
                    print ("Nice Job that anwser is correct! .")
                    score = score + 1
                    break;
                elif question1 == "B" or question1 == "b":
                    print ("Ginny is a real person not a house elf!")
                    break;
                elif question1 == "C" or question1 == "c":
                    print ("Nope, good try tho.")
                    break;
                elif question1 == "D" or question1 == "d":
                    print ("Nice try.")
                elif question1 == "E" or question1 == "e":
                    print ("Sorry, this is not the correct answer.")
                    break;
                else:
                    print ("Invalid choice")
        if questionlist[i] == 10:
            while True:
                screen.addshape(image11)
                shape(image11)
                print ("The picture on the right is Harry's wand. Which animal is related to the tail of his wand ? ")
                print ("A) Dragon")
                print ("B) Lion")
                print ("C) Crow")
                print ("D) Fish")
                print ("E) Phoenix")
                question1 = input("")
                if question1 == "A" or question1 == "a":
                    print ("Sorry thats wrong")
                    break;
                elif question1 == "B" or question1 == "b":
                    print ("Close but you are wrong")
                    break;
                elif question1 == "C" or question1 == "c":
                    print ("Nice try but that is the wrong anwser")
                    break;
                elif question1 == "D" or question1 == "d":
                    print ("Nope fish aren't prominent in Harry Potter but nice try")
                    break;
                elif question1 == "E" or question1 == "e":
                    print ("Correct Great job")
                    score = score + 1
                    break;
                else:
                    print ("Invalid choice")
                    clearscreen()
        if questionlist[i] == 11:
            while True:
                screen.addshape(image12)
                shape(image12)
                print ("The picture on the right is the name of Harry Potter's godfather ")
                print ("A) James")
                print ("B) Sirius")
                print ("C) Peter")
                print ("D) Remus")
                print ("E) Dumbledore")
                question1 = input("")
                if question1 == "A" or question1 == "a":
                    print ("Nice try but James is Harry's dad not godfather! .")
                    break;
                elif question1 == "B" or question9 == "b":
                    print ("Correct great job!")
                    score = score + 1
                    break;
                elif question1 == "C" or question9 == "c":
                    print ("Nope close but not the right anwser.")
                    break;
                elif question1 == "D" or question9 == "d":
                    print ("Nice try and I can see why you choose that.")
                    break;
                elif question1 == "E" or question1 == "e":
                    print ("Sorry, this is not the correct answer.")
                    break;
                else:
                    print ("Invalid choice")
                    clearscreen()
        if questionlist[i] == 12:
            while True:
                screen.addshape(image13)
                shape(image13)
                print ("The picture on the right is the name of Harry Potter's mom ")
                print ("A) James")
                print ("B) Lily")
                print ("C) Bellatrix")
                print ("D) Narcissa")
                print ("E) Dumbledore")
                question10 = input("")
                if question1 == "A" or question1 == "a":
                    print ("Nice try but that is the name of his dad .")
                    break;
                elif question1 == "B" or question1 == "b":
                    print ("Correct great job!")
                    score = score + 1
                    break;
                elif question1 == "C" or question1 == "c":
                    print ("Nope, that is a charecter in the movie but not Harry's mom")
                    break;
                elif question1 == "D" or question1 == "d":
                    print ("Nice try and I can see why you choose that.")
                    break;
                elif question1 == "E" or question1 == "e":
                    print ("Sorry, this is not the correct answer.")
                    break;
                else:
                    print ("Invalid choice")
                    clearscreen()
        if questionlist[i] == 13:
            while True:
                screen.addshape(image14)
                shape(image14)
                print ("The picture on the right shows a person with red hair. Using your knowledge of the movies books which family in harry potter usually has red hair ")
                print ("A) Potter's")
                print ("B) Weasleys")
                print ("C) Malfoy's")
                print ("D) Black's")
                print ("E) Granger's")
                question1 = input("")
                if question1 == "A" or question1 == "a":
                    print ("Nice try but Harry Potter and his family don't have red hair! .")
                    break;
                elif question1 == "B" or question11 == "b":
                    print ("Correct great job")
                    score = score + 1
                    break;
                elif question1 == "C" or question1 == "c":
                    print ("Nope, malfoys do not have red hair aswell.")
                    break;
                elif question1 == "D" or question1 == "d":
                    print ("Nice try and I can see why you choose that.")
                    break;
                elif question1 == "E" or question1 == "e":
                    print ("Sorry, this is not the correct answer. The granger's actually have different hair within their own family.")
                    break;
                else:
                    print ("Invalid choice")
        if questionlist[i] == 14:
            while True:
                screen.addshape(image15)
                shape(image15)
                print ("The picture on the right is name of the what charms teacher ")
                print ("A) Professor Snape")
                print ("B) Professor Quirell")
                print ("C) Professor Mcgonagall")
                print ("D) Professor Flitwick")
                print ("E) Professor Quirell")
                question1 = input("")
                if question1 == "A" or question1 == "a":
                    print ("Incorrect but nice try !")
                    break;
                elif question1 == "B" or question1 == "b":
                    print ("Very close but not their yet.")
                    break;
                elif question1 == "C" or question1 == "c":
                    print ("That is wrong but nice try")
                    break;
                elif question1 == "D" or question1 == "d":
                    print (" Great job your correct")
                    score = score + 1
                    break;
                elif question1 == "E" or question1 == "e":
                    print ("Sorry but that anwser is wrong")
                    break;
                else:
                    print ("Invalid choice")
                    clearscreen()   
        if questionlist[i] == 15:
            while True:
                screen.addshape(image16)
                shape(image16)
                print ("The picture on the right is name of this group of boys ")
                print ("A) Mauraders")
                print ("B) Potters")
                print ("C) Wizards")
                print ("D) Gryffindors")
                print ("E) The Cool Boys")
                question1 = input("")
                if question1 == "A" or question1 == "a":
                    print ("Yes that is correct")
                    score = score + 1
                    break;
                elif question1 == "B" or question1 == "b":
                    print ("Nope nice try but that is incorrect")
                    break;
                elif question1 == "C" or question1 == "c":
                    print ("Although this is correct it is not what I was looking for")
                    break;
                elif question1 == "D" or question1 == "d":
                    print ("Again this is theoretically correct but not what I was looking for")
                    break;
                elif question1 == "E" or question1 == "e":
                    print ("Nope this is incorrect but nice try")
                    break;
                else:
                    print ("Invalid choice")
                    clearscreen()
        if questionlist[i] == 16:
            while True:
                screen.addshape(image17)
                shape(image17)
                print ("The picture on the right is the name of the train that is used to go to Hogwarts ")
                print ("A) Hogwarts Train")
                print ("B) Hogwarts Express")
                print ("C) Go Train")
                print ("D) Subway")
                print ("E) Hogwarts Transit")
                question1 = input("")
                if question1 == "A" or question1 == "a":
                    print ("Very close but not their yet")
                    break;
                elif question1 == "B" or question1 == "b":
                    print ("Correct !")
                    score = score + 1
                    break;
                elif question1 == "C" or question1 == "c":
                    print (" Nope, the go train is in real life, not in Harry Potter")
                    break;
                elif question1 == "D" or question1 == "d":
                    print ("Sorry thats not the right anwser")
                    break;
                elif question1 == "E" or question1 == "e":
                    print ("Close again but thats not the anwser")
                    break;
                else:
                    print ("Invalid choice")
                    clearscreen()
        if questionlist[i] == 17:
            while True:
                screen.addshape(image18)
                shape(image18)
                print ("The picture on the right shows a picture of Lord Voldermort, What is his real name")
                print ("A) Tom Marit Riddle")
                print ("B) Tom Marvolo Riddle")
                print ("C) Craig Jenkins")
                print ("D) Vernon Dursley")
                print ("E) Dudley Dursley")
                question1 = input("")
                if question1 == "A" or question1 == "a":
                    print ("Very close but his middle name is Marvelo")
                    break;
                elif question1 == "B" or question1 == "b":
                    print ("Correct")
                    score = score + 1
                    break;
                elif question1 == "C" or question1 == "c":
                    print ("Incorrect, that is the name of another student")
                    break;
                elif question1 == "D" or question1 == "d":
                    print ("Sorry that is not correct")
                    break;
                elif question1 == "E" or question1 == "e":
                    print ("Nice try but Incorrect")
                    break;
                else:
                    print ("Invalid choice")
                    clearscreen()
        if questionlist[i] == 18:
            while True:
                screen.addshape(image19)
                shape(image19)
                print ("On the right is a picture displaying one of the 3 unforgivable curses. Which one is it ? ")
                print ("A) Killing Curse")
                print ("B) Imperius Curse")
                print ("C) Cruciatus Curse")
                print ("D) Disarming Curse")
                print ("E) The charms curse")
                question1 = input("")
                if question1 == "A" or question1 == "a":
                    print ("Correct great job")
                    score = score + 1
                    break;
                elif question1 == "B" or question1 == "b":
                    print ("Sorry that anwser is wrong")
                    break;
                elif question1 == "C" or question1 == "c":
                    print ("Very close but that anwser is wrong as well")
                    break;
                elif question1 == "D" or question1 == "d":
                    print ("That is also close but not the right anwser")
                    break;
                elif question1 == "E" or question1 == "e":
                    print ("Nice try but that is incorrect")
                    break;
                else:
                    print ("Invalid choice")
                    clearscreen()
        if questionlist[i] == 19:
            while True:
                screen.addshape(image20)
                shape(image20)
                print ("The picture on the right is the name of the tournament in the fifth movie ")
                print ("A) Goblet of fire")
                print ("B) Triwizard Tournament")
                print ("C) Maze of Death")
                print ("D) Quidittch")
                print ("E) House Cup")
                question1 = input("")
                if question1 == "A" or question1 == "a":
                    print (" That is the name of the movie not the tournament, but nice try")
                    break;
                elif question1 == "B" or question1 == "b":
                    print ("Correct great job")
                    break;
                elif question1 == "C" or question1 == "c":
                    print ("That is close but incorrect")
                    break;
                elif question1 == "D" or question1 == "d":
                    print ("That is a sport in Hogwarts not the name of a tournament")
                    break;
                elif question1 == "E" or question1 == "e":
                    print ("Nice try but incorrect")
                    break;
                else:
                    print ("Invalid choice")
                    clearscreen()
        if questionlist[i] == 20:
            while True:
                screen.addshape(image21)
                shape(image21)
                print ("What is the brand of the broom on the left ")
                print ("A) Silverarrow")
                print ("B) Nimbus 2000")
                print ("C) Shooting Star")
                print ("D) Comet")
                print ("E) Cleansweep")
                question1 = input("")
                if question1 == "A" or question1 == "a":
                    print (" Nice try but incorrect")
                    break;
                elif question1 == "B" or question1 == "b":
                    print ("Correct, great job !")
                    score = score + 1
                    break;
                elif question1 == "C" or question1 == "c":
                    print ("You were close but that is not the right anwser")
                    break;
                elif question1 == "D" or question1 == "d":
                    print ("Very similiar but not quite the right anwser")
                    break;
                elif question1 == "E" or question1 == "e":
                    print ("Sorry that was incorrect")
                    break;
                else:
                    print ("Invalid choice")
                    clearscreen()
        if questionlist[i] == 21:
            while True:
                screen.addshape(image22)
                shape(image22)
                print ("The picture on the right is the name of a charecter that betrayed Harry's Parents. What is his name ")
                print ("A) Peter Pettigrew")
                print ("B) James Potter")
                print ("C) Sirius Black")
                print ("D)  Remus Liping")
                print ("E) Severus Snape")
                question1 = input("")
                if question1 == "A" or question1 == "a":
                    print ("Correct Great Job !")
                    score = score + 1
                    break;
                elif question1 == "B" or question1 == "b":
                    print ("Very close but not their yet")
                    break;
                elif question1 == "C" or question1 == "c":
                    print ("Nice try but incorrect")
                    break;
                elif question1 == "D" or question1 == "d":
                    print ("You were clse but not quite their")
                    break;
                elif question1 == "E" or question1 == "e":
                    print ("Sorry that's wrong")
                    break;
                else:
                    print ("Invalid choice")
                    clearscreen()
    print("Your score on this test is " + str(score) + " /21!")
    if score == 21:
        print ("Great Job, you are a genius regarding Harry Potter")
    elif 11 < score < 21:
        print ("Great effort, you are very close to becoming profund regarding Harry Potter!")
    else:
        print ("Keep working. If you keep reading the books and watching the movies you will continue to develop your knowledge!")

    play_again = input("Would you like to play again? Yes/No: ")
    if play_again == "No" or play_again == "no":
        print ("Thanks for playing and I hoped you enjoyed")
        break;
    elif play_again == "Yes" or play_again == "yes":
        continue;
    else:
        break;



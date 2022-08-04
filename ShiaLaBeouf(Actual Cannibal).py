import time
print("You're walking in the woods")
print("There's no one around and your phone is dead")
print("Out of the corner of your eye you spot him:")
print("Shia LaBeouf")
print("He's following you, about 30 feet back")
shia1 = input("do you start running? ")
if shia1.lower() == "no":
    print("He gets down on all fours and breaks into a sprint")
    print("He's gaining on you")
    print("Shia LaBeouf")
    #different ways Shia catches you for each ending
    #you died ending 1
    print("")
elif shia1.lower() == "yes":
    print("He gets down on all fours and breaks into a sprint")
    print("He's gaining on you")
    print("Shia LaBeouf")
    print("You're looking for your car but you're all turned around")
    print("He's almost upon you now and you can see there's blood on his face")
    print("My God there's blood everywhere!")
    print("Running for your life (from Shia LaBeouf)")
    print("He's brandishing a knife (It's Shia LaBeouf)")
    print("Lurking in the shadows")
    print("Hollywood superstar Shia LaBeouf")
    print("Living in the woods (Shia LaBeouf)")
    print("Killing for sport (Shia Labeouf)")
    print("Eating all the bodies")
    print("actual cannibal Shia LaBeouf")
    shia2 = input("do you try to fight him? ")
    if shia2.lower() == "yes":
        #you died: ending 2
        print("")
    elif shia2.lower() == "no":
        print("Now it's dark and you seem to have lost him")
        print("But you're hopelessly lost yourself")
        print("Stranded with a murderer")
        print("You creep silently through the underbrush")
        print("Aha! In the distance")
        print("A small cottage with a light on")
        print("Hope! you move stealthily toward it")
        print("But your leg! Ah! It's caught in a bear trap!")
        shia3 = input("what do you do? ")
        if shia3.lower() == "gnaw off your leg":
            print("Gnawing of your leg (quiet, quiet)")
            print("Limping to the cottage (quiet, quiet)")
            print("Now you're on the doorstep")
            print("Sitting inside: Shia LaBeouf")
            print("Sharpening an axe (Shia LaBeouf)")
            print("But he doesn't hear you enter (Shia LaBeouf)")
            shia4 = input("what do you do? ")
            if shia4.lower() == "sneak up behind him":
                print("You're sneaking up behind him")
                print("Strangling superstar Shia LaBeouf")
                print("Fighting for your life with Shia LaBeouf")
                print("Wrestling a knife from Shia LaBeouf")
                print("Stab it in his kidneys")
                print("Safe at last from Shia Labeouf")
                shia5 = input("what do you do? ")
                if shia5.lower() == "limp into the dark woods":
                    print("you limp into the dark woods")
                    print("Blood oozing from your stump leg")
                    print("You've beaten Shia LaBeouf")
                    time.sleep(5)
                    print("WAIT! HE ISN'T DEAD! (Shia Surprise)")
                    print("There's a gun to your head and death in his eyes.")
                    shia6 = input("what skill do you use? ")
                    if shia6.lower() == "jiu jitsu":
                        print("But you can do Jiu Jitsu")
                        print("Body slam superstar Shia LaBeouf")
                        print("Legendary fight with Shia LaBeouf")
                        print("Normal Tuesday night for Shia LaBeouf")
                        shia7 = input("what do you do? ")
                        if shia7.lower() == "try to swing an axe at Shia LaBeouf":
                            print("you try to swing an axe at Shia LaBeouf")
                            print("But blood is draining fast from your stump leg")
                            print("He's dodging every swipe, he parries to the left")
                            shia8 = input("what do you do? ")
                            if shia8.lower() == "counter to the right":
                                print("you counter to the right, you catch him in the neck")
                                print("You're chopping off his head now")
                                print("You have just decapitated Shia LaBeouf")
                                print("His head topples to the floor, expresionless")
                                print("You fall to your knees and catch your breath")
                                print("You're finally safe from Shia LaBeouf")
                            else:
                                #you died: ending 8
                                print("")
                        else:
                            #you died: ending 7
                            print("")
                    else:
                        #you died: ending 6
                        print("")
                else:
                    #you died: ending 5
                    print("")
            else:
                #you died: ending 4
                print("")
        else:
            #you died: ending 3
            print("")





            

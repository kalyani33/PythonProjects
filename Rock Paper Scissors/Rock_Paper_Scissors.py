import random
# library that we use in order to choose
# on randomly rock,paper,scissors

#computer score
comp_score=0

#man score
man_score=0

#function for selection of rock,paper,scissors
#to man
def man_choose():
    user_choice=input("Select Rock(r),paper(p),or Scissors(s): ")
    #user_choice=="s"
    if user_choice in ["Rock","r","R","rock"]:
        user_choice="r"
    elif user_choice in ["paper","p","P","Paper"]:
        user_choice="p"
    elif user_choice in ["s","S","Scissors","scissors"]:
        user_choice="s"
    else:
        print("I did't understand ,please try again")
    return user_choice

#function for randomly selection of rock,
#paper,scissors
def comp_choose():
    l=["r","s","p"]
    #r-rock,s-scissors,p-paper
    comp_choice=random.choice(l)
    return comp_choice


while True:
    man=man_choose()
    comp=comp_choose()
    print(comp)
    #if man selects paper
    if man=="p":
        if comp=="p":
            print("comp chooses 'paper' so,it is tie")
        elif comp=="r":
            print("comp chooses 'rock' you WON!!")
            man_score=man_score+1
        elif comp=="s":
            print("comp chooses 'scisssors' ,you LOOSE!!")
            comp_score=comp_score+1
    #if man selects rock
    elif man=="r":
        if comp=="p":
            print("comp chooses 'paper' you LOOSE!!")
            comp_score=comp_score+1
        elif comp=="r":
            print("comp chooses rock so,it is tie")
        elif comp=="s":
            print("comp choose 'scissors' YOU WON!!!")
            man_score=man_score+1
    #if man selects scissors
    elif man=="s":
        if comp=="p":
            print("comp chooses 'paper' YOU WON!")
            man_score=man_score+1

        elif comp=="r":
            print("comp chooses 'rock' YOU LOOSE!!!")
            comp_score=comp_score+1
        elif comp=="s":
            print("comp chooses 'scissors' so,it is tie")


    #print("")
    print("your score: "+str(man_score))
    print("comp score: "+str(comp_score))
    print("")
    inp=input("Do you want to continue:Y/N ")
    if inp=="y":
        continue
    else:
        print("Thanks for playing!!!!")
        break






















import time
import random

fs = 0
fs2 = 0
x = 0
gc = 0


p1 = input("enter player 1 name: ")
p2  = input("enter player 2 name: ")
gc = int(input("enter gamecode: "))


if gc == 1234:
    for x in range (5):
        roll = (random.randint(1,6))
        roll1 = (random.randint(1,6))
        tot = (roll+roll1)
        time.sleep(1)
        print("")


        print("round",x+1)

        print("")


        print(p1,"has rolled",roll,"and",roll1)
        print("making a total of",tot)

        if roll == roll1:
            print("your rolls are the same you get a duplicate roll")
            dr = (random.randint(1,6))
            tot = (roll+roll1+dr)
            print(p1,"has rolled",dr)
            print("making his new total",tot)
        else:
            time.sleep(0)


        if tot%2 == 0:
            print("your number is even you get +10 points")
            fs = (fs+10)

        else:
            print("your number is even you get -5 points")
            fs = (fs-5)



        if fs < 0:
            fs = fs*0
            print("you scored",fs)


        else:
            print("you scored",fs)
            
else:
    print("WRONG GAME CODE EXITING")
    time.sleep(3)
    exit()

            
print("")
print("")
print(p2,"GO")



for x in range (5):

    roll2 = (random.randint(1,6))
    roll12 = (random.randint(1,6))
    tot2 = (roll2+roll12)
    time.sleep(1)
    print("")
    print("")
    print("round",x+1)
    print("")


    print(p2,"has rolled",roll2,"and",roll12)
    print("making a total of",tot2)

    if roll2 == roll12:
        print("your rolls are the same you get a duplicate roll")
        dr2 = (random.randint(1,6))
        tot2 = (roll2+roll12+dr2)
        print(p2,"has rolled",dr2)
        print("making a total of",tot2)


    else:
        time.sleep(0)


    if tot2%2 == 0:
        print("your number is even you get +10 points")
        fs2 = (fs2+10)

    else:
        print("your number is even you get -5 points")
        fs2 = (fs2-5)




    if fs2 < 0:
        fs2 = fs2*0
        print("you scored",fs2)


    else:
        print("you scored",fs2)



if fs > fs2:
    print("")
    print("")
    print(p1,"has won with",fs,"points")

elif fs < fs2:
    print("")
    print("")
    print(p2,"has won with",fs2,"points")

else:
    while lr1 == lr2:
        print("")
        print("")
        print("you both have the same number of points")
        time.sleep(1)
        print("one last dice will be thrown to decide the winner")
        print("")
        lr1 = (random.randint(1,6))
        print(p1,"has rolled",lr1)
        print("")
        lr2 = (random.randint(1,6))
        print(p2,"has rolled",lr2)
        print("")
        if lr1 > lr2:
            print("")
            print(p1,"has won with the dice score of",lr1)
        else:
            ("")
            print(p2,"has won with the dice score of", lr2)

        
myfile = open ("Score_Of_Game.txt", "a")
myfile.write("\n")
myfile.write(p1)
myfile.write(" has gotten ")
myfile.write(str(fs))
myfile.write(" points")
myfile.write(str("\n"))
myfile.write(p2)
myfile.write(" has gotten ")
myfile.write(str(fs2))
myfile.write(" points")
if fs>fs2:
    myfile.write("\n")
    myfile.write(p1)
    myfile.write(" has won")
elif fs == fs2:
    if lr1>lr2:
        myfile.write("\n")
        myfile.write(p1)
        myfile.write(" has won with the last roll of ")
        myfile.write(str(lr1))
    else:
        myfile.write("\n")
        myfile.write(p2)
        myfile.write(" has won with the last roll of ")
        myfile.write(str(lr2))
else:
    myfile.write("\n")
    myfile.write(p2)
    myfile.write(" has won")
myfile.close()

print("THE GAME HAS FINISHED. CODE WILL KILL ITSELF IN 5 SECONDS")
time.sleep(5)
exit()
from random import randint
javab = randint(1, 6)# the number random betwen one and six

while True:

    i=int(input("can you tell me a number: "))

    if i==javab:
        print("you win well down")
        break # becase tjis is a winner

    elif i <= javab:
        print(f' our number is {javab} pease Increase your number')

    elif i >javab:
        print(f" parrn brear our number is{javab}")

    else:
        print("please follow the rules")
        
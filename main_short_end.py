import random

computer = random.choice([1, -1, 0])

'''
1 for snake 
-1 for water 
0 for gun 
'''
youstr =input("Enter your choice :")
youdict = {"s": 1 , "w": -1,"g":0}
reversedict = {1 :"Snake", -1 : "Water ", 0 : "Gun "}
you  = youdict[youstr]
# by now we have 2 numbers (variables ) ,you and computer 

print(f"you choose {reversedict[you]}\ncomputer choose {reversedict[computer]}")

if (computer == you ):
    print("its a draw ! ")
else :
    # by analysis 
    '''
    if(computer == -1 and you ==1 ):(computer - you) = -2
        print("You win ")

    elif(computer == -1 and you == 0):(computer - you) = -1
        print("You loss ")

    elif(computer == 1 and you ==-1 ):(computer - you) =2  
        print("You loss!")    

    elif(computer == 1 and you == 0):(computer - you) = 1
        print("You win!")

    elif (computer == 0 and you == -1):(computer - you) = 1
        print("You win!")

    elif(computer == 0 and you == 1 ):(computer - you) = -1
        print("You lose !")

        the below logic is based on the value of computer - you
    '''
    if ((computer - you )== -1 or (computer - you == 2)):
        print("You lose !")
    else :
        print("You win !")
#SHORT CODE 

'''
Assignment: You have to import random module
 
Take first  user input the lucky number between 1 to 10
Then generate the random number between 1 to 10 using random module
Check if the random number matches the lucky number or not, if it matches come out of the loop else generate the random number till it matches the  lucky number.
'''
import random
luckyNum=int(input("enter the number b/w 1 - 10:"))
randomNum=random.randint(1,10)
print("random:",randomNum)
# res=False
while luckyNum!=randomNum:
    randomNum=random.randint(1,10)
    print("random inside loop:",randomNum)
    # if luckyNum==randomNum:
    #     res=True
    # else:
    #     res=False
# if res:
print("Matched",randomNum)


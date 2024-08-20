from random import *
import os
listnum=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninrnth","tenth"]
#random shuffling
os.system('cls')
score=0  # match score
game=0  # total number of games playes
k=1
while k==1: #to continue till the user want to play
    print("you are playing it for",listnum[game],"time.\n")
    list1=["apple","banana","orange","pear","guava","watermelon","papaya","pineapple"] #fruit collection
    list2=["tomato","carrot","cabbage","potato","onion","spinach"]     #vegetable collection
    list3=["bull","pig","rabbit","tiger","rat","dog","cat","rhino","elephant"]      # animal collection
    listcollection=[list1,list2,list3]               #collection of list of a fruit,vegetable and animal
    listchoice=choice(listcollection)                #list selection of fruit,vegetable and animal
    objectchoice=choice(listchoice)                   #object selction
    l=len(set(objectchoice))
    length=len(objectchoice)
    ans_char=[]


    def hint():#hint
        if (listchoice==list1):
            print("hint:the above word is a fruit.")
            print("starts with:",objectchoice[0])
        elif(listchoice==list2):
            print("hint:the above word is a vegetable.") 
            print("starts with:-",objectchoice[0]) 
        else:
            print("hint:the above word is a animal.") 
            print("starts with:-",objectchoice[0])   
#list creation of _
    for i in range(length):
        ans_char.append("_")    
    hint()
    print(" ".join(ans_char))
    print()
#checkin
    for j in range(l+1):
        a=input("enter a character you have guessed:")
        for i in range(length):
            if(a == objectchoice[i]):
               ans_char[i]=objectchoice[i]
            print(ans_char[i],end=" ")
        ass="".join(ans_char)#list to string
        if(ass==objectchoice):
            score=score+1
            print("\nthe word was",objectchoice)
            print("\n\n\n_______________________congratulations,you won!______________________________")     
            break
        print("\nyou have ",(l-j),"chances left.")
        
    print("\nDo you want to play again?\n")
    game=game+1
    strb=input("enter yes or no:=")
    if (strb[0]=="y"):
        k=1
    else:
        k=0
    os.system('cls')    
print("\n______________________________your score is",score,"._____________________________")
print("\n______________________________GAME END______________________________________\n\n\n\n\n")    

    
        






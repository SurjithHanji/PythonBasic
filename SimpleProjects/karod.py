questions=[["which language are used in front end","html","java","javascript","c++",0],["which language are used in front end","html","java","javascript","c++",0],
["which language are used in front end","html","java","javascript","c++",0],["which language are used in front end","html","java","javascript","c++",0]]

levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money=0
for i in range(0,len(questions)):
    question=questions[i] 
    print(f"Question for Rs.{levels[i]}")
    print(f"a.{question[1]}           b.{question[2]}")
    print(f"a.{question[3]}           b.{question[4]} ")
    reply=int(input("enter your answer(1-4) "))
    if(reply == question[-1]):
        print(f"correct answer you have won Rs.{levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=500000
    
    else:
        print("wrong answer")
        break

print(f"you take home money is {money}")
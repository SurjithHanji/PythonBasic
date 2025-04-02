def operation(a,b,ope):
    match ope:
        case 1:
            return a+b
        case 2:
            return a-b
        case 3:
            return a*b
        case 4:
            if b==0:
                return "enter more than 0"
            else:
                return a/b
        case 5:
             
             if b==0:
                return "enter more than 0"
             else:
                return a%b    
        case 6:
            return a**b
        case _:
            return "invalid ope"
        
history=[]
        
while True:
    a=int(input("enter the value of a:"))
    b=int(input("enter the value of b:"))
    
    if a<0 or b<0:
        print("u enterd negative numbers dont wry it will stil  proceed")

    print("1.sum 2.Sub 3.Mul 4.Div 5.rem 6.pow")

    ope=int(input("choose a operation to perform:"))
    res=operation(a,b,ope)
    print("result:",res)

    history.append(f"{a} {["+","-","*","/","%","**"][ope-1]} {b}={res}")
    print("history:",history)


    
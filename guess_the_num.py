import random
random.randint(0,100)
a=0
while True:
    a1=int(input("guess the number "))
    if a1<random.randint(0,100):
        print("number is small ")

    elif a1>random.randint(0,100):
        print("number is large")
    else:
        print("perfect guessing in number of attepts",a)
        
        break
    a+=1

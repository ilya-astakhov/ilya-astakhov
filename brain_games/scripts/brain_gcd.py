import random


def nod():
    print('Find the greatest common divisor of given numbers.')
    a = random.randint(1, 99)
    b = random.randint(1, 99)
    print('Question:', a, b)
    while a != b:
        if a>b:
            a=a-b
        else:
            b=b-a
    y = int(input("Your answer:"))
    if y == a:
        print('Correct!')
    else:
        y != a
        print("'",y,"' is wrong answer ;(. Correct answer was '",a,"'.\nLet's try again, Sam!")
        return
    #второй проход
    a = random.randint(1, 99)
    b = random.randint(1, 99)
    print('Question:', a, b)
    while a != b:
        if a>b:
            a=a-b
        else:
            b=b-a
    y = int(input("Your answer:"))
    if y == a:
        print('Correct!')
    else:
        y != a
        print("'",y,"' is wrong answer ;(. Correct answer was '",a,"'.\nLet's try again, Sam!")
        return
    #третий проход
    a = random.randint(1, 99)
    b = random.randint(1, 99)
    print('Question:', a, b)
    while a != b:
        if a>b:
            a=a-b
        else:
            b=b-a
    y = int(input("Your answer:"))
    if y == a:
        print('Correct!'\nCongratulations, Sam!)
    else:
        y != a
        print("'",y,"' is wrong answer ;(. Correct answer was '",a,"'.\nLet's try again, Sam!")
        return

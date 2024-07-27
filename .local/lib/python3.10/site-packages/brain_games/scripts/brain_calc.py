import random

def even():
    print('What is the result of the expression?')
    a = random.randint(1, 9) #первый проход
    b = random.randint(1, 9)
    seq = ['+', "-", "*"]
    c = random.choice(seq)
    print("Question:", a, c, b)
    if c == '+':
        d = a + b
    elif c == '-':
        d = a - b
    elif c == '*':
        d = a * b
    #print(d)
    y = int(input("Your answer:"))
    if y == d:
        print('Correct!')
    else:
        y != d
        print("'",y,"' is wrong answer ;(. Correct answer was '",d,"'.\nLet's try again, Sam!")
        return
    a = random.randint(1, 9) #второй проход
    b = random.randint(1, 9)
    seq = ['+', "-", "*"]
    c = random.choice(seq)
    print("Question:", a, c, b)
    if c == '+':
        d = a + b
    elif c == '-':
        d = a - b
    elif c == '*':
        d = a * b
    y = int(input("Your answer:"))
    if y == d:
        print('Correct!')
    else:
        y != d
        print("'",y,"' is wrong answer ;(. Correct answer was '",d,"'.\nLet's try again, Sam!")
        return
    a = random.randint(1, 9) #третий проход
    b = random.randint(1, 9)
    seq = ['+', "-", "*"]
    c = random.choice(seq)
    print("Question:", a, c, b)
    if c == '+':
        d = a + b
    elif c == '-':
        d = a - b
    elif c == '*':
        d = a * b
    y = int(input("Your answer:"))
    if y == d:
        print('Correct!\nCongratulations, Sam!')
        return
    else:
        y != d
        print("'",y,"' is wrong answer ;(. Correct answer was '",d,"'.\nLet's try again, Sam!")
        return
even()

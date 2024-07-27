import random


def progression():
    print('What number is missing in the progression?')
    a = random.randint(1, 50)
    b = random.randint(2, 4)
    c = random.randint(0, 6)
    list = [a, a+1*b, a+2*b, a+3*b, a+4*b, a+5*b, a+6*b]
    x=(list[c])
    list[c] = '..'
    result = ' '.join(str(item) for item in list)
    print("Question:", result)
    y = int(input("Your answer:"))
    if y == x:
        print('Correct!')
    else:
        y!= x
        print("'",y,"' is wrong answer ;(. Correct answer was '",x,"'.\nLet's try again, Sam!")
    #вторая проходка
    a = random.randint(1, 50)
    b = random.randint(2, 4)
    c = random.randint(0, 6)
    list = [a, a + 1 * b, a + 2 * b, a + 3 * b, a + 4 * b, a + 5 * b, a + 6 * b]
    x = (list[c])
    list[c] = '..'
    result = ' '.join(str(item) for item in list)
    print("Question:", result)
    y = int(input("Your answer:"))
    if y == x:
        print('Correct!')
    else:
        y != x
        print("'", y, "' is wrong answer ;(. Correct answer was '", x, "'.\nLet's try again, Sam!")
    #третья проходка
    a = random.randint(1, 50)
    b = random.randint(2, 4)
    c = random.randint(0, 6)
    list = [a, a + 1 * b, a + 2 * b, a + 3 * b, a + 4 * b, a + 5 * b, a + 6 * b]
    x = (list[c])
    list[c] = '..'
    result = ' '.join(str(item) for item in list)
    print("Question:", result)
    y = int(input("Your answer:"))
    if y == x:
        print('Correct!\nCongratulations, Sam!')
    else:
        y != x
        print("'", y, "' is wrong answer ;(. Correct answer was '", x, "'.\nLet's try again, Sam!")

progression()

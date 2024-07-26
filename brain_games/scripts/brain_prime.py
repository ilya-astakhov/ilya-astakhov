import random


def prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    # первый проход
    x = random.randint(2, 101)
    print('Question:', x)
    y = (input("Your answer:"))
    if y in ['yes'] and (x==2 or x==3 or x==5 or x==7 or x==11 or x==13 or x==17 or x==19 or x==23 or x==29 or x==31 or x==37 or x==41 or x==43 or x==47 or x==53 or x==59 or x==61 or x==67 or x==71 or x==73 or x==79 or x==83 or x==89 or x==97 or x==101):
        print('Correct!')
    elif y in ['yes'] and (x!=2 or x!=3 or x!=5 or x!=7 or x!=11 or x!=13 or x!=17 or x!=19 or x!=23 or x!=29 or x!=31 or x!=37 or x!=41 or x!=43 or x!=47 or x!=53 or x!=59 or x!=61 or x!=67 or x!=71 or x!=73 or x!=79 or x!=83 or x!=89 or x!=97 or x!=101):
        print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again,")
    elif y in ['no'] and (x==2 or x==3 or x==5 or x==7 or x==11 or x==13 or x==17 or x==19 or x==23 or x==29 or x==31 or x==37 or x==41 or x==43 or x==47 or x==53 or x==59 or x==61 or x==67 or x==71 or x==73 or x==79 or x==83 or x==89 or x==97 or x==101):
        print("'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again,")
    elif y in ['no'] and (x!=2 or x!=3 or x!=5 or x!=7 or x!=11 or x!=13 or x!=17 or x!=19 or x!=23 or x!=29 or x!=31 or x!=37 or x!=41 or x!=43 or x!=47 or x!=53 or x!=59 or x!=61 or x!=67 or x!=71 or x!=73 or x!=79 or x!=83 or x!=89 or x!=97 or x!=101):
        print('Correct!')
    else:
        return

prime()

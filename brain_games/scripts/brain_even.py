from random import randint
from brain_games.cli import welcome_user


def main():
    welcome_user()


if __name__ == '__main__':
    main()


def even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    x = randint(1, 999)
    print('Question:', x)
    y = (input("Your answer:"))
    if y in ['yes'] and x % 2 == 0:
        print('Correct!')
    elif y in ['yes'] and x % 2 != 0:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again," name)
	return
    elif y in ['no'] and x % 2 != 0:
        print('Correct!')
    else:
        y in ['no'] and x % 2 == 0
        print("'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again," name)
	return
    x = randint(1, 999) #второй проход
    print('Question:', x)
    y = (input("Your answer:"))
    if y in ['yes'] and x % 2 == 0:
        print('Correct!')
    elif y in ['yes'] and x % 2 != 0:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again," name)
	return
    elif y in ['no'] and x % 2 != 0:
        print('Correct!')
    else:
        y in ['no'] and x % 2 == 0
        print("'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again," name)
	return
    x = randint(1, 999) #третий проход
    print('Question:', x)
    y = (input("Your answer:"))
    if y in ['yes'] and x % 2 == 0:
        print('Correct!\nCongratulations, ', name)
	elif y in ['yes'] and x % 2 != 0:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again," name)
	return
    elif y in ['no'] and x % 2 != 0:
        print('Correct!\nCongratulations, ', name)
    else:
        y in ['no'] and x % 2 == 0
        print("'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again," name)
	return

# variable

def get_guess():
    guess = input("enter a number:")
    return guess


def main():
    guess = get_guess()
    print('You entered:', guess)
    if guess == 50:
        print('your guess is correct')
    else:
        print('your guess is wrong')


main()
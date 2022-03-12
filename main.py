from random import randint

def get_six():
    six = set()
    while len(six) < 6:
        six.add(randint(0, 49))
    return six


def main():
    result = get_six()
    user_try = set()
    counter = 0

    while user_try != result:
        user_try = get_six()
        counter += 1


    print('result: ', result)
    print('six: ', user_try)
    print(counter)

if __name__ == '__main__':
    main()
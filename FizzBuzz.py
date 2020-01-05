def main():
    fizz_buzz()


def fizz_buzz():
    word = ""
    for i in range(1, 101):
        word = i
        if check_number(i, 15):
            word = "FizzBuzz"
        elif check_number(i, 5):
            word = "Buzz"
        elif check_number(i, 3):
            word = "Fizz"
        print(word)
    return


def check_number(current_number, mod_number):
    return current_number % mod_number == 0


main()

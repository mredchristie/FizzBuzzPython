for num in range(1,101):
    string = ""
    if num % 3 == 0:
        string +="Fizz"
    if num % 5 == 0:
        string += "Buzz"
    if num % 3 != 0 and num % 5 != 0:
        string = str(num)
    print(num, string)
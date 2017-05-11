def factorial(num):

    total = 1

    for number in range(1, num ):
        new_num = number + 1
        number *= new_num
        total = total * new_num


    print("The factorial total for " + str(num) + " is: " + str(total) + ".")

factorial(3)
factorial(5)
factorial(6)
factorial(10)
factorial(20)

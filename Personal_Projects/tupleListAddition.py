
print('Enter numbers in a list to add them together \n')
go = True
while go is True:
    tuply = input("enter a list, separated by spaces> ")
    try:
        if '' == tuply:
            print('nothing is there. \n')
        else:

            thing = (tuply.split())
            print(*thing)
            thing1 = [int(item) for item in thing]
            a = 0
            for i in thing1:
                a += i
            print(a)
            go = False
    except ValueError:
        print("error, only integers are allowed \n")

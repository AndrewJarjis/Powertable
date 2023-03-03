while True:
    num = int(input("Enter an integer: "))

    print("Number\tSquare\tCube")
    for i in range(1, num+1):
        square = i**2
        cube = i**3
        print(f"{i:6}\t{square:6}\t{cube:4}")

    response = input("Do you want to continue? (y/n): ")
    if response.lower() == 'n':
        break

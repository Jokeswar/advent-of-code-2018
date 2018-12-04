with open("input", "r") as input:
    lines = input.readlines()
    two_letters = 0
    three_letters = 0

    for line in lines:
        mod_2 = 0
        mod_3 = 0
        for i in range(ord('a'), ord('z') + 1):
            if line.count(str(chr(i))) == 2 and mod_2 == 0:
                two_letters += 1
                mod_2 = 1

            if line.count(str(chr(i))) == 3 and mod_3 == 0:
                three_letters += 1
                mod_3 = 1

print(two_letters * three_letters)
                
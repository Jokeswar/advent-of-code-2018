with open("input", "r") as input:
    lines = input.readlines()

    for line1 in lines:
        for line2 in lines:
            count = 0
            ans = ""
            if line1 != line2:
                for i in range(len(line1) - 1):
                    if line1[i] != line2[i]:
                        count += 1
                    
                if count == 1:
                    for i in range(len(line1)):
                        if line1[i] != line2[i]:
                            ans = line1.replace(line1[i], "")
                            print(ans)
                            exit()
                
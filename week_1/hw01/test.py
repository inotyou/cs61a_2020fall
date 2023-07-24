list = [i for i in range(1, 13)]
for i in list[-1::-1]:
    if 13 % i == 0:
        print(i)
        break

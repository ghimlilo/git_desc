def abc(num):
    result=[]
    for i in range(1, num+1):
        if i % 2 == 0:
            result.append(i)
    print(result)

abc(50)

def upperlower(l):
    upper = 0
    lower = 0

    for x in l:
        for i in range(len(x)):
            if (ord(x[i]) >= 97 and ord(x[i]) <= 122):
                lower += 1
            elif (ord(x[i]) >= 65 and ord(x[i]) <= 90):
                upper += 1
    
    print(upper)
    print(lower)

list = ['Python','Php','Java']

upperlower(list)




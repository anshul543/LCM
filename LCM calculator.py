def LCM():
    x = int(input('n'))
    y = int(input('p'))
    if x > y:
            smaller = y
    else:
            smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
            lcm = x * y / hcf
    return lcm

LCM()

    
        

def tem_igual(*args):
    for i in range(len(args)-1):
        n = args[i]
        for k in range(i+1, (len(args))):
            if args[i] == args[k]:
                return True
    return False

print(tem_igual(1,2,3,4,2))


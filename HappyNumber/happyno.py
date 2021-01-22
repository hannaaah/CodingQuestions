import sys
import os

while(1):
    os.system("clear")
    ch = int(input("\n\nPress\n1. To enter a positive integer\n2. To exit\n\nEnter your choice: "))
    if ch == 1:
        num = int(input('Enter a positive integer: '))
        l = []
        l.append(num)
        while(1):
            t = l[-1]
            sum = 0
            while(t>0):
                d = t%10
                sum += (d*d)
                t//=10
            if sum == 1:
                print("\n\n  Happy Number :)\n\n\n")
                break
            else:
                if sum  in l:
                   print("\n\n  Not a Happy Number :(\n\n\n")
                   break
                else:
                   l.append(sum)
        any = input("\n\n\n\n\n\nPress any key to go back.")
    elif ch == 2:
        sys.exit()
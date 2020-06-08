def main():
    n = str(input("Enter a number: "))
    k = int(input("Enter a duplicating value: "))

    p = (n * k)

    if len(p) == 1:
        print(p)
    elif len(p) > 1:
        print(super_digit(p))

def super_digit(x):
    s = 0

    for i in x:
        s += int(i)

    s = str(s)
    
    if len(s) == 1:
        return s
    elif len(s) > 1:
        return super_digit(s)

main()
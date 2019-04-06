def table(n):
    return lambda a:a*n #a will contain the iteration i and a multiple
n=int(input("Enter a number : "))
b=table(n)
for i in range(1,11):
    print(n,"X",i,"=",b(i))
    
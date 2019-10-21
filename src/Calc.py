

m = eval(input("请输入m："))
n = eval(input("请输入n："))
sum = 0
for x in range(m,n):
    sum += x**2+1/x


print("sum = {}".format(sum))



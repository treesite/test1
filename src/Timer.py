import time



totaltime = eval(input("输入倒计时总时间："))
total = totaltime

print("{}秒倒计时开始".format(totaltime).center(20, '-'))

st = time.time()

for n in range(totaltime+1):
    finish = '▮' * (totaltime-n)
    re = '▯'*n
    print("\r{}{}\t{}".format(finish, re, total), end='')
    if total == 0:
        break
    time.sleep(1)
    total -= 1

print("\n{}秒倒计时结束".format(totaltime).center(20, '-'))

et = time.time()

print("误差：{:.3f}%".format((et-st)/100))













#while的意思是只要在我规定内，你就一直在循环中，只有违反我的规定，你才能跳出循环
#def power(x, n):
    s = 1
    while n > 0:#只要n>0就一直在我循环内，就执行不了return，
        n = n - 1#只有违反n>0，也就是n<=0才能执行return
        s = s * x
    return s

names=['Near', 'Bob', 'Tracy']
for name in names:
	print(name,'nihao')

sum=0
list(range(10))
for x in range(10):#range后面不是[]!!!!括号（）！！！！
        sum=sum+x
        print(sum)    

# 计算1+2+3+...+100:
sum = 0
n = 1
while n <= 100:
    sum = sum + n
    n = n + 1
print(sum)
# 计算1x2x3x...x100:
acc = 1
n = 1
while n <= 100:
    acc = acc * n
    n = n + 1
print(acc)  

sum = 0
n = 99
while n > 0:#只要n>0就在这个循环内
    sum = sum + n
    n = n - 2#减到最后不能比0小
print(sum)

sum=0
n = 1
while n<=100:#只要n<=100就在这个循环内
	sum = sum + n
	n += 2#加到最后不能比100大
print(sum)

n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    print(n)

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

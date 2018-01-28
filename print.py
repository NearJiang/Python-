print('100+200=',100+200)

print(1.23e9)#e9=10的9次方
print(1.2e-5)
#e-5=10的-5次方，它会输出1e-05,不是他没有变化，而是它自动将0.00001转换成1e-05
print('I\'m ok') #字符串内含单引号，可用转义符号\来标识
print('I"m ok')#双引号不需转义啊！why？？

print('\\')#想要输出\这个符号也得用它自己转义下

print("学号\t姓名\t语文\t数学\t英语")#\t制表符，自己F5试试，全部对齐啦
print("2017001\t曹操\t99\t88\t0")
print("2017002\t周瑜\t92\t45\t93")
print("2017008\t黄盖\t77\t82\t100")

print(r'\\ \n \t')#r''防止转义，就是你这里面有\,\n.\t统统不会有用


print('I\'m learning\n Python')#\n换行
print('''line1
line2
line3
sadas''')#'''xx'''也表换行

print(r'''\\
\t
\n''')#r'''xx'''换行有禁止转义

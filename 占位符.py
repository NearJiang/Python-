print('hello,%s' %'world')#s“字符串”

print('hello,%d' % 5)#d整数

print('hello,%f' % 0.5)#f浮点数


print('%.2d' % 3)#输出几位整数
print('%.2d' % 13)
print('%.2d' % 0.3)
print('%.2d' % 123)#大于设置的数就照常显示



print('%.2f' % 3.1415926)#f保留小数点后的位数


#想单纯用百分比%时，可用%%转义
print( 'growth rate: %d %%' % 7)



#也可用.format()代替%占位,  .1f就是保留小数点后面1位
print('Hello,{0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
print('Hello,{0}, 成绩提升了 {1}%'.format('小明', '滚出去'))

print('小明数学期中考72，期末考85，小明成绩提升了"%.1f"：'% (85/72) )

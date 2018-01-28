print('hey,here is a simple test for your bmi,thank you for you help')
name=input('please enter ur name:')
h=float(input('please enter %s height(sample:1.75): '% name))#float浮点数，int整数
w=float(input('please enter %s weight(sample:65): '% name))
bmi=w/(h**2)#**2就是平方，**3就是立方  这种里面有乘除的就先定义下，再print，不要上了就print什么什么，很容易出错
if bmi<18.5:
	print('%s u r silm,BMI result %.1f' %(name,bmi))
elif bmi>=18.5 and bmi<25:
    print('%s,you are good,BMI result is %.1f' % (name,bmi))
elif bmi>=25 and bmi<28: 
    print('%s,you are heavy,BMI result is %.1f' % (name,bmi))
elif bmi>=28 and bmi<32: 
    print('%s,you are fat,BMI result is %.1f' % (name,bmi))
elif bmi>=32:
    print('%s,you are too fat,BMI result is %.1f' % (name,bmi))

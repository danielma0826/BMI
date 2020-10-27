
height=eval(input('請輸入身高（cm)='))
weight=eval(input('請輸入體重（KG)='))
bmi=weight/((height/100)**2)
bmi = int(bmi)
print('此人的BMI=', bmi)

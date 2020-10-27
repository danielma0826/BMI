#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#height=eval(input('請輸入身高（cm):'))
#weight=eval(input('請輸入體重（KG):'))
#bmi=weight/ ((height/100)**2)
#print('此人的bmi為：' ,bmi)


height=eval(input('請輸入身高（cm)='))
weight=eval(input('請輸入體重（KG)='))
bmi=weight/((height/100)**2)
bmi = int(bmi)
print('此人的BMI=', bmi)

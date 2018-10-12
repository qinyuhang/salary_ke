#!/usr/bin/env python3
print ('本公式适用于3个月年终奖的计算，未精确计算每月补助的免征额，具体情况具体分析，仅供参考！')
print ('请输入扣除五险一金后的工资，即年年有余无余额时每月能领取的最大额度')
salary = int(input())
print ('请输入年终奖的基数，即未扣除五险一金的薪资')
bonus = int(input())
avg = ((salary - 5000) * 12 + bonus * 3) / (12 + 12)
print ('每月领取的最佳工资{0}，即尽量保证每月领取数额'.format(avg))

print ('以上内容适用于从一月份开始操作岁岁有余的情况')
print ('--')
print ('以下内容适用于当前岁岁有余已有余额的情况')

print ('请输入全年还有几个月份工资')
month = int(input())
print ('请输入岁岁有余当前已存余额')
nnyy = int(input())
balance = (nnyy + (salary - 5000) * month + bonus * 2) / (month + 12)
print ('每月领取的最佳工资{0}，即尽量保证每月领取数额'.format(balance))

def Subway_fare(days):
    Eve_day_money = 12
    DayAllMoney = 0
    M_100 = 0
    M_150 = 0
    M_300 = 0
    Max = 0
    Month_All_Money = 0
    for i in range(1,days+1):
        if DayAllMoney <= 100:
            DayAllMoney += Eve_day_money
            M_100 +=Eve_day_money
        elif DayAllMoney < 150:
            DayAllMoney += Eve_day_money * 0.8
            M_150 +=Eve_day_money * 0.8
        elif DayAllMoney < 300:
            DayAllMoney += Eve_day_money * 0.5
            M_300 += Eve_day_money * 0.5
        else:
            DayAllMoney += Eve_day_money
            Max += Eve_day_money

        i+=1 #乘车天数
        Month_All_Money = M_100+M_150+M_300+Max
    return Month_All_Money
    # print('您当月乘坐地铁的天数为%d,总的乘车费用为:%.2f' % (days,M_100+M_150+M_300+Max))
while True:
    days = input('请输入您该月乘车天数：\n')
    if days.isdigit():
        days = int(days)
        print('您该月的乘车费用为%.2f' % Subway_fare(days))
    else:
        print('您输入的乘车天数有误。')
        break
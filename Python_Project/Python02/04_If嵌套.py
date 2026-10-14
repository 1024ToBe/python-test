score = int(input('请输入你的成绩:'))
if 0<= score <= 100:
    print('成绩有效，开始评判等级')
    if score >= 90:
        print('成绩等级:优秀')
    elif score >= 80:
        print('成绩等级:良')
    elif score >= 70:
        print('成绩等级:合格')
    else:
        print('成绩不合格')
else:
    print('成绩无效')
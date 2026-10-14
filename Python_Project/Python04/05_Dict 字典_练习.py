dict1 = {}
print(dict1,type(dict1))

dict2 = dict()
print(dict2,type(dict2))

dict3 = {"张三":18, "李四":28, "王武":38}
print(dict3,type(dict3))

dict4 = {1:dict1, 2:dict2, 3:dict3}
print(dict4,type(dict4))

score_dict = {
    '张三':{'语文':99,'数学':99,'英语':99,},
    '李四':{'语文':90,'数学':89,'英语':99,},
    '王五':{'语文':89,'数学':79,'英语':89,}
}
print(score_dict,type(score_dict))
print(score_dict['张三'])


score_dict = {'李四': 80, '王五': 99, '赵六': 90, '张三': 100, '田七': 100}
for k in score_dict:
    v = score_dict[k]
    print(v)

for k  in score_dict.keys():
    v = score_dict.get(k)
    print(f"{k}的分数是:{v}")

#推荐 拆包样式
for k,v in score_dict.items():
    print(f'{k}的分数是{v}')


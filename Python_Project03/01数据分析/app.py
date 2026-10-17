from  file_reader import FileReader
from data_class import DataClass

from pyecharts import options as opts
from pyecharts.charts import Bar

def read_all_data(csv_path,json_path)->list[DataClass]:
    # fr1 = FileReader(f'/Users/jolly2/Desktop/黑马/代码/python-test/2026-04销售数据.csv')
    # fr2 = FileReader(f'/Users/jolly2/Desktop/黑马/代码/python-test/2026-05销售数据.txt')
    fr1 = FileReader(csv_path)
    fr2 = FileReader(json_path)


    ls1 = fr1.read_csv()
    ls2 = fr2.read_json()

    all_data = ls1 + ls2
    return all_data


#得到每日的销售额
def data_process(data:list[DataClass]):
    #用来存储计算好的 {日期：营业额}
    data_dic = {}
    for dc in data:
        #日期 key 已存在过
        if dc.date in data_dic:
            # old_value = data_dic[dc.date]
            # data_dic[dic.date] = old_value + dc.sale_amount
            data_dic[dc.date] += dc.sale_amount
        else:
            data_dic[dc.date] = dc.sale_amount

    #推导式 字典转列表
    data_list = [(k, v) for k, v in data_dic.items()]

    #方便排序，list内是元组，默认按元组第一个元素作为排序依据
    data_list.sort()

    l1 = [t[0] for t in data_list]
    l2 = [t[1] for t in data_list]
    #拆包： return a,b  = return(a,b)
    #返回元组(date_list,amount_list)
    return l1,l2

    # return data_list

def create_sales_bar(date_list, amount_list):
    """
    生成销售额柱状图
    :param date_list: 日期字符串列表 x轴
    :param amount_list: 销售额float列表 y轴，与日期一一对应
    :return: bar对象，可渲染html
    """
    bar = (
        Bar()
        .add_xaxis(date_list)
        .add_yaxis(
            "销售额",
            amount_list,
            color="blue",
            stack="",
            label_opts=opts.LabelOpts(is_show=False), # 关闭柱子上方文字
            bar_width="60%" # ✅柱子宽度放在这里！
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="黑马程序员数据分析案例"),
            # X轴旋转，缩小字体
            xaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(rotate=-45, font_size=10),
            ),
        )
    )
    return bar


lst = read_all_data(f'/Users/jolly2/Desktop/黑马/代码/python-test/2026-04销售数据.csv',
                    f'/Users/jolly2/Desktop/黑马/代码/python-test/2026-05销售数据.txt')

print(data_process(lst))
date_list,amount_list = data_process(lst)
print(date_list)
print(len(date_list))
print(amount_list)
print(len(amount_list))

# ============测试示例代码（你可以删掉或者保留）============
if __name__ == "__main__":
    print('第一步数据列表内容：',lst)
    print('第一步数据列表内容类型：', type(lst[0]))
    bar_chart = create_sales_bar(date_list, amount_list)
    bar_chart.render("sales_bar.html")

    print("图表已生成 sales_bar.html，直接打开即可查看")

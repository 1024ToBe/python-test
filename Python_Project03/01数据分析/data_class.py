#1.封装数据类，用类对象存放数据
class DataClass():
    def __init__(self,date,order_id,sale_amount,province):
        self.date = date
        self.order_id = order_id
        self.sale_amount = sale_amount
        self.province = province

    # 如果单独打印对象用__str__
    def __str__(self):
        return f"{self.date},{self.order_id},{self.sale_amount},{self.province}"

    # 如果对象在[容器内]，要输出，需要用__repr__
    def __repr__(self):
        return f"{self.date},{self.order_id},{self.sale_amount},{self.province}"


if __name__ == '__main__':
    arr = ['2026-04-15','ORD5272517',1434.04,'河南']
    dc = DataClass(arr[0], arr[1], float(arr[2]), arr[3])
    print(dc)


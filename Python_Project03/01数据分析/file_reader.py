from data_class import DataClass
import json
#读取文件类
class FileReader():
    def __init__(self,file_path,encoding='utf8'):
        try:
            self.fr = open(file_path, 'r', encoding=encoding)
        except Exception as e:
            print('文件读取失败，原因：', e)
    def read_csv(self)->list[DataClass]:
        data_list = []
        self.fr.seek(0)
        #从第一行开始读,因为第0行是表头
        for line in self.fr.readlines()[1:]:
            #去掉自动读取到的换行符\n
            line = line.strip()
            arr = line.split(',')

            #float 一定要转数字，否则后面累加营业额会计算成字符串
            dc = DataClass(arr[0],arr[1],float(arr[2]),arr[3])
            data_list.append(dc)
        return data_list

    def read_json(self)->list[DataClass]:
        #{"日期":"2026-05-01","订单ID":"ORD7392645","销售额":4885,"省份":"广东"}
        #把json字符串转化为字典: 字典 = json.loads(字符串)
        data_list = []
        self.fr.seek(0)
        for line in self.fr.readlines():
            # 去掉自动读取到的换行符\n
            line = line.strip()
            data_dict = json.loads(line)
            #使用()
            dc = DataClass(data_dict['日期'],data_dict['订单ID'],data_dict['销售额'],data_dict['省份'])
            data_list.append(dc)
        return data_list

if __name__ == '__main__':
   # fr = FileReader(f'/Users/jolly2/Desktop/黑马/代码/python-test/2026-04销售数据.csv')
    fr = FileReader(f'/Users/jolly2/Desktop/黑马/代码/python-test/2026-05销售数据.txt')
    print(fr.read_json())





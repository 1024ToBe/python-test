from  testM2 import show2
def show1(a,b):
    print('两数之和=',a+b)
    return a+b

def copy1():
    with open('../sources/file.mp4', 'rb') as filein, open('backup/file(copy).mp4', 'wb') as fileout:
        while True:
            chunk = filein.read(1024*1024)
            if not chunk:
                break
            fileout.write(chunk)



#确保只在当前页面执行，被其他模块调用时不执行
if __name__ =='__main__':
    show1(1,2)
__all__ = ['show2']
def show2():
    print('just print')

def copy2():
    with open('../test.txt', 'r', encoding='utf8') as fin, open('../new_word.txt', 'w') as fout:
        while True:
            chunk = fin.read()
            if not chunk:
                break
            fout.write(chunk)

if  __name__ == '__main__':
    show2()
    #copy2()
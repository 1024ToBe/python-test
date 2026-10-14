#导包
import ollama

'''
#连接本地ollama服务
client = ollama.Client('http://127.0.0.1:11434')

#封装成函数
def get_ollama_response(prompt):
    # 选择模型以及角色 然后开始聊天
    result = client.chat(
        model='qwen2.5:1.5b',
        messages=[
            {'role': 'user', 'content': prompt}
        ],
        stream = False
    )
    print(result.message.content)

if __name__ == '__main__':
    get_ollama_response('你是谁？')
    get_ollama_response('给我讲一个冷笑话')
'''

# 注意:ollama默认可以直接调用本地本地大模型: http://127.0.0.1:11434
# 如果要调用linux大模型,创建Client客户端需要修改url: http://linux服务器ip:11434
# 2.需求: 用户输入对应问题,调用ollama本地模型,返回结果
# 2.1 获取用户问题
# TODO 以后从页面获取问题,本次先写固定的问题
question =  """
你需要对用户的反馈进行原因分类。
分类包括：价格过高、售后支持不足、产品使用体验不佳、其他。
回答格式为：分类结果：xx。
用户的问题是：商品不小心掉地上了, 把地板砸坏了.
"""
print(f"用户输入的问题:{question}")
# 2.2 使用ollama本地模型,返回结果
ai_response = ollama.chat(model="qwen2.5:1.5b", messages=[{"role": "user", "content": question}])
print(f"AI返回的完整结果:{ai_response}")
# 2.3 从ai返回结果中获取答案
result = ai_response['message']['content']
print(f"AI返回的答案:{result}")




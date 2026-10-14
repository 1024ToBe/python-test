import ollama

#连接本地ollama服务
client = ollama.Client('http://127.0.0.1:11434')

#封装成函数
def get_ollama_response(messages):
    # 选择模型以及角色 然后开始聊天
    result = client.chat(
        model='qwen2.5:1.5b',
        messages = messages[-10:],
        stream = False
    )
    print(result.message.content)
    return  result.message.content

if __name__ == '__main__':
    messages = [{'role': 'user', 'content': '你是谁'}]
    result1 = get_ollama_response(messages)
    messages.append({'role': 'assistant', 'content':result1 })
    # messages.append({'role': 'user', 'content': '给我讲一个笑话'})
    # result2 = get_ollama_response(messages)
    # messages.append({'role': 'assistant', 'content': result2})
    print(messages)


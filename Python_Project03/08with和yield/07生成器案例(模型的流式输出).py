import ollama
client = ollama.Client('http://127.0.0.1:11434')
content = ''
def ollama_chat(query):
    result = client.chat(
        model='qwen2.5:1.5b',
        messages=[
            # {'role':'system','content':content}
            {'role':'user','content':query}
        ],
        stream=True,  #开启流，此时类型是generator

    )

    # print(result.message.content)
    print(type(result))

    for chunk in result:
        # print(chunk)
        # print(type(chunk))
        if not chunk.message.content:
            print(chunk.message.thinking,end='')
        else:
            print(chunk.message.content,end='')





ollama_chat('你是谁')
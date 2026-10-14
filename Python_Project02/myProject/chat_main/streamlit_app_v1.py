import streamlit as st
from chat_utils.ollama_chat_result import get_ollama_response

#标题
st.title('黑马智聊机器人')
#分割线
st.divider()
#构建聊天窗口
#1.ai 开场白
begin_str = '您好，我是黑马智聊机器人，有什么可以帮助您的吗？'
st.chat_message('assistant').write(begin_str)
messages = [{'role': 'user', 'content': begin_str}]

#2.用户输入问题
prompt = st.chat_input('请输入您要咨询的问题')
#3.用户底部输入框输入的内容展示到上面
if prompt:
    st.chat_message('user').write(prompt)
    messages.append ({'role': 'user', 'content': prompt})
    #4.TODO AI 根据用户的问题 去大模型调取答案
    response = get_ollama_response(messages)
    #把 AI 回答的答案拼接到里面
    messages.append({'role': 'assistant', 'content': response})
    #5.把答案读取到之后 再放到上面展示出来
    st.chat_message('assistant').write(messages.con)
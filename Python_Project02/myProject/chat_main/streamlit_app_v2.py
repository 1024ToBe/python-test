import streamlit as st
from chat_utils.ollama_chat_result import get_ollama_response

#标题
st.title('黑马智聊机器人')
#分割线
st.divider()


if 'messages' not in st.session_state:
    #先添加第一条 AI提示， 后面的就都是实时拼接的信息了
    st.session_state['messages'] = [{'role': 'assistant', 'content': '您好，我是黑马智聊机器人，有什么可以帮助您的吗？'}]

#构建聊天窗口
#1.AI 先说话
for message in st.session_state['messages']:
    st.chat_message(message['role']).write(message['content'])

#2.用户问问题
prompt = st.chat_input('请输入您要咨询的问题')
#3.用户底部输入框输入的内容展示到上面
if prompt:
    # 如果用户底部输入框输入内容，展示到上面并添加记忆
    st.chat_message('user').write(prompt)
    st.session_state['messages'].append({'role': 'user', 'content':prompt})

    #AI回答
    #调用A I 大模型获取答案
    with st.spinner('正在思考中...'):
        res = get_ollama_response(st.session_state['messages'][-30:])
    #如果获取到 AI 的答案 就展示到页面上并添加记忆
    st.chat_message('assistant').write(res)
    st.session_state['messages'].append({'role': 'assistant', 'content':res})


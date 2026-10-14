#1.倒包
import streamlit as st

#2.构建用户注册平台
st.title('传智教育用户注册平台')
name = st.text_input('请输入用户名：')
pwd = st.text_input('请输入密码：',type='password')
age = st.number_input('请输入年龄：',min_value = 0,max_value=100,value=22)
gender = st.radio('请选择性别：',options=['男','女','保密'],horizontal=True)
birth = st.date_input('请选择出生日期：')
height = st.slider('请选择身高：',min_value=0.0,max_value=300.0,value=167.0)
result = st.button('确认')
if result:
    print('恭喜你,信息录入成功')
    print(name,pwd,age,gender,birth,height)
    with open('user.txt', 'a', encoding='utf8') as f:
        f.write(f'{name},{pwd},{age},{gender},{birth},{height}'+'\n')
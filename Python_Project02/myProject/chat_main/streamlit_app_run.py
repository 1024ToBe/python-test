#导包
import os

# 先把当前目录切换到脚本所在目录(myProject)
os.chdir(os.path.dirname(__file__))
#执行 ../代表先从myproject/test 退一层级回到myproject 目录
os.system('streamlit run streamlit_app_v2.py')


import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
import koreanize_matplotlib

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 본 프로젝트 차트 모듈
import charts


# page setting
st.set_page_config(
   page_title="[지출코드 3] 의류 및 신발 - 으4으4",
    layout="wide"
)

@st.cache
def load_data(url):
    return pd.read_csv(url)
url1 = "data/out/raw01.csv"
url2 = "data/out/raw02.csv"
# raw01 = load_data(url1)
# raw02 = load_data(url2)
raw01 = pd.read_csv(url1)
raw02 = pd.read_csv(url2)
code3 = pd.read_csv('data/out/code3.csv')


st.markdown('# 지출코드 3 - 의류 및 신발')
st.markdown('''
            **분석1.** 분석1. 2012년 ~ 2016년, 2019년~2020년에 의류 및 신발 물가가 상승함에 따라 가계지출이 감소하였습니다.  
            이는 가격이 비싸졌음에도 불구하고 지출금액이 감소하였다는 것은 사람들의 소비량이 감소했다는 것으로 해석할 수 있습니다.    
            ''')
st.markdown('따라서 의류 및 신발은 **물가에 민감한 항목**이라고 볼 수 있습니다. ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

# 소비지수별 가계지출

st.markdown('##### 대상 품목')
code3
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

# 지출코드3
st.markdown(' ')
st.markdown('##### 연도 별 소비자물가지수와 가계지출')
df_raw_3 = raw02[raw02["지출코드"] == 3]
fig = charts.linebar(df_raw_3, x='연도', y='가계지출', sy='소비자물가지수')
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 소득계층 별 물가지수와 가계지출')
temp = df_raw_3[(df_raw_3["가구형태"] != "전체가구") & (df_raw_3["소득계층"] != "전체")]
fig = charts.multiLineGroup(temp, x='소비자물가지수', y='가계지출', color='소득계층', fcol='가구형태')
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 소득계층 별 소비자물가지수에 따른 가계지출')
temp = df_raw_3[(df_raw_3["가구형태"] == "전체가구") & (df_raw_3["소득계층"] != "전체")]
fig = charts.scatter(temp, x='소비자물가지수', y="가계지출", color="소득계층", size="가계지출")
fig
st.markdown('')
st.markdown('')
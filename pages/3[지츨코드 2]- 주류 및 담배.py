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
   page_title="[지출코드 2] 주류 및 담배 - 으4으4",
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
code2 = pd.read_csv('data/out/code2.csv')


st.markdown('# 지출코드 2 - 주류 및 담배')
st.markdown('''
            **분석1.** 정부정책에 따라 2014년~2015년 물가지수가 급등하였으나 지수가 증가한 정도보다 지출금액이 증가한 정도가 적어보여 가격 인상으로 인해 어느정도 소비량이 줄은 것으로 보입니다.
            ''')
st.markdown('따라서 주류 및 담배는 물가에 민감한 항목은 아니나, **물가가 일정 수준 이상으로 급등하면 영향을 받는 항목**으로 보여집니다. ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

# 소비지수별 가계지출

# 지출코드2
st.markdown('##### 대상 품목')
code2
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 연도 별 소비자물가지수와 가계지출')
df_raw_2 = raw02[raw02["지출코드"] == 2]
fig = charts.linebar(df_raw_2, x='연도', y='가계지출', sy='소비자물가지수')
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 각 소득계층의 연도 별 가계지출')
temp = df_raw_2.loc[df_raw_2['소득계층'] != '전체']
temp = temp.loc[temp['가구형태'] != '전체가구']
fig = charts.scatterGroup(temp, x='연도',y='가계지출',color='가구형태',fcol='소득계층',size='가계지출', height=650)
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

# st.markdown('##### 소득계층 별 물가지수와 가계지출')
# temp = df_raw_2[(df_raw_2["가구형태"] != "전체가구") & (df_raw_2["소득계층"] != "전체")]
# fig = charts.multiLineGroup(temp, x='소비자물가지수', y='가계지출', color='소득계층', fcol='가구형태')
# fig
# st.markdown(' ')
# st.markdown(' ')
# st.markdown(' ')
# st.markdown(' ')
# st.markdown(' ')
# st.markdown(' ')
# st.markdown(' ')

st.markdown('##### 소득계층 별 소비자물가지수에 따른 가계지출')
temp = df_raw_2[(df_raw_2["가구형태"] == "전체가구") & (df_raw_2["소득계층"] != "전체")]
fig = charts.scatter(temp, x='소비자물가지수', y="가계지출", color="소득계층", size="가계지출")
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 소득계층 별 각 가구형태의 소비자물가와 가계지출')
temp = df_raw_2.loc[df_raw_2['소득계층'] != '전체']
temp = temp.loc[temp['가구형태'] != '전체가구']
fig = charts.histoGroup(temp, x='소비자물가지수',y='가계지출',color='가구형태',fcol='소득계층')
fig
st.markdown('')
st.markdown('')
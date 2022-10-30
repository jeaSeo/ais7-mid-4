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
   page_title="[지출코드 4] 주택 수도 전기 및 연로 - 으4으4",
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
code4 = pd.read_csv('data/out/code4.csv')


st.markdown('# 지출코드 4 - 주택 수도 전기 및 연료')
st.markdown('''
            **분석1.** 2012년 ~ 2016년은 물가지수상승하락에 상관 없이 가계지출이 비슷한 수준입니다.  \n
            **분석2.** 2017년 ~ 2021년은 물가지수가 상승을 했고, 가계지출도 다소 상승을 했지만 2015년과 비슷한 수준입니다.  
            따라서 소비자 물가가 큰 폭으로 상승하거나 하락하여도 사람들은 소비량을 조절해가며 일정 수준의 지출금액을 맞추려는 경향이 있는 것으로 보입니다.  
            ''')
st.markdown('따라서 주택 수도 전기 및 연료는 **물가에 민감한 항목**입니다.')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

# 소비지수별 가계지출

st.markdown('##### 대상 품목')
code4
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 연도 별 소비자물가지수와 가계지출')
df_raw_4 = raw02[raw02["지출코드"] == 4]
fig = charts.linebar(df_raw_4, x='연도', y='가계지출', sy='소비자물가지수')
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

# st.markdown('##### 소득계층 별 물가지수와 가계지출')
# temp = df_raw_4[(df_raw_4["가구형태"] != "전체가구") & (df_raw_4["소득계층"] != "전체")]
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
temp = df_raw_4[(df_raw_4["가구형태"] == "전체가구") & (df_raw_4["소득계층"] != "전체")]
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
temp = df_raw_4.loc[df_raw_4['소득계층'] != '전체']
temp = temp.loc[temp['가구형태'] != '전체가구']
fig = charts.histoGroup(temp, x='소비자물가지수',y='가계지출',color='가구형태',fcol='소득계층')
fig
st.markdown('')
st.markdown('')
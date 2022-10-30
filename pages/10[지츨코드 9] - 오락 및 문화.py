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
   page_title="[지출코드 9] 오락 및 문화 - 으4으4",
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
code9 = pd.read_csv('data/out/code9.csv')


st.markdown('# 지출코드 9 - 오락 및 문화')
st.markdown('''
            **분석1.** 2015년도 이후 물가와 지출 추세가 비슷한 형태를 보이고 있습니다.  
            이를 통해 물가가 상승하여도 소비자는 문화생활을 꾸준히 한다는 것을 알 수 있습니다.  
            오락 및 문화는 물가가 상승하여도 소비지출을 포기하지 않는 특징을 보입니다.  \n
            ''')
st.markdown('따라서 오락 및 문화는 **물가에 민감하지 않은 항목**입니다.')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

# 소비지수별 가계지출

st.markdown('##### 대상 품목')
code9
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 연도 별 소비자물가지수와 가계지출')
df_raw_9 = raw02[raw02["지출코드"] == 9]
fig = charts.linebar(df_raw_9, x='연도', y='가계지출', sy='소비자물가지수')
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')


st.markdown('##### 각 소득계층의 연도 별 가계지출')
temp = df_raw_9.loc[df_raw_9['소득계층'] != '전체']
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
# temp = df_raw_9.loc[df_raw_9['소득계층'] != '전체']
# temp = temp.loc[temp['가구형태'] != '전체가구']
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
temp= df_raw_9[(df_raw_9["가구형태"] == "전체가구") & (df_raw_9["소득계층"] != "전체")]
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
temp = df_raw_9.loc[df_raw_9['소득계층'] != '전체']
temp = temp.loc[temp['가구형태'] != '전체가구']
fig = charts.histoGroup(temp, x='소비자물가지수',y='가계지출',color='가구형태',fcol='소득계층')
fig
st.markdown('')
st.markdown('')
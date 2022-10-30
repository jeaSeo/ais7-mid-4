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
   page_title="[지출코드 11] 음식 및 숙박 - 으4으4",
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
code11 = pd.read_csv('data/out/code11.csv')


st.markdown('# 지출코드 11 - 음식 및 숙박')
st.markdown('''
**분석 1** 2012 ~ 2016년도의 물가는 계속 상승한 반면, 지출은 일정 금액을 유지하고 있습니다.  
이를 통해 소비자는 해당 품목에 대해 적정한 지출을 유지하고 있음을 알 수 있습니다.  \n
**분석 2** 2017년도 이후 가계지출이 늘어났습니다.  
이는 최저임금 이슈로 인해 해당 품목이 ‘외부 요인’에 영향을 받았다는 것을 알 수 있습니다.  \n
**분석 3** 2019년도 이후 가계지출이 급락한 형태를 보인다. 이는 코로나19 이후 비대면 문화 확산으로 인한 외식 및 숙박 이용이 줄어들었기 때문입니다.  
음식 및 숙박 항목은 외부요인(임금) 및 사회적 이슈에 영향을 받는 특징을 가지고 있습니다. \n
            ''')
st.markdown('따라서 음식 및 숙박은 **물가에 민감한 항목**입니다.')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

# 소비지수별 가계지출

st.markdown('##### 대상 품목')
code11
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 연도 별 소비자물가지수와 가계지출')
df_raw_11 = raw02[raw02["지출코드"] == 11]
fig = charts.linebar(df_raw_11, x='연도', y='가계지출', sy='소비자물가지수')
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 소득계층 별 물가지수와 가계지출')
temp = df_raw_11.loc[df_raw_11['소득계층'] != '전체']
temp = temp.loc[temp['가구형태'] != '전체가구']
fig = charts.multiLineGroup(temp, x='소비자물가지수', y='가계지출', color='소득계층', fcol='가구형태')
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 각 소득계층의 연도 별 가계지출')
temp = df_raw_11.loc[df_raw_11['소득계층'] != '전체']
temp = temp.loc[temp['가구형태'] != '전체가구']
fig = charts.scatterGroup(temp, x='연도',y='가계지출',color='소득계층',fcol='소득계층',size='가계지출', height=650)
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')


st.markdown('##### 각 소득계층의 연도 별 가계지출')
temp = df_raw_11[(df_raw_11["소득계층"]!="전체")&(df_raw_11["가구형태"]!="전체가구")]
fig = charts.histogram(temp, x='소비자물가지수', y='가계지출', color='가구형태')
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 각 소득계층의 연도 별 가계지출')
temp = df_raw_11.loc[df_raw_11['소득계층'] != '전체']
temp = temp.loc[temp['가구형태'] != '전체가구']
fig = charts.scatterGroup(temp, x='연도',y='가계지출',color='가구형태',fcol='소득계층',size='가계지출', height=650)
fig
st.markdown('')
st.markdown('')
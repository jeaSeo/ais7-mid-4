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
   page_title="[지출코드 1] 식료품 및 비주류음료 - 으4으4",
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
code1 = pd.read_csv('data/out/code1.csv')


st.markdown('# 지출코드 1 - 식료품 및 비주류음료')
st.markdown('''
            **분석1.** 2012~2016 물가 상승으로 인해 식료품 등의 필수 품목의 실질 지출이 감소했습니다.  \n
            **분석2.** 2017년 조류인플루엔자 및 계란 파동, 오징어 어획량 감소의 원인에 따른 주 식료품 가격 인상으로 가계지출이 급증했습니다.  \n
            **분석3.** 2019년부터 역대급 폭염 및 기록적인 폭우로 출하량등이 감소하여 물가가 급증해 전체적으로 가격이 인상되었으며, 그만큼 가계지출이 증가했습니다.  
            ''')
st.markdown('따라서 식료품 및 비주류음료는 **물가에 민감한 항목**입니다.')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

# 소비지수별 가계지출

# 지출코드1
st.markdown('##### 대상 품목')
code1
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 연도 별 소비자물가지수와 가계지출')
df_raw_1  = raw02[raw02["지출코드"] == 1]
fig = charts.linebar(df_raw_1, x='연도', y='가계지출', sy='소비자물가지수')
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 각 소득계층의 연도 별 가계지출')
temp = df_raw_1.loc[df_raw_1['소득계층'] != '전체']
temp = temp.loc[temp['가구형태'] != '전체가구']
fig = charts.scatterGroup(temp, x='연도',y='가계지출',color='가구형태',fcol='소득계층',size='가계지출', height=650)
fig
st.markdown('''
식료품 부문에서 근로자가구보다 근로자외가구에서 소비지출이 더 크게 나타납니다.  \n
이는 근로자 가구의 경우 1인가구 증가(배달, 밀키트 등의 간편식 소비 증가) 및 "회사"에서의 식사해결 등의 이유로 비교적 낮으며, 근로자외 가구는 자영업자가 포함되어 있기때문에 식료품 소비자출이 클것으로 예상할 수 있습니다. 
            ''')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 소득계층 별 각 가구형태의 소비자물가와 가계지출')
temp = df_raw_1.loc[df_raw_1['소득계층'] != '전체']
temp = temp.loc[temp['가구형태'] != '전체가구']
fig = charts.histoGroup(temp, x='소비자물가지수',y='가계지출',color='가구형태',fcol='소득계층')
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 각 가구형태의 소비자물가지수 별 가계지출')
temp = df_raw_1.loc[df_raw_1['소득계층'] != '전체']
temp = temp.loc[temp['가구형태'] != '전체가구']
fig = charts.multiLineGroup(temp, x='소비자물가지수', y='가계지출', color='소득계층', fcol='가구형태')
fig
st.markdown(' ')
st.markdown(' ')
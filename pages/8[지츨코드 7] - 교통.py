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
   page_title="[지출코드 7] 교통 - 으4으4",
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
code7 = pd.read_csv('data/out/code7.csv')


st.markdown('# 지출코드 7 - 교통')
st.markdown('''
            **분석1.** 2014년도 이후로 물가지수와 가계지출의 추이가 비슷한 형태를 보이고 있습니다.  \n
            **분석2.** 2014 ~ 2016년도에 물가지수가 급락한 이유는 유가가 급락하던 시기이기 때문에 국제유가의 영향을 받은 것으로 보입니다.  \n
            교통 항목은 유가지수와 물가지수가 동일한 추이를 가지고 있으며, 물가지수 상승 시 소비도 증가한다는 점에서 물가가 상승하여도 소비를 줄이지 않는 특성을 보입니다. 
            ''')
st.markdown('따라서 교통은 **물가에 민감하지 않은 항목**입니다.')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

# 소비지수별 가계지출

st.markdown('##### 대상 품목')
code7
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 연도 별 소비자물가지수와 가계지출')
df_raw_7 = raw02[raw02["지출코드"] == 7]
fig = charts.linebar(df_raw_7, x='연도', y='가계지출', sy='소비자물가지수')
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown(' ')
st.markdown('##### [첨고지표] 월간 유가지수(Dubai Crude)')
# 두바이유 (Dubai Crude), monthly
df_du = pd.read_csv('data/out/df_du.csv')
# df_du.columns = [' Dubai Crude']
fig = px.line(df_du, x='DATE', y=' Dubai Crude')
fig.update_layout(
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="bottom", y=-0.2, # y축 방향 위치 설정
        xanchor="left", x=0.28, # x축 방향 위치 설정
	)
    , margin=dict(l=0, r=0, t=10, b=20)
    # , paper_bgcolor="LightSteelBlue"
    , plot_bgcolor='#fff'
).update_xaxes(showgrid=True
               , gridwidth=1
               , gridcolor='#f0f0f0'
               , title_text="연도"
).update_yaxes(
                showgrid=True
               , gridwidth=1
               , gridcolor='#f0f0f0'
)
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 가구형태로 본 소득계층 별 소비자물가와 가계지출')
raw_df_7 = raw02[raw02["지출코드"] == 7]
temp = raw_df_7.loc[raw_df_7['소득계층'] != '전체']
temp = temp.loc[temp['가구형태'] != '전체가구']
fig = charts.scatterGroup(temp, x='소비자물가지수',y='가계지출',color='가구형태',fcol='소득계층',size='가계지출', facet_col_wrap=4, height=650)
fig
st.markdown(' ')
st.markdown(' ')
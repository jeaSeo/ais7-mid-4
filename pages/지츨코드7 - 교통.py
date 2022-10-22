import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
import koreanize_matplotlib

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import pandas_datareader as pdr

# page setting
st.set_page_config(layout="wide")

@st.cache
def load_data(url):
    return pd.read_csv(url)
url1 = "data/out/raw01.csv"
url2 = "data/out/raw02.csv"
raw01 = load_data(url1)
raw02 = load_data(url2)
code7 = load_data('data/out/code7.csv')


st.markdown('# 지출목적별 가계지출')
st.markdown(' ')

# 소비지수별 가계지출

# 지출코드 7
st.markdown('#### [지출코드 7] 교통')
st.markdown('##### 대상 품목')
code7
st.markdown(' ')
st.markdown('##### 연도별 소비자물가지수와 가계지출')
df_raw_7 = raw02[raw02["지출코드"] == 7]
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(x = df_raw_7["연도"], y = df_raw_7["가계지출"]
            ,name = "연도별 가계지출", width = 0.6, marker = dict(color = "#e6e8ef")),
            secondary_y = False)

fig.add_trace(
    go.Scatter(mode = 'lines+markers+text'
               , x= df_raw_7["연도"], y = df_raw_7["소비자물가지수"]
               , name = "연도별 소비자물가지수", marker = dict(color = "#1c5bff")), secondary_y = True
)

fig.update_layout(
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="bottom", y=-0.2, # y축 방향 위치 설정
        xanchor="left", x=0.28, # x축 방향 위치 설정
	)
    , margin=dict(l=10, r=0, t=10, b=20)
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

st.markdown('##### [첨고지표] 월간 유가지수(Dubai Crude)')
# 두바이유 (Dubai Crude), monthly
df_du = pdr.DataReader('POILDUBUSDM', 'fred', start='2012-01-01')
df_du.columns = [' Dubai Crude']
fig = px.line(df_du)
fig.update_layout(
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="bottom", y=-0.2, # y축 방향 위치 설정
        xanchor="left", x=0.28, # x축 방향 위치 설정
	)
    , margin=dict(l=10, r=0, t=10, b=20)
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

raw_df_7 = raw02[raw02["지출코드"] == 7]
temp = raw_df_7.loc[raw_df_7['소득계층'] != '전체']
temp = temp.loc[temp['가구형태'] != '전체가구']
chart7 = px.scatter(temp, x = "소비자물가지수", y = "가계지출", color = "가구형태", facet_col = "소득계층"
            ,  size = "가계지출",log_x = True, width=1500, height = 650)
chart7
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')


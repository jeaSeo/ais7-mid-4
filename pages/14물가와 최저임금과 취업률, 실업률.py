import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
import koreanize_matplotlib

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# page setting
st.set_page_config(layout="wide")

@st.cache
def load_data(url):
    return pd.read_csv(url)
url3 = "data/in/raw03.csv"
url4 = "data/in/raw04.csv"
raw03 = load_data(url3)
# raw04 = load_data(url4)


st.markdown('# 물가상승률과 취업률')
st.markdown(' ')

# 소비지수별 가계지출
# 지출코드1
st.markdown('#### 전년대비 물가상승률과 연도별 고용률')
st.markdown('설명설명')
fig1 = make_subplots(specs=[[{"secondary_y": True}]])

fig1.add_trace(
    go.Scatter(mode = 'lines+markers+text'
               , x= raw03["시점"], y = raw03["전년대비 물가상승률"]
               , name = "전년대비 물가상승률(%)", marker = dict(color = "#ccc")), secondary_y = False)

fig1.add_trace(
    go.Scatter(mode = 'lines+markers+text'
               , x= raw03["시점"], y = raw03["고용률 (%)"]
               , name = "연도별 고용률(%)", marker = dict(color = "#204AB7")), secondary_y = True)

fig1.update_layout(
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="top", y=1.15, # y축 방향 위치 설정
        xanchor="right", x=1, # x축 방향 위치 설정
	)
    , margin=dict(l=20, r=0, t=10, b=20)
    # , paper_bgcolor="LightSteelBlue"
    , plot_bgcolor='#fff'
).update_xaxes(
    showgrid=True
    , gridwidth=1
    , gridcolor='#f0f0f0'
    , title_text="연도"
).update_yaxes(
    showgrid=True
    , gridwidth=1
    , gridcolor='#f0f0f0'
    , title_text='전년대비 물가상승률(%)'
).update_yaxes(
    secondary_y = True
    , title_text='연도별 고용률(%)'
)
fig1
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

# 물가상승률과 실업률 비교
st.markdown('#### 물가상승률과 실업률 비교')
st.markdown('설명설명')
fig1 = make_subplots(specs=[[{"secondary_y": True}]])


fig1.add_trace(
    go.Scatter(mode = 'lines+markers+text'
               , x= raw03["시점"], y = raw03["전년대비 물가상승률"]
               , name = "전년대비 물가상승률(%)", marker = dict(color = "#ccc")), secondary_y = False)

fig1.add_trace(
    go.Scatter(mode = 'lines+markers+text'
               , x= raw03["시점"], y = raw03["실업률 (%)"]
               , name = "연도별 실업률(%)", marker = dict(color = "#213569")), secondary_y = True)
fig1.update_layout(
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="top", y=1.15, # y축 방향 위치 설정
        xanchor="right", x=1, # x축 방향 위치 설정
	)
    , margin=dict(l=20, r=0, t=10, b=20)
    # , paper_bgcolor="LightSteelBlue"
    , plot_bgcolor='#fff'
).update_xaxes(
    showgrid=True
    , gridwidth=1
    , gridcolor='#f0f0f0'
    , title_text="연도"
).update_yaxes(
    showgrid=True
    , gridwidth=1
    , gridcolor='#f0f0f0'
    , title_text='전년대비 물가상승률(%)'
).update_yaxes(
    secondary_y = True
    , title_text='연도별 실업률(%)'
)
fig1
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

# 물가상승률과 실업률 비교
st.markdown('#### 연도별 물가상승률과 취업률 및 실업률')
st.markdown('설명설명')
# 정규화 과정
df_num = raw03[["실업률 (%)", "고용률 (%)"]]
df_std = (df_num - df_num.mean())/df_num.std()
df_std.insert(0, "시점", raw03["시점"])
df_std["전년대비 물가상승률"] = raw03["전년대비 물가상승률"]

# 연도별 물가상승률과 취업률 및 실업률
fig15 = make_subplots(specs=[[{"secondary_y": True}]])

fig15.add_trace(
    go.Scatter(mode = 'lines+markers+text', x= df_std["시점"], y = df_std["전년대비 물가상승률"], 
           name = "전년대비 물가상승률", marker = dict(color = "#ccc")), secondary_y = False
)

# 고용률(정규화)
fig15.add_trace(
    go.Scatter(mode = 'lines+markers+text', x = df_std["시점"], y = df_std["고용률 (%)"]
           , name = "취업률", marker = dict(color = "#204AB7")),
            secondary_y = True)

# 실업률(정규화)
fig15.add_trace(
    go.Scatter(mode = 'lines+markers+text', x = df_std["시점"], y = df_std["실업률 (%)"]
           , name = "실업률", marker = dict(color = "#213569")),
            secondary_y = True)

fig15.update_layout(
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="top", y=1.15, # y축 방향 위치 설정
        xanchor="right", x=1, # x축 방향 위치 설정
	)
    , margin=dict(l=20, r=0, t=10, b=20)
    # , paper_bgcolor="LightSteelBlue"
    , plot_bgcolor='#fff'
).update_xaxes(
    showgrid=True
    , gridwidth=1
    , gridcolor='#f0f0f0'
    , title_text="연도"
).update_yaxes(
    showgrid=True
    , gridwidth=1
    , gridcolor='#f0f0f0'
    , title_text="전년대비 물가상승률"
    , secondary_y=False
).update_yaxes(
    title_text="취업률 및 고용률(%)"
    , secondary_y=True
)
fig15
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
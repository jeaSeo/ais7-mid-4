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
url1 = "data/out/raw01.csv"
url2 = "data/out/raw02.csv"
raw01 = load_data(url1)
raw02 = load_data(url2)
code11 = pd.read_csv('data/out/code11.csv')


st.markdown('# 지출코드 11 - 음식 및 숙박')
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

st.markdown('##### 연도별 소비자물가지수와 가계지출')
df_raw_11 = raw02[raw02["지출코드"] == 11]
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(x = df_raw_11["연도"], y = df_raw_11["가계지출"]
            ,name = "연도별 가계지출", width = 0.6, marker = dict(color = "#e6e8ef")),
            secondary_y = False)

fig.add_trace(
    go.Scatter(mode = 'lines+markers+text'
               , x= df_raw_11["연도"], y = df_raw_11["소비자물가지수"]
               , name = "연도별 소비자물가지수", marker = dict(color = "#8446db")), secondary_y = True
)

fig.update_layout(
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="top", y=1.11, # y축 방향 위치 설정
        xanchor="right", x=1, # x축 방향 위치 설정
	)
    , margin=dict(l=0, r=0, t=80, b=20)
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
    , title_text='가계지출'
).update_yaxes(
    secondary_y = True
    , title_text='소비자물가지수'
)
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

st.markdown('##### 소득계층별 물가지수와 가계지출')
fig = px.line(df_raw_11[(df_raw_11["가구형태"] != "전체가구") & (df_raw_11["소득계층"] != "전체")]
        , x = "소비자물가지수", y = "가계지출", color = "소득계층", facet_col = "가구형태", markers = True, width=1000, height=400)
fig.update_layout(
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="top", y=1.25, # y축 방향 위치 설정
        xanchor="right", x=1, # x축 방향 위치 설정
	)
    , margin=dict(l=0, r=0, t=105, b=20)
    # , paper_bgcolor="LightSteelBlue"
    # , plot_bgcolor='#fff'
).update_xaxes(showgrid=True
               , gridwidth=1
            #    , gridcolor='#f0f0f0'
               , title_text="소비자물가지수"
).update_yaxes(
                showgrid=True
               , gridwidth=1
            #    , gridcolor='#f0f0f0'
)
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 각 소득계층의 연도별 가계지출')
temp = df_raw_11.loc[df_raw_11['소득계층'] != '전체']
temp = temp.loc[temp['가구형태'] != '전체가구']
fig1 = px.scatter(temp,
           x="연도", y="가계지출", color="소득계층", facet_col="소득계층", size="가계지출", log_x=True)

fig1.update_layout(
    width=1000
    , height=650
	, legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="top", y=1.11, # y축 방향 위치 설정
        xanchor="right", x=1, # x축 방향 위치 설정
	)
    , margin=dict(l=0, r=0, t=90, b=20)
    # , paper_bgcolor="LightSteelBlue"
    # , plot_bgcolor='#fff'
).update_xaxes(showgrid=True
               , gridwidth=1
            #    , gridcolor='#f0f0f0'
               , title_text="연도"
).update_yaxes(
                showgrid=True
               , gridwidth=1
            #    , gridcolor='#f0f0f0'
            #    , title_text="가계지출"
)
fig1
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')


st.markdown('##### 각 소득계층의 연도별 가계지출')
fig = px.histogram(df_raw_11[(df_raw_11["소득계층"]!="전체")&(df_raw_11["가구형태"]!="전체가구")], x="소비자물가지수", y="가계지출", 
             histfunc='avg',color="가구형태", barmode='group',
            title="<b>음식 및 숙박 - 가구형태별 소비자물가지수에 따른 가계지출</b>")
fig.update_layout(
    # width=1000
    # , height=650
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="top", y=1.11, # y축 방향 위치 설정
        xanchor="right", x=1, # x축 방향 위치 설정
	)
    , margin=dict(l=0, r=0, t=90, b=20)
    # , paper_bgcolor="LightSteelBlue"
    # , plot_bgcolor='#fff'
).update_xaxes(showgrid=True
               , gridwidth=1
            #    , gridcolor='#f0f0f0'
               , title_text="연도"
).update_yaxes(
                showgrid=True
               , gridwidth=1
            #    , gridcolor='#f0f0f0'
            #    , title_text="가계지출"
)
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 각 소득계층의 연도별 가계지출')
temp = df_raw_11.loc[df_raw_11['소득계층'] != '전체']
temp = temp.loc[temp['가구형태'] != '전체가구']
fig1 = px.scatter(temp,
           x="연도", y="가계지출", color="가구형태", facet_col="소득계층", size="가계지출", log_x=True)

fig1.update_layout(
    width=1000
    , height=650
	, legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="top", y=1.11, # y축 방향 위치 설정
        xanchor="right", x=1, # x축 방향 위치 설정
	)
    , margin=dict(l=0, r=0, t=90, b=20)
    # , paper_bgcolor="LightSteelBlue"
    # , plot_bgcolor='#fff'
).update_xaxes(showgrid=True
               , gridwidth=1
            #    , gridcolor='#f0f0f0'
               , title_text="연도"
).update_yaxes(
                showgrid=True
               , gridwidth=1
            #    , gridcolor='#f0f0f0'
            #    , title_text="가계지출"
)
fig1

st.markdown('- 결론1. 2017년 본 품목에 대한 소비자 물가지수의 상승에따른 가계지출이 전년대비 상대적으로 크게 증가했다')
st.markdown('    - 물가상승의 이유: 외식과 호텔숙박료 등이 올라  전년 대비 2.7% 상승하면서 전체 물가 1.5% 상승하는 데 0.36%p 기여하여 가장 큰 영향을 미침')
st.markdown('    - 음식·숙박, 교통, 가사서비스 등은 최저임금 인상의 영향을 많이 받는 업종으로 꼽힌다.')
st.markdown('    - 한편 2018년 음식·숙박 물가가 3.0% 오르면서 2011년(4.3%) 후 상승폭이 가장 컸다. ')
st.markdown('    - 정리: 2017년부터 최저임금에 대한 이슈가 있었음 > 음식 및 숙박, 교통, 가사 서비스등의 물가는 최저임금의 영향을 많이 받는 업종임 > 이로인한 물가 상승이 있었으나, 2017년 소득계층별 지출 역시 함께 증가하여 민감성이 덜하다고 볼 수 있음. 하지만 2018년 최저임금 인상으로 소비자물가지수가 증가하였으나 꾸준히 하락세를 보이며 물가지수에 민감한 반응을 보임')
st.markdown('- 결론2. 가구형태로 볼 때 근로자 가구가 비근로자가구에 비해 물가상승에 덜 민감하게 반응한다.')
st.markdown('- 결론3. 대부분의 소득계층에서 소비자물가지수가 상승함에 따라 가계지출은 2017년에 정점을 찍고 감소추세를 보인다. 즉 2017년 이후로 소비자물가지수에 민감하게 반응한다고 볼 수 있다.')
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
code2 = pd.read_csv('data/out/code2.csv')


st.markdown('# 지출코드 2 - 주류 및 담배')
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

st.markdown('##### 연도별 소비자물가지수와 가계지출')
df_raw_2 = raw02[raw02["지출코드"] == 2]
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(x = df_raw_2["연도"], y = df_raw_2["가계지출"]
            ,name = "연도별 가계지출", width = 0.6, marker = dict(color = "#e6e8ef")),
            secondary_y = False)

fig.add_trace(
    go.Scatter(mode = 'lines+markers+text'
               , x= df_raw_2["연도"], y = df_raw_2["소비자물가지수"]
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

st.markdown('##### 각 소득계층의 연도별 가계지출')
temp = df_raw_2.loc[df_raw_2['소득계층'] != '전체']
temp = temp.loc[temp['가구형태'] != '전체가구']
fig1 = px.scatter(temp,
           x="연도", y="가계지출", color="가구형태", facet_col="소득계층", size="가계지출", width=1000, height=650, log_x=True)

fig1.update_layout(
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
               , title_text="가계지출"
)
fig1
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 소득계층별 물가지수와 가계지출')
fig = px.line(df_raw_2[(df_raw_2["가구형태"] != "전체가구") & (df_raw_2["소득계층"] != "전체")]
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

st.markdown('##### 소득계층별 소비자물가지수에 따른 가계지출')
fig = px.scatter(df_raw_2[(df_raw_2["가구형태"] == "전체가구") & (df_raw_2["소득계층"] != "전체")], x = "소비자물가지수", y = "가계지출", color = "소득계층"
           ,size = "가계지출",log_x = True, width=1000, height= 400)
fig.update_layout(
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="top", y=1.18, # y축 방향 위치 설정
        xanchor="right", x=1, # x축 방향 위치 설정
	)
    , margin=dict(l=0, r=0, t=90, b=20)
).update_xaxes(showgrid=True
               , gridwidth=1
               , title_text="소비자물가지수"
).update_yaxes(
                showgrid=True
               , gridwidth=1
)
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
fig1 = px.histogram(temp, x = "소비자물가지수", y = "가계지출", color = "가구형태", facet_col = "소득계층", histfunc='avg'
            , barmode = "group", facet_col_wrap=4)
fig1.update_layout(
    width= 1000,
    height= 400,
    legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="top", y=1.25, # y축 방향 위치 설정
        xanchor="right", x=1, # x축 방향 위치 설정
	)
    , margin=dict(l=0, r=0, t=105, b=20)
    # , paper_bgcolor="LightSteelBlue"
    # , plot_bgcolor='#fff'
).update_xaxes(
            showgrid=True
               , gridwidth=1
            #    , gridcolor='#f0f0f0'
            #    , title_text="소비자물가지수"
).update_yaxes(
                showgrid=True
               , gridwidth=1
            #    , gridcolor='#f0f0f0'
            #    , title_text="가계지출"
)
fig1
st.markdown('- 최종결론: 가격에 크게 영향을 받지 않는 항목이다. (단, 물가가 일정량 이상 상승하면 영향을 받는 항목이다.)')
st.markdown('  - 전반적으로 물가지수(라인)와 가계지출(막대)의 증감 추이가 비슷한 흐름을 가지고 있는 것으로 보인다.')
st.markdown('- 정부정책에 따라 2014년~2015년 물가지수가 급등하였으며, 2014년 ~ 2015년의 경우 지수가 증가한 정도보다 지출금액이 증가한 정도가 적어보여 가격 인상으로 인해 어느정도 소비량이 줄은 것으로 보인다.')
st.markdown('  -  2019년에도 지수가 상승하였음에도 지출이 다소 감소하였다.')
st.markdown('  - 이는 가격에 크게 영향을 받지는 않으나, 물가가 일정 수준 이상으로 급등하면 영향을 받는 항목으로 보여진다.')
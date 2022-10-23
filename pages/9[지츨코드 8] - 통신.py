import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
import koreanize_matplotlib

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# page setting
st.set_page_config(
   page_title="[지출코드 8] 통신 - 으4으4",
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
code8 = pd.read_csv('data/out/code8.csv')


st.markdown('# 지출코드 8 - 통신')
st.markdown('''
            **분석1.** 2012 ~ 2017년도의 물가와 가계지출은 일정하게 유지되고 있다.  
            이는 매달 고정비용으로 나가는 품목이기 때문에 물가와 지출이 변동없이 일정 값으로 유지되고 있는 것으로 판단된다.  \n
            **분석2.** 2017년도 이후물가지수와 지출금액 추이가 비슷한 흐름을 가지고 있다.  
            이는 최근 5G 사용자 수가 증가한 반면, 해당 품목의 물가지수 선정 품목에 5G 통신 요금제가 포함되어있지 않기 때문에 가계 지출이 감소한 것으로 보인다.  
            통신 항목은 소비할 금액을 정한 후 물가에 따라 소비량을 조정해가며 지출한다는 특징이 있다.  \n
            ''')
st.markdown('따라서 통신은 **물가에 민감한 항목**이다.')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

# 소비지수별 가계지출

st.markdown('##### 대상 품목')
code8
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 연도별 소비자물가지수와 가계지출')
df_raw_8 = raw02[raw02["지출코드"] == 8]
fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(
    go.Bar(x = df_raw_8["연도"], y = df_raw_8["가계지출"]
            ,name = "연도별 가계지출", width = 0.6, marker = dict(color = "#e6e8ef")),
            secondary_y = False)

fig.add_trace(
    go.Scatter(mode = 'lines+markers+text'
               , x= df_raw_8["연도"], y = df_raw_8["소비자물가지수"]
               , name = "연도별 소비자물가지수", marker = dict(color = "#8446db")), secondary_y = True
)
fig.update_layout(
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="top", y=1.18, # y축 방향 위치 설정
        xanchor="right", x=1, # x축 방향 위치 설정
	)
    , margin=dict(l=0, r=0, t=90, b=20)
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

st.markdown('##### 소득계층별 소비자물가지수에 따른 가계지출')
fig = px.scatter(df_raw_8[(df_raw_8["가구형태"] == "전체가구") & (df_raw_8["소득계층"] != "전체")], x = "소비자물가지수", y = "가계지출", color = "소득계층"
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

st.markdown('##### 가구형태별 소비자물가지수에 따른 가계지출')
fig = px.scatter(df_raw_8[(df_raw_8["가구형태"] != "전체가구") & (df_raw_8["소득계층"] == "전체")], x = "소비자물가지수", y = "가계지출", color = "가구형태"
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

st.markdown('##### 가구형태별 소득계층별 소비자물가지수에 따른 가계지출')
fig = px.scatter(df_raw_8[(df_raw_8["가구형태"] != "전체가구") & (df_raw_8["소득계층"].isin(["100~200만원 미만", "200~300만원 미만", "300~400만원 미만", "400~500만원 미만"]))]
           , x = "소비자물가지수", y = "가계지출", color = "가구형태", facet_col = "소득계층" 
           ,size = "가계지출",log_x = True)
fig.update_layout(
    width=1000
    , height=400
	, legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="top", y=1.23, # y축 방향 위치 설정
        xanchor="right", x=1, # x축 방향 위치 설정
	)
    , margin=dict(l=0, r=0, t=105, b=20)
    # , paper_bgcolor="LightSteelBlue"
    # , plot_bgcolor='#fff'
).update_xaxes(showgrid=True
               , gridwidth=1
               , title_text="소비자물가지수"
).update_yaxes(
                showgrid=True
               , gridwidth=1
)
fig
st.markdown('')
st.markdown('')
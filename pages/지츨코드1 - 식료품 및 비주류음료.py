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
code1 = pd.read_csv('data/out/code1.csv')


st.markdown('# 지출목적별 가계지출')
st.markdown(' ')

# 소비지수별 가계지출

# 지출코드1
st.markdown('#### [지출코드 1] 식료품 및 비주류음료')
st.markdown('##### 대상 품목')
code1
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 연도별 소비자물가지수와 가계지출')
df_raw_1  = raw02[raw02["지출코드"] == 1]
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(x = df_raw_1["연도"], y = df_raw_1["가계지출"]
           , name = "연도별 가계지출", width = 0.4, marker = dict(color = "#e6e8ef")),
            secondary_y = False)

fig.add_trace(
    go.Scatter(mode = 'lines+markers+text'
               , x= df_raw_1["연도"], y = df_raw_1["소비자물가지수"]
               , name = "연도별 소비자물가지수", marker = dict(color = "#1c5bff")), secondary_y = True
)

fig.update_layout(
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="bottom", y=1.04, # y축 방향 위치 설정
        xanchor="left", x=0.28, # x축 방향 위치 설정
	)
    , margin=dict(l=20, r=0, t=10, b=20)
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
            #    , title_text="소비자물가지수"
)
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 소비자물가와 가구형태와 소득계층')
temp = df_raw_1.loc[df_raw_1['소득계층'] != '전체']
temp = temp.loc[temp['가구형태'] != '전체가구']
fig1 = px.scatter(temp,
           x="연도", y="가계지출", color="가구형태", facet_col="소득계층", size="가계지출", width=1500, height=650, log_x=True)

fig1.update_layout(
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="bottom", y=1.04, # y축 방향 위치 설정
        xanchor="left", x=0.28, # x축 방향 위치 설정
	)
    , margin=dict(l=20, r=0, t=10, b=20)
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
               , title_text="소비자물가지수"
)
fig1
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
# fig1 = px.histogram(temp, x = "소비자물가지수", y = "가계지출", color = "가구형태", facet_col = "소득계층", histfunc='avg', 
#              , barmode = "group", width=1500, height = 400)
fig1 = px.histogram(temp, x = "소비자물가지수", y = "가계지출", color = "가구형태", facet_col = "소득계층", histfunc='avg'
            , facet_col_wrap = 4
             , barmode = "group")
fig1.update_layout(
    width= 1300,
    height= 600,
    grid_xgap= 0.2,
    legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="bottom", y=1.04, # y축 방향 위치 설정
        xanchor="left", x=0.28, # x축 방향 위치 설정
	)
    , margin=dict(l=20, r=0, t=10, b=20)
    # , paper_bgcolor="LightSteelBlue"
    # , plot_bgcolor='#fff'
).update_xaxes(
            showgrid=True
               , gridwidth=1
            #    , gridcolor='#f0f0f0'
               , title_text="소비자물가지수"
).update_yaxes(
                showgrid=True
               , gridwidth=1
            #    , gridcolor='#f0f0f0'
               , title_text="가계지출"
)
# raw02_total2 = raw02[(raw02["가구형태"]!="전체가구")]
code1_temp1 = pd.read_csv('data/out/code1_temp1.csv') # 근로자
code1_temp2 = pd.read_csv('data/out/code1_temp2.csv') # 근로자외
fig = make_subplots(rows=2, cols=4, horizontal_spacing= 0.03, vertical_spacing= 0.12)
fig.add_trace(go.Histogram(x=code1_temp1[code1_temp1["소득계층"] == '100만원 미만']["소비자물가지수"],
                         y=code1_temp1[code1_temp1["소득계층"] == '100만원 미만']["가계지출"],
             name='100만원 미만'), row=1, col=1)
fig.add_trace(go.Histogram(x=code1_temp2[code1_temp2["소득계층"] == '100만원 미만']["소비자물가지수"],
                         y=code1_temp2[code1_temp2["소득계층"] == '100만원 미만']["가계지출"],
             name='100만원 미만'), row=1, col=1)
fig.add_trace(go.Histogram(x=code1_temp1[code1_temp1["가구형태"] == '근로자가구']["소비자물가지수"],
                         y=code1_temp1[code1_temp1["소득계층"] == '100~200만원 미만']["가계지출"],
             name='100만원 이상 200만원 미만', xbins=dict(size=0.5)), row=1, col=2)
fig.add_trace(go.Histogram(x=code1_temp2[code1_temp2["가구형태"] == '근로자가구']["소비자물가지수"],
                         y=code1_temp2[code1_temp2["소득계층"] == '100~200만원 미만']["가계지출"],
             name='100만원 이상 200만원 미만', xbins=dict(size=0.5)), row=1, col=2)
# fig.add_trace(go.Histogram(x=raw02_total2[raw02_total2["소득계층"] == '100~200만원 미만']["소비자물가지수"],
#                          y=raw02_total2[raw02_total2["소득계층"] == '100~200만원 미만']["가계지출"],
#              name='10만원 이상 200만원 미만'), row=1, col=2)
# fig.add_trace(go.Histogram(x=raw02_total2[raw02_total2["소득계층"] == '200~300만원 미만']["소비자물가지수"],
#                          y=raw02_total2[raw02_total2["소득계층"] == '200~300만원 미만']["가계지출"],
#              name='200만원 이상 300만원 미만'), row=1, col=3)
# fig.add_trace(go.Histogram(x=raw02_total2[raw02_total2["소득계층"] == '300~400만원 미만']["소비자물가지수"],
#                          y=raw02_total2[raw02_total2["소득계층"] == '300~400만원 미만']["가계지출"],
#              name='300만원 이상 400만원 미만'), row=1, col=4)
# fig.add_trace(go.Histogram(x=raw02_total2[raw02_total2["소득계층"] == '400~500만원 미만']["소비자물가지수"],
#                          y=raw02_total2[raw02_total2["소득계층"] == '400~500만원 미만']["가계지출"],
#              name='400만원 이상 500만원 미만'), row=2, col=1)
# fig.add_trace(go.Histogram(x=raw02_total2[raw02_total2["소득계층"] == '500~600만원 미만']["소비자물가지수"],
#                          y=raw02_total2[raw02_total2["소득계층"] == '500~600만원 미만']["가계지출"],
#              name='500만원 이상 600만원 미만'), row=2, col=2)
# fig.add_trace(go.Histogram(x=raw02_total2[raw02_total2["소득계층"] == '600만원이상 ~ 700미만']["소비자물가지수"],
#                          y=raw02_total2[raw02_total2["소득계층"] == '600만원이상 ~ 700미만']["가계지출"],
#              name='600만원 이상 700만원 미만'), row=2, col=3)
fig.update_layout(
    width= 1300,
    height= 800,
    legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="bottom", y=1.04, # y축 방향 위치 설정
        xanchor="left", x=0.28, # x축 방향 위치 설정
	)
    , margin=dict(l=20, r=0, t=10, b=20)
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
               , title_text="가계지출"
)
# fig
fig1
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 소비자물가와 가구형태와 소득계층')
temp = df_raw_1.loc[df_raw_1['소득계층'] != '전체']
temp = temp.loc[temp['가구형태'] != '전체가구']
fig = px.line(temp, x = "소비자물가지수", y = "가계지출", color = "소득계층", facet_col = "가구형태", markers = True, width=1200, height= 400)
fig.update_layout(
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="bottom", y=1.04, # y축 방향 위치 설정
        xanchor="left", x=0.28, # x축 방향 위치 설정
	)
    , margin=dict(l=20, r=0, t=10, b=20)
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
               , title_text="소비자물가지수"
)
fig
st.markdown(' ')
st.markdown(' ')

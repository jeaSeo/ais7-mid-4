import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
import koreanize_matplotlib

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.graph_objs import Line
from plotly.graph_objs.scatter.marker import Line

# page setting
st.set_page_config(layout="wide")

@st.cache
def load_data(url):
    return pd.read_csv(url)
url1 = "data/out/raw01.csv"
url2 = "data/out/raw02.csv"
raw01 = load_data(url1)
raw02 = load_data(url2)



st.markdown('# 소비지수별 가계지출')
st.markdown(' ')

# raw1
st.markdown('### 연도별 소비자 물가지수(종합)')
fig = make_subplots(specs=[[{"secondary_y": True}]])
#add_traces
fig.add_trace(
    go.Line(x=raw01[raw01["지출코드"]== 0]["연도"], y=raw01[raw01["지출코드"]== 0]["소비자물가지수"], name="소비자물가지수"),
    secondary_y=True,
)
fig.add_trace(
    go.Bar(x=raw01[raw01["지출코드"]== 0]["연도"], y=raw01[raw01["지출코드"]== 0]["소비자물가지수"], name="소비자물가지수", 
          width = 0.4, marker = dict(color = "#e6e8ef")),
    secondary_y=False,
)

fig.update_layout(
    # title_text="<b>연도별 가계지출(종합)</b>",
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="top", y=1.06, # y축 방향 위치 설정
        xanchor="left", x=0.01, # x축 방향 위치 설정
	)
    , margin=dict(l=10, r=0, t=10, b=0)
    , plot_bgcolor='#fff'
).update_xaxes(showgrid=True
               , gridwidth=1
               , gridcolor='#f0f0f0'
               , title_text="연도"
).update_yaxes(
                showgrid=True
               , gridwidth=1
               , gridcolor='#f0f0f0'
               , title_text="소비자물가지수"
               , secondary_y=True
)
fig


# 연도별 지출품목별 가계지출(종합)
st.markdown('### 연도별 지출품목별 소비자물가지수(종합)')
fig = make_subplots(rows=3, cols=4, horizontal_spacing= 0.03, vertical_spacing= 0.12, 
                   )
fig.add_trace(go.Scatter(x=raw01[raw01["지출코드"] == 1]["연도"],
                         y=raw01[raw01["지출코드"] == 1]["소비자물가지수"],
             mode='lines+markers', name='식료품 및 비주류음료'), row=1, col=1)
fig.add_trace(go.Scatter(x=raw01[raw01["지출코드"] == 2]["연도"],
                         y=raw01[raw01["지출코드"] == 2]["소비자물가지수"],
             mode='lines+markers', name='주류 및 담배'), row=1, col=2)
fig.add_trace(go.Scatter(x=raw01[raw01["지출코드"] == 3]["연도"],
                         y=raw01[raw01["지출코드"] == 3]["소비자물가지수"],
             mode='lines+markers', name='의류 및 신발'), row=1, col=3)
fig.add_trace(go.Scatter(x=raw01[raw01["지출코드"] == 4]["연도"],
                         y=raw01[raw01["지출코드"] == 4]["소비자물가지수"],
             mode='lines+markers', name='주택 수도 전기 및 연료'), row=1, col=4)
fig.add_trace(go.Scatter(x=raw01[raw01["지출코드"] == 5]["연도"],
                         y=raw01[raw01["지출코드"] == 5]["소비자물가지수"],
             mode='lines+markers', name='가정용품 및 가사 서비스'), row=2, col=1)
fig.add_trace(go.Scatter(x=raw01[raw01["지출코드"] == 6]["연도"],
                         y=raw01[raw01["지출코드"] == 6]["소비자물가지수"],
             mode='lines+markers', name='보건'), row=2, col=2)
fig.add_trace(go.Scatter(x=raw01[raw01["지출코드"] == 7]["연도"],
                         y=raw01[raw01["지출코드"] == 7]["소비자물가지수"],
             mode='lines+markers', name='교통'), row=2, col=3)
fig.add_trace(go.Scatter(x=raw01[raw01["지출코드"] == 8]["연도"],
                         y=raw01[raw01["지출코드"] == 8]["소비자물가지수"],
             mode='lines+markers', name='통신'), row=2, col=4)
fig.add_trace(go.Scatter(x=raw01[raw01["지출코드"] == 9]["연도"],
                         y=raw01[raw01["지출코드"] == 9]["소비자물가지수"],
             mode='lines+markers', name='오락 및 문화'), row=3, col=1)
fig.add_trace(go.Scatter(x=raw01[raw01["지출코드"] == 10]["연도"],
                         y=raw01[raw01["지출코드"] == 10]["소비자물가지수"],
             mode='lines+markers', name='교육'), row=3, col=2)
fig.add_trace(go.Scatter(x=raw01[raw01["지출코드"] == 11]["연도"],
                         y=raw01[raw01["지출코드"] == 11]["소비자물가지수"],
             mode='lines+markers', name='음식 및 숙박'), row=3, col=3)
fig.add_trace(go.Scatter(x=raw01[raw01["지출코드"] == 12]["연도"],
                         y=raw01[raw01["지출코드"] == 12]["소비자물가지수"],
             mode='lines+markers', name='기타 상품 및 서비스'), row=3, col=4)
# fig.update_layout(title='<b>연도별 지출품목별 가계지출(종합)</b>')

fig.update_layout(
    title_text="<b></b>",
    width= 1300,
    height= 800,
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="top", y=1.06, # y축 방향 위치 설정
        xanchor="left", x=0.01, # x축 방향 위치 설정
	)
    , margin=dict(l=20, r=0, t=10, b=0)
    # , plot_bgcolor='#fff'
).update_xaxes(showgrid=True
               , gridwidth=1
               , gridcolor='#f0f0f0'
               , title_text="연도"
).update_yaxes(
                showgrid=True
               , gridwidth=1
               , gridcolor='#f0f0f0'
            #    , title_text="<b>가계지출</b>"
               , secondary_y=True
)
fig


# 연도별 지출품목별 소비자물가지수
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown('### 연도별 가계지출(종합)')
# raw02_total = raw02[(raw02["소득계층"] == "전체")&(raw02["가구형태"]=="전체가구")&(raw02["지출코드"]==0)]
raw02_total = load_data('data/out/raw02_total.csv')

fig = make_subplots(specs=[[{"secondary_y": True}]])
#add_traces
fig.add_trace(
    go.Line(x=raw02_total["연도"], y=raw02_total["가계지출"], name="가계지출"),
    secondary_y=True,
)
fig.add_trace(
    go.Bar(x=raw02_total["연도"], y=raw02_total["가계지출"], name="가계지출", 
          width = 0.4, marker = dict(color = "#e6e8ef")),
    secondary_y=False,
)

fig.update_layout(
    # title_text="<b>연도별 가계지출(종합)</b>",
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="top", y=0.99, # y축 방향 위치 설정
        xanchor="left", x=0.01, # x축 방향 위치 설정
	)
    , margin=dict(l=10, r=0, t=10, b=0)
    , plot_bgcolor='#fff'
).update_xaxes(showgrid=True
               , gridwidth=1
               , gridcolor='#f0f0f0'
               , title_text="연도"
).update_yaxes(
                showgrid=True
               , gridwidth=1
               , gridcolor='#f0f0f0'
            #    , title_text="<b>가계지출</b>"
               , secondary_y=True
)
fig

# 연도별 지출품목별 가계지출(종합)
st.markdown(' ')
st.markdown('### 연도별 지출품목별 가계지출(종합)')
raw02_total2 = raw02[(raw02["소득계층"] == "전체")&(raw02["가구형태"]=="전체가구")]
fig = make_subplots(rows=3, cols=4, horizontal_spacing= 0.03, vertical_spacing= 0.12, 
                   )
fig.add_trace(go.Scatter(x=raw02_total2[raw02_total2["지출코드"] == 1]["연도"],
                         y=raw02_total2[raw02_total2["지출코드"] == 1]["가계지출"],
             mode='lines+markers', name='식료품 및 비주류음료'), row=1, col=1)
fig.add_trace(go.Scatter(x=raw02_total2[raw02_total2["지출코드"] == 2]["연도"],
                         y=raw02_total2[raw02_total2["지출코드"] == 2]["가계지출"],
             mode='lines+markers', name='주류 및 담배'), row=1, col=2)
fig.add_trace(go.Scatter(x=raw02_total2[raw02_total2["지출코드"] == 3]["연도"],
                         y=raw02_total2[raw02_total2["지출코드"] == 3]["가계지출"],
             mode='lines+markers', name='의류 및 신발'), row=1, col=3)
fig.add_trace(go.Scatter(x=raw02_total2[raw02_total2["지출코드"] == 4]["연도"],
                         y=raw02_total2[raw02_total2["지출코드"] == 4]["가계지출"],
             mode='lines+markers', name='주택 수도 전기 및 연료'), row=1, col=4)
fig.add_trace(go.Scatter(x=raw02_total2[raw02_total2["지출코드"] == 5]["연도"],
                         y=raw02_total2[raw02_total2["지출코드"] == 5]["가계지출"],
             mode='lines+markers', name='가정용품 및 가사 서비스'), row=2, col=1)
fig.add_trace(go.Scatter(x=raw02_total2[raw02_total2["지출코드"] == 6]["연도"],
                         y=raw02_total2[raw02_total2["지출코드"] == 6]["가계지출"],
             mode='lines+markers', name='보건'), row=2, col=2)
fig.add_trace(go.Scatter(x=raw02_total2[raw02_total2["지출코드"] == 7]["연도"],
                         y=raw02_total2[raw02_total2["지출코드"] == 7]["가계지출"],
             mode='lines+markers', name='교통'), row=2, col=3)
fig.add_trace(go.Scatter(x=raw02_total2[raw02_total2["지출코드"] == 8]["연도"],
                         y=raw02_total2[raw02_total2["지출코드"] == 8]["가계지출"],
             mode='lines+markers', name='통신'), row=2, col=4)
fig.add_trace(go.Scatter(x=raw02_total2[raw02_total2["지출코드"] == 9]["연도"],
                         y=raw02_total2[raw02_total2["지출코드"] == 9]["가계지출"],
             mode='lines+markers', name='오락 및 문화'), row=3, col=1)
fig.add_trace(go.Scatter(x=raw02_total2[raw02_total2["지출코드"] == 10]["연도"],
                         y=raw02_total2[raw02_total2["지출코드"] == 10]["가계지출"],
             mode='lines+markers', name='교육'), row=3, col=2)
fig.add_trace(go.Scatter(x=raw02_total2[raw02_total2["지출코드"] == 11]["연도"],
                         y=raw02_total2[raw02_total2["지출코드"] == 11]["가계지출"],
             mode='lines+markers', name='음식 및 숙박'), row=3, col=3)
fig.add_trace(go.Scatter(x=raw02_total2[raw02_total2["지출코드"] == 12]["연도"],
                         y=raw02_total2[raw02_total2["지출코드"] == 12]["가계지출"],
             mode='lines+markers', name='기타 상품 및 서비스'), row=3, col=4)
# fig.update_layout(title='<b>연도별 지출품목별 가계지출(종합)</b>')

fig.update_layout(
    title_text="<b></b>",
    width= 1300,
    height= 800,
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="top", y=1.06, # y축 방향 위치 설정
        xanchor="left", x=0.01, # x축 방향 위치 설정
	)
    , margin=dict(l=20, r=0, t=10, b=0)
    # , plot_bgcolor='#fff'
).update_xaxes(showgrid=True
               , gridwidth=1
               , gridcolor='#f0f0f0'
               , title_text="연도"
).update_yaxes(
                showgrid=True
               , gridwidth=1
               , gridcolor='#f0f0f0'
            #    , title_text="<b>가계지출</b>"
               , secondary_y=True
)
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

#가구형태 = 전체가구, 지출목적 = 소비지출
st.markdown('### 소득계층별 연도별 가계지출(전체)')
pv = load_data('data/out/pv.csv')
#heatmap시각화
fig = plt.figure(figsize=(15,6))
sns.heatmap(pv, annot = True, fmt=",.0f", cmap="Greens")
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

#가구형태별 연도별 가계지출(전체)
st.markdown('### 가구형태별 연도별 가계지출(전체)')
#소득계층 = 전체, 지출목적 = 소비지출
hs_he_pv = load_data('data/out/hs_he_pv.csv')
#heatmap 시각화
fig = plt.figure(figsize=(15,6))
sns.heatmap(hs_he_pv, annot = True, fmt=",.0f", cmap="Greens")
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')


# 지출목적별 연도별 가계지출(전체)
st.markdown('### 지출목적별 연도별 가계지출(전체)')
ct_he_pv = load_data('data/out/ct_he_pv.csv')
#시각화
fig = plt.figure(figsize=(15,6))
sns.heatmap(ct_he_pv, annot = True, fmt=",.0f", cmap="Greens")
fig
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


st.markdown('# 지출목적별 가계지출')
st.markdown(' ')

# 소비지수별 가계지출
# 지출코드1
st.markdown('#### [지출코드 1] 식료품 및 비주류음료')
st.markdown('설명설명')
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
st.markdown('##### 소비자물가와 가구형태와 소득계층')
temp = df_raw_1.loc[df_raw_1['소득계층'] != '전체']
temp = temp.loc[temp['가구형태'] != '전체가구']
fig = px.histogram(temp, x = "소비자물가지수", y = "가계지출", color = "가구형태", facet_col = "소득계층", histfunc='avg'
            , facet_col_wrap = 4
             , barmode = "group", width=1500, height = 400)

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
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')


# 지출코드 7
st.markdown('#### [지출코드 7] 교통')
st.markdown('설명설명')
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

import pandas_datareader as pdr
st.markdown(' ')
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

st.markdown(' ')
st.markdown('##### 소비자물가와 가구형태와 소득계층')
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
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')



# # 지출코드 8
st.markdown('#### [지출코드 8] 통신')
st.markdown('설명설명')
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

st.markdown(' ')
st.markdown('##### 소득계층별 소비자물가지수에 따른 가계지출')
fig = px.scatter(df_raw_8[(df_raw_8["가구형태"] == "전체가구") & (df_raw_8["소득계층"] != "전체")], x = "소비자물가지수", y = "가계지출", color = "소득계층"
           ,size = "가계지출",log_x = True, width=1200, height= 400)
fig.update_layout(
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="top", y=1.06, # y축 방향 위치 설정
        xanchor="left", x=0.28, # x축 방향 위치 설정
	)
    , margin=dict(l=10, r=0, t=10, b=20)
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
)
fig

st.markdown(' ')
st.markdown('##### 가구형태별 소비자물가지수에 따른 가계지출')
fig = px.scatter(df_raw_8[(df_raw_8["가구형태"] != "전체가구") & (df_raw_8["소득계층"] == "전체")], x = "소비자물가지수", y = "가계지출", color = "가구형태"
           ,size = "가계지출",log_x = True, width=1200, height= 400)
fig.update_layout(
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="top", y=1.06, # y축 방향 위치 설정
        xanchor="left", x=0.28, # x축 방향 위치 설정
	)
    , margin=dict(l=10, r=0, t=10, b=20)
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
)
fig

st.markdown(' ')
st.markdown('##### 가구형태별 소득계층별 소비자물가지수에 따른 가계지출')
fig = px.scatter(df_raw_8[(df_raw_8["가구형태"] != "전체가구") & (df_raw_8["소득계층"].isin(["100~200만원 미만", "200~300만원 미만", "300~400만원 미만", "400~500만원 미만"]))]
           , x = "소비자물가지수", y = "가계지출", color = "가구형태", facet_col = "소득계층" 
           ,size = "가계지출",log_x = True, width=1200, height=400)
fig.update_layout(
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="top", y=1.06, # y축 방향 위치 설정
        xanchor="left", x=0.28, # x축 방향 위치 설정
	)
    , margin=dict(l=10, r=0, t=10, b=20)
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

# 지출코드 11
st.markdown('#### [지출코드 11] 음식 및 숙박')
st.markdown('설명설명')
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

st.markdown(' ')
st.markdown('##### 소득계층별 물가지수와 가계지출')
fig = px.line(df_raw_11[(df_raw_11["가구형태"] != "전체가구") & (df_raw_11["소득계층"] != "전체")]
        , x = "소비자물가지수", y = "가계지출", color = "소득계층", facet_col = "가구형태", markers = True, width=1500, height=400)
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
               , title_text="소비자물가지수"
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
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

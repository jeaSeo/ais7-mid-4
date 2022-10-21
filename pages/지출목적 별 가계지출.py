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
fig = px.scatter(temp, x = "소비자물가지수", y = "가계지출", color = "가구형태", facet_col = "소득계층"
            , size = "가계지출",log_x = True, width=1500, height = 650)

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
fig = px.line(df_raw_1.loc[(df_raw_1["가구형태"] != "전체가구") & (df_raw_1["소득계층"] != "전체")]
        , x = "소비자물가지수", y = "가계지출", color = "소득계층", facet_col = "가구형태", markers = True ,width=1500, height = 650)

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




# 지출코드2
st.markdown('#### [지출코드 2] 주류 및 담배')
st.markdown('설명설명')
df_raw_2 = raw02[raw02["지출코드"] == 2]
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(x = df_raw_2["연도"], y = df_raw_2["가계지출"]
            ,name = "연도별 가계지출", width = 0.6, marker = dict(color = "#e6e8ef")),
            secondary_y = False)

fig.add_trace(
    go.Scatter(mode = 'lines+markers+text'
               , x= df_raw_2["연도"], y = df_raw_2["소비자물가지수"]
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
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')




# 지출코드3
st.markdown('#### [지출코드 3] 의류 및 신발')
st.markdown('설명설명')
df_raw_3 = raw02[raw02["지출코드"] == 3]
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(x = df_raw_3["연도"], y = df_raw_3["가계지출"]
            ,name = "연도별 가계지출", width = 0.6, marker = dict(color = "#e6e8ef")),
            secondary_y = False)

fig.add_trace(
    go.Scatter(mode = 'lines+markers+text'
               , x= df_raw_3["연도"], y = df_raw_3["소비자물가지수"]
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
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')


# 지출코드4
st.markdown('#### [지출코드 4] 주택 수도 전기 및 연료')
st.markdown('설명설명')
df_raw_4 = raw02[raw02["지출코드"] == 4]
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(x = df_raw_4["연도"], y = df_raw_4["가계지출"]
            ,name = "연도별 가계지출", width = 0.6, marker = dict(color = "#e6e8ef")),
            secondary_y = False)

fig.add_trace(
    go.Scatter(mode = 'lines+markers+text'
               , x= df_raw_4["연도"], y = df_raw_4["소비자물가지수"]
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
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')


# 지출코드5
st.markdown('#### [지출코드 5] 가정용품 및 가사 서비스')
st.markdown('설명설명')
df_raw_5 = raw02[raw02["지출코드"] == 5]
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(x = df_raw_5["연도"], y = df_raw_5["가계지출"]
           , name = "연도별 가계지출", width = 0.4, marker = dict(color = "#9298a1")),
            secondary_y = False)

fig.add_trace(
    go.Scatter(mode = 'lines+markers+text'
               , x= df_raw_5["연도"], y = df_raw_5["소비자물가지수"]
               , name = "연도별 소비자물가지수", marker = dict(color = "#305285")), secondary_y = True
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
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')


# 지출코드6
st.markdown('#### [지출코드 6] 보건')
st.markdown('설명설명')
df_raw_6 = raw02[raw02["지출코드"] == 6]
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(x = df_raw_6["연도"], y = df_raw_6["가계지출"]
            ,name = "연도별 가계지출", width = 0.6, marker = dict(color = "#e6e8ef")),
            secondary_y = False)

fig.add_trace(
    go.Scatter(mode = 'lines+markers+text'
               , x= df_raw_6["연도"], y = df_raw_6["소비자물가지수"]
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
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')


# 지출코드 7
st.markdown('#### [지출코드 7] 교통')
st.markdown('설명설명')
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



# 지출코드 8
st.markdown('#### [지출코드 8] 통신')
st.markdown('설명설명')

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
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')


# 지출코드 9
st.markdown('#### [지출코드 9] 오락 및 문화')
st.markdown('설명설명')
df_raw_9 = raw02[raw02["지출코드"] == 9]
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(x = df_raw_9["연도"], y = df_raw_9["가계지출"]
            ,name = "연도별 가계지출", width = 0.6, marker = dict(color = "#e6e8ef")),
            secondary_y = False)

fig.add_trace(
    go.Scatter(mode = 'lines+markers+text'
               , x= df_raw_9["연도"], y = df_raw_9["소비자물가지수"]
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
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')


# 지출코드 10
st.markdown('#### [지출코드 10] 교육')
st.markdown('설명설명')
df_raw_10 = raw02[raw02["지출코드"] == 10]
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(x = df_raw_10["연도"], y = df_raw_10["가계지출"]
            ,name = "연도별 가계지출", width = 0.6, marker = dict(color = "#e6e8ef")),
            secondary_y = False)

fig.add_trace(
    go.Scatter(mode = 'lines+markers+text'
               , x= df_raw_10["연도"], y = df_raw_10["소비자물가지수"]
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
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')


# 지출코드 11
st.markdown('#### [지출코드 11] 음식 및 숙박')
st.markdown('설명설명')
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
               , gridcolor='#e0e0e0'
               , title_text="연도"
).update_yaxes(
                showgrid=True
               , gridwidth=1
               , gridcolor='#e0e0e0'
)
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')


# 지출코드 12
st.markdown('#### [지출코드 12] 기타 상품 및 서비스')
st.markdown('설명설명')
df_raw_12 = raw02[raw02["지출코드"] == 12]
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(x = df_raw_12["연도"], y = df_raw_12["가계지출"]
            ,name = "연도별 가계지출", width = 0.6, marker = dict(color = "#e6e8ef")),
            secondary_y = False)

fig.add_trace(
    go.Scatter(mode = 'lines+markers+text'
               , x= df_raw_12["연도"], y = df_raw_12["소비자물가지수"]
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
).update_yaxes(
                showgrid=True
               , gridwidth=1
               , gridcolor='#f0f0f0'
               , title_text="연도"
).update_xaxes(
                showgrid=True
               , gridwidth=1
               , gridcolor='#f0f0f0'
)
fig
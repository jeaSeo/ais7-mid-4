import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
import koreanize_matplotlib

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from PIL import Image


# page setting
st.set_page_config(
   page_title="프로젝트 요약 - 으4으4",
    layout="wide"
)

@st.cache
def load_data(url):
    return pd.read_csv(url)
url1 = "data/out/raw01.csv"
url2 = "data/out/raw02.csv"
raw01 = load_data(url1)
raw02 = load_data(url2)
raw02 = pd.read_csv(url2)
code1 = pd.read_csv('data/out/code1.csv')


# raw02 = raw02.loc[raw02['소득계층'] != '전체']
# raw02 = raw02.loc[raw02['가구형태'] != '전체가구']

df_raw_1 = raw02[raw02["지출코드"] == 1]
df_raw_3 = raw02[raw02["지출코드"] == 3]
df_raw_4 = raw02[raw02["지출코드"] == 4]
df_raw_6 = raw02[raw02["지출코드"] == 6]
df_raw_7 = raw02[raw02["지출코드"] == 7]
df_raw_8 = raw02[raw02["지출코드"] == 8]
df_raw_10 = raw02[raw02["지출코드"] == 10]
df_raw_11 = raw02[raw02["지출코드"] == 11]

df_raw_2 = raw02[raw02["지출코드"] == 2]
df_raw_5 = raw02[raw02["지출코드"] == 5]
df_raw_7 = raw02[raw02["지출코드"] == 7]
df_raw_9 = raw02[raw02["지출코드"] == 9]

st.markdown('# 프로젝트 요약')
st.markdown('''
            12개의 소비자물가지수 항목과 이에 대한 각 가계지출 데이터를 분석하여 물가상승에 민감한 항목을 도출하였습니다.  
            또한 추가분석으로 물가상승률과 고용률 및 취업률의 관계를 분석해보았습니다.''')
st.markdown(' ')
image3 = Image.open('data/image3.png')
st.image(image3)
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
# raw02
st.markdown('## 물가 상승에 민감한 항목')
st.markdown(''''물가 상승에 민감한 항목' 은 분석 요소인 막대의 추이(지출) 와 선의 추이 (물가) 가 서로 반비례 관계일 때와 비례관계이지만 물가지수 변동폭이 가계지출의 변동폭 보다 클 때를 의미한다.''')
st.markdown('')
st.markdown('')
st.markdown('')
# st.markdown('---')
col1_1, col1_2= st.columns(2)
with col1_1:
    # 소비지수별 가계지출
    st.markdown('##### [지출코드 1] 식료품 및 비주류음료')
    st.markdown('##### 연도 별 소비자물가지수와 가계지출')


    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(x = df_raw_1["연도"], y = df_raw_1["가계지출"]
            , name = "연도 별 가계지출", width = 0.4, marker = dict(color = "#e6e8ef")),
                secondary_y = False)

    fig.add_trace(
        go.Scatter(mode = 'lines+markers+text'
                , x= df_raw_1["연도"], y = df_raw_1["소비자물가지수"]
                , name = "연도 별 소비자물가지수", marker = dict(color = "#8446Db")), secondary_y = True
    )

    fig.update_layout(
        width= 450
        , legend=dict(
            orientation="h", # 가로 방향으로
            yanchor="top", y=1.11, # y축 방향 위치 설정
            xanchor="right", x=1, # x축 방향 위치 설정
        )
        , margin=dict(l=10, r=0, t=80, b=20)
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
                , title_text="소비자물가지수"
                , secondary_y = True
    ).update_yaxes(
                title_text="가계지출"
                , secondary_y = False
    )
    fig
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    
    # 소비지수별 가계지출
    st.markdown('##### [지출코드 4] 주택 수도 전기 및 연료')
    st.markdown('##### 연도 별 소비자물가지수와 가계지출')


    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(x = df_raw_4["연도"], y = df_raw_4["가계지출"]
            , name = "연도 별 가계지출", width = 0.4, marker = dict(color = "#e6e8ef")),
                secondary_y = False)

    fig.add_trace(
        go.Scatter(mode = 'lines+markers+text'
                , x= df_raw_4["연도"], y = df_raw_4["소비자물가지수"]
                , name = "연도 별 소비자물가지수", marker = dict(color = "#8446Db")), secondary_y = True
    )

    fig.update_layout(
        width= 450
        ,legend=dict(
            orientation="h", # 가로 방향으로
            yanchor="top", y=1.11, # y축 방향 위치 설정
            xanchor="right", x=1, # x축 방향 위치 설정
        )
        , margin=dict(l=10, r=0, t=80, b=20)
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
                , title_text="소비자물가지수"
                , secondary_y = True
    ).update_yaxes(
                title_text="가계지출"
                , secondary_y = False
    )
    fig
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')

    # 소비지수별 가계지출
    st.markdown('##### [지출코드 8] 통신')
    st.markdown('##### 연도 별 소비자물가지수와 가계지출')


    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(x = df_raw_8["연도"], y = df_raw_8["가계지출"]
            , name = "연도 별 가계지출", width = 0.4, marker = dict(color = "#e6e8ef")),
                secondary_y = False)

    fig.add_trace(
        go.Scatter(mode = 'lines+markers+text'
                , x= df_raw_8["연도"], y = df_raw_8["소비자물가지수"]
                , name = "연도 별 소비자물가지수", marker = dict(color = "#8446Db")), secondary_y = True
    )

    fig.update_layout(
        width=450
        , legend=dict(
            orientation="h", # 가로 방향으로
            yanchor="top", y=1.11, # y축 방향 위치 설정
            xanchor="right", x=1, # x축 방향 위치 설정
        )
        , margin=dict(l=10, r=0, t=80, b=20)
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
                , title_text="소비자물가지수"
                , secondary_y = True
    ).update_yaxes(
                title_text="가계지출"
                , secondary_y = False
    )
    fig
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')



    # 소비지수별 가계지출
    st.markdown('##### [지출코드 11] 음식 및 숙박')
    st.markdown('##### 연도 별 소비자물가지수와 가계지출')


    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(x = df_raw_11["연도"], y = df_raw_11["가계지출"]
            , name = "연도 별 가계지출", width = 0.4, marker = dict(color = "#e6e8ef")),
                secondary_y = False)

    fig.add_trace(
        go.Scatter(mode = 'lines+markers+text'
                , x= df_raw_11["연도"], y = df_raw_11["소비자물가지수"]
                , name = "연도 별 소비자물가지수", marker = dict(color = "#8446Db")), secondary_y = True
    )

    fig.update_layout(
        width=450
        , legend=dict(
            orientation="h", # 가로 방향으로
            yanchor="top", y=1.11, # y축 방향 위치 설정
            xanchor="right", x=1, # x축 방향 위치 설정
        )
        , margin=dict(l=10, r=0, t=80, b=20)
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
                , title_text="소비자물가지수"
                , secondary_y = True
    ).update_yaxes(
                title_text="가계지출"
                , secondary_y = False
    )
    fig

with col1_2:
    # 소비지수별 가계지출
    st.markdown('##### [지출코드 3] 의류 및 신발')
    st.markdown('##### 연도 별 소비자물가지수와 가계지출')


    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(x = df_raw_3["연도"], y = df_raw_3["가계지출"]
            , name = "연도 별 가계지출", width = 0.4, marker = dict(color = "#e6e8ef")),
                secondary_y = False)

    fig.add_trace(
        go.Scatter(mode = 'lines+markers+text'
                , x= df_raw_3["연도"], y = df_raw_3["소비자물가지수"]
                , name = "연도 별 소비자물가지수", marker = dict(color = "#8446Db")), secondary_y = True
    )

    fig.update_layout(
        width=450
        , legend=dict(
            orientation="h", # 가로 방향으로
            yanchor="top", y=1.11, # y축 방향 위치 설정
            xanchor="right", x=1, # x축 방향 위치 설정
        )
        , margin=dict(l=10, r=0, t=80, b=20)
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
                , title_text="소비자물가지수"
                , secondary_y = True
    ).update_yaxes(
                title_text="가계지출"
                , secondary_y = False
    )
    fig
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')


    # 소비지수별 가계지출
    st.markdown('##### [지출코드 6] 보건')
    st.markdown('##### 연도 별 소비자물가지수와 가계지출')


    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(x = df_raw_6["연도"], y = df_raw_6["가계지출"]
            , name = "연도 별 가계지출", width = 0.4, marker = dict(color = "#e6e8ef")),
                secondary_y = False)

    fig.add_trace(
        go.Scatter(mode = 'lines+markers+text'
                , x= df_raw_6["연도"], y = df_raw_6["소비자물가지수"]
                , name = "연도 별 소비자물가지수", marker = dict(color = "#8446Db")), secondary_y = True
    )

    fig.update_layout(
        width=450
        , legend=dict(
            orientation="h", # 가로 방향으로
            yanchor="top", y=1.11, # y축 방향 위치 설정
            xanchor="right", x=1, # x축 방향 위치 설정
        )
        , margin=dict(l=10, r=0, t=80, b=20)
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
                , title_text="소비자물가지수"
                , secondary_y = True
    ).update_yaxes(
                title_text="가계지출"
                , secondary_y = False
    )
    fig
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    
    
    # 소비지수별 가계지출
    st.markdown('##### [지출코드 10] 교육')
    st.markdown('##### 연도 별 소비자물가지수와 가계지출')


    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(x = df_raw_10["연도"], y = df_raw_10["가계지출"]
            , name = "연도 별 가계지출", width = 0.4, marker = dict(color = "#e6e8ef")),
                secondary_y = False)

    fig.add_trace(
        go.Scatter(mode = 'lines+markers+text'
                , x= df_raw_10["연도"], y = df_raw_10["소비자물가지수"]
                , name = "연도 별 소비자물가지수", marker = dict(color = "#8446Db")), secondary_y = True
    )

    fig.update_layout(
        width= 450
        , legend=dict(
            orientation="h", # 가로 방향으로
            yanchor="top", y=1.11, # y축 방향 위치 설정
            xanchor="right", x=1, # x축 방향 위치 설정
        )
        , margin=dict(l=10, r=0, t=80, b=20)
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
                , title_text="소비자물가지수"
                , secondary_y = True
    ).update_yaxes(
                title_text="가계지출"
                , secondary_y = False
    )
    fig
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')


st.markdown('## 물가 상승에 민감하지 않은 항목')
st.markdown(''''물가 상승에 민감하지 않은 항목' 은 분석 요소인 막대의 추이(지출) 와 선의 추이(물가) 가 서로 비례관계이지만 물가지수의 변동폭이 가계지출의 변동폭보다 작은 경우와 두 변동폭이 비슷할 때의 경우를 의미한다.''')
st.markdown('')
st.markdown('')
st.markdown('')
col2_1, col2_2= st.columns(2)
with col2_1:
    # 소비지수별 가계지출
    st.markdown('##### [지출코드 2] 주류 및 담배')
    st.markdown('##### 연도 별 소비자물가지수와 가계지출')


    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(x = df_raw_2["연도"], y = df_raw_2["가계지출"]
            , name = "연도 별 가계지출", width = 0.4, marker = dict(color = "#e6e8ef")),
                secondary_y = False)

    fig.add_trace(
        go.Scatter(mode = 'lines+markers+text'
                , x= df_raw_2["연도"], y = df_raw_2["소비자물가지수"]
                , name = "연도 별 소비자물가지수", marker = dict(color = "#8446Db")), secondary_y = True
    )

    fig.update_layout(
        width= 450
        , legend=dict(
            orientation="h", # 가로 방향으로
            yanchor="top", y=1.11, # y축 방향 위치 설정
            xanchor="right", x=1, # x축 방향 위치 설정
        )
        , margin=dict(l=10, r=0, t=80, b=20)
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
                , title_text="소비자물가지수"
                , secondary_y = True
    ).update_yaxes(
                title_text="가계지출"
                , secondary_y = False
    )
    fig
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    
    # 소비지수별 가계지출
    st.markdown('##### [지출코드 7] 교통')
    st.markdown('##### 연도 별 소비자물가지수와 가계지출')


    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(x = df_raw_4["연도"], y = df_raw_4["가계지출"]
            , name = "연도 별 가계지출", width = 0.4, marker = dict(color = "#e6e8ef")),
                secondary_y = False)

    fig.add_trace(
        go.Scatter(mode = 'lines+markers+text'
                , x= df_raw_4["연도"], y = df_raw_4["소비자물가지수"]
                , name = "연도 별 소비자물가지수", marker = dict(color = "#8446Db")), secondary_y = True
    )

    fig.update_layout(
        width= 450
        ,legend=dict(
            orientation="h", # 가로 방향으로
            yanchor="top", y=1.11, # y축 방향 위치 설정
            xanchor="right", x=1, # x축 방향 위치 설정
        )
        , margin=dict(l=10, r=0, t=80, b=20)
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
                , title_text="소비자물가지수"
                , secondary_y = True
    ).update_yaxes(
                title_text="가계지출"
                , secondary_y = False
    )
    fig
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    
with col2_2:
    # 소비지수별 가계지출
    st.markdown('##### [지출코드 3] 의류 및 신발')
    st.markdown('##### 연도 별 소비자물가지수와 가계지출')


    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(x = df_raw_3["연도"], y = df_raw_3["가계지출"]
            , name = "연도 별 가계지출", width = 0.4, marker = dict(color = "#e6e8ef")),
                secondary_y = False)

    fig.add_trace(
        go.Scatter(mode = 'lines+markers+text'
                , x= df_raw_3["연도"], y = df_raw_3["소비자물가지수"]
                , name = "연도 별 소비자물가지수", marker = dict(color = "#8446Db")), secondary_y = True
    )

    fig.update_layout(
        width=450
        , legend=dict(
            orientation="h", # 가로 방향으로
            yanchor="top", y=1.11, # y축 방향 위치 설정
            xanchor="right", x=1, # x축 방향 위치 설정
        )
        , margin=dict(l=10, r=0, t=80, b=20)
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
                , title_text="소비자물가지수"
                , secondary_y = True
    ).update_yaxes(
                title_text="가계지출"
                , secondary_y = False
    )
    fig
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')


    # 소비지수별 가계지출
    st.markdown('##### [지출코드 6] 보건')
    st.markdown('##### 연도 별 소비자물가지수와 가계지출')


    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(x = df_raw_6["연도"], y = df_raw_6["가계지출"]
            , name = "연도 별 가계지출", width = 0.4, marker = dict(color = "#e6e8ef")),
                secondary_y = False)

    fig.add_trace(
        go.Scatter(mode = 'lines+markers+text'
                , x= df_raw_6["연도"], y = df_raw_6["소비자물가지수"]
                , name = "연도 별 소비자물가지수", marker = dict(color = "#8446Db")), secondary_y = True
    )

    fig.update_layout(
        width=450
        , legend=dict(
            orientation="h", # 가로 방향으로
            yanchor="top", y=1.11, # y축 방향 위치 설정
            xanchor="right", x=1, # x축 방향 위치 설정
        )
        , margin=dict(l=10, r=0, t=80, b=20)
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
                , title_text="소비자물가지수"
                , secondary_y = True
    ).update_yaxes(
                title_text="가계지출"
                , secondary_y = False
    )
    fig
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
st.markdown('')
st.markdown('')

st.markdown('## 소득 계층 별 소비자물가지수에 따른 가계지출')
st.markdown('''
물가 상승에 민감한 7개 항목에 대한 추가분석으로 소득계층별 소비자물가지수에 따른 가계지출을 시각화해보았습니다.  \n
**결과1.** 저소득층이 가장 많이 지출하는 항목은 식료품 및 비주류 항목이며 고소득층은 음식 및 숙박 항목에 가장많은 지출을 하는 것으로 나타났습니다.  \n
**결과2.** 저소득층은 교육 항목에 가장 적은 소비를 하며, 소득이 높아질수록 교육에 투자하는 지출이 점점 늘어나는 것을 볼 수 있습니다.  \n
**결과3.** 의류 및 신발 항목도 소득이 높아질수록 지출이 높아지며, 주택 수도, 보건, 통신항목은 소득계층간에 큰 차이가 없음을 확인할 수 있습니다. \n
            ''')
fig= px.scatter(raw02[(raw02["지출목적"].isin(["식료품 및 비주류음료", "주택 수도 전기 및 연료","보건"
            ,"통신", "교육", "음식 및 숙박", "의류 및 신발"])) & (raw02["소득계층"] != "전체")]
        , x = "소비자물가지수", y = "가계지출", color = "지출목적"
                  , facet_col = "소득계층", facet_col_wrap = 10, size = "가계지출",log_x = True, height = 500, width = 2000)

fig.update_layout(
    title_text="<b></b>",
    width= 1000,
    height= 800,
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="top", y=1.1, # y축 방향 위치 설정
        xanchor="right", x=1.0, # x축 방향 위치 설정
	)
    , margin=dict(l=20, r=0, t=110, b=0)
    # , plot_bgcolor='#fff'
).update_xaxes(showgrid=True
               , gridwidth=1
               , title_text="소비자물가지수"
).update_yaxes(
                showgrid=True
               , gridwidth=1
            #    , title_text="<b>가계지출</b>"
               , secondary_y=True
)
fig
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')


url3 = "data/in/raw03.csv"
raw03 = load_data(url3)



# 정규화 과정
df_num = raw03[["실업률 (%)", "고용률 (%)"]]
df_std = (df_num - df_num.mean())/df_num.std()
df_std.insert(0, "시점", raw03["시점"])
df_std["전년대비 물가상승률"] = raw03["전년대비 물가상승률"]

st.markdown('## 전년대비 물가상승률과 연도 별 고용률')
fig1 = make_subplots(specs=[[{"secondary_y": True}]])

# 물가상승률과 실업률 비교
st.markdown('#### 연도 별 물가상승률과 취업률 및 실업률')
# 연도 별 물가상승률과 취업률 및 실업률
fig15 = make_subplots(specs=[[{"secondary_y": True}]])

fig15.add_trace(
    go.Scatter(mode = 'lines+markers+text', x= df_std["시점"], y = df_std["전년대비 물가상승률"], 
           name = "전년대비 물가상승률", marker = dict(color = "#DC5373")), secondary_y = False
)

# 실업률(정규화)
fig15.add_trace(
    go.Scatter(mode = 'lines+markers+text', x = df_std["시점"], y = df_std["실업률 (%)"]
           , name = "실업률", marker = dict(color = "#807DBA")),
            secondary_y = True)

# 고용률(정규화)
fig15.add_trace(
    go.Scatter(mode = 'lines+markers+text', x = df_std["시점"], y = df_std["고용률 (%)"]
           , name = "취업률", marker = dict(color = "#3F007D")),
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
st.markdown('''
물가상승률과 취업률/실업률 사이에 어떠한 **상관관계를 확인할 수 없음**  
세 지표 모두 **외부적 요인에 의해 영향**을 받는 지표  \n
**물가상승률의 주된 급등락 원인**: 국제 유가, 원자재 가격, 환율
            ''')
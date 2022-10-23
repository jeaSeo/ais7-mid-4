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
   page_title="[지출코드 10] 교육 - 으4으4",
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
code10 = pd.read_csv('data/out/code10.csv')


st.markdown('# 지출코드 10 - 교육')
st.markdown('''
            **분석1.** 2012 ~ 2017년도의 물가는 계속 상승하는 반면 지출은 감소하고 있습니다.  
            물가와 지출이 반비례 관계를 가지는 이유는 소비자는 해당 품목의 비용이 증가하면 ‘교육’에 대한 지출을 줄인다는 것을 알 수 있습니다.  \n
            **분석2.** 교육에 대한 물가지수는 매년 증가하는 추세를 보이다가 2019년에 급락하였습니다.  
            코로나19로 인해 비교적 저렴한 비대면 교육의 확산으로 물가지수가 감소한 것으로 보입니다.  
            따라서 교육 항목은 물가가 상승하면 소비를 줄일 수 있는 항목이며 사회적 이슈에 지출 형태가 달라지는 특성을 가집니다.
            ''')
st.markdown('따라서 교육은 **물가에 매우 민감한 항목**이다.')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

# 소비지수별 가계지출

st.markdown('##### 대상 품목')
code10
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 연도 별 소비자물가지수와 가계지출')
df_raw_10 = raw02[raw02["지출코드"] == 10]
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(x = df_raw_10["연도"], y = df_raw_10["가계지출"]
            ,name = "연도별 가계지출", width = 0.6, marker = dict(color = "#e6e8ef")),
            secondary_y = False)

fig.add_trace(
    go.Scatter(mode = 'lines+markers+text'
               , x= df_raw_10["연도"], y = df_raw_10["소비자물가지수"]
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


st.markdown('##### 소득계층 별 소비자물가지수에 따른 가계지출')
fig = px.scatter(df_raw_10[(df_raw_10["가구형태"] == "전체가구") & (df_raw_10["소득계층"] != "전체")], x = "소비자물가지수", y = "가계지출", color = "소득계층"
           ,size = "가계지출",log_x = True, width=1000, height= 400)
fig.update_layout(
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="top", y=1.18, # y축 방향 위치 설정
        xanchor="right", x=1, # x축 방향 위치 설정
	)
    , margin=dict(l=0, r=0, t=90, b=20)
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


st.markdown('##### 각 소득계층의 연도 별 가계지출')
temp = df_raw_10.loc[df_raw_10['소득계층'] != '전체']
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
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

# st.markdown('##### 소득계층 별 물가지수와 가계지출')
# fig = px.line(df_raw_10[(df_raw_10["가구형태"] != "전체가구") & (df_raw_10["소득계층"] != "전체")]
#         , x = "소비자물가지수", y = "가계지출", color = "소득계층", facet_col = "가구형태", markers = True, width=1000, height=400)
# fig.update_layout(
# 	legend=dict(
#         orientation="h", # 가로 방향으로
#         yanchor="top", y=1.25, # y축 방향 위치 설정
#         xanchor="right", x=1, # x축 방향 위치 설정
# 	)
#     , margin=dict(l=0, r=0, t=105, b=20)
#     # , paper_bgcolor="LightSteelBlue"
#     # , plot_bgcolor='#fff'
# ).update_xaxes(showgrid=True
#                , gridwidth=1
#             #    , gridcolor='#f0f0f0'
#                , title_text="소비자물가지수"
# ).update_yaxes(
#                 showgrid=True
#                , gridwidth=1
#             #    , gridcolor='#f0f0f0'
# )
# fig
# st.markdown(' ')
# st.markdown(' ')
# st.markdown(' ')
# st.markdown(' ')
# st.markdown(' ')
# st.markdown(' ')
# st.markdown(' ')

st.markdown('##### 소득계층 별 각 가구형태의 소비자물가와 가계지출')
temp = df_raw_10.loc[df_raw_10['소득계층'] != '전체']
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
st.markdown('')
st.markdown('')
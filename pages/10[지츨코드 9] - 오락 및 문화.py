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
code9 = pd.read_csv('data/out/code9.csv')


st.markdown('# 지출코드 9 - 오락 및 문화')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

# 소비지수별 가계지출

st.markdown('##### 대상 품목')
code9
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 연도별 소비자물가지수와 가계지출')
df_raw_9 = raw02[raw02["지출코드"] == 9]
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(x = df_raw_9["연도"], y = df_raw_9["가계지출"]
            ,name = "연도별 가계지출", width = 0.6, marker = dict(color = "#e6e8ef")),
            secondary_y = False)

fig.add_trace(
    go.Scatter(mode = 'lines+markers+text'
               , x= df_raw_9["연도"], y = df_raw_9["소비자물가지수"]
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


st.markdown('##### 각 소득계층의 연도별 가계지출')
temp = df_raw_9.loc[df_raw_9['소득계층'] != '전체']
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
st.markdown('원의 크기와 위치를 보면 해당 자수에 대한 소득걔충 별 지출의 정도를 알 수 있는데 모든 계층에서 금액의 차이정도만 가지고 있으면서 그 분포가 매우 비슷하다.')
st.markdown('따라서 이 지수에 대해서는 소득계층간의 소비패턴의 차이가 없어가 작다고 볼 수 있다.')

st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 소득계층별 물가지수와 가계지출')
fig = px.line(df_raw_9[(df_raw_9["가구형태"] != "전체가구") & (df_raw_9["소득계층"] != "전체")]
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
fig = px.scatter(df_raw_9[(df_raw_9["가구형태"] == "전체가구") & (df_raw_9["소득계층"] != "전체")], x = "소비자물가지수", y = "가계지출", color = "소득계층"
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
temp = df_raw_9.loc[df_raw_9['소득계층'] != '전체']
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
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('##### 최종결론')
st.markdown('**의견1**')
st.markdown('  - 오락 및 문화에 대한 소비자물가지수는 지속적으로 상승하는 추세를 보입니다. ')
st.markdown('  - 2015년까지는 물가의 상승에도 가계지출은 큰 변화가 없었지만 2016년부터 상승하기 시작하면서 지수와 흐름을 같이하였고 2018년 지수도, 가계지출도 모두 그래프상 정점을 찍었습니다.')
st.markdown('  - 이후의 가계지출도 지수의 등락과 흐름이 같습니다.')
st.markdown('  - 이는 전 소득계층에서 동일하게 확인되고 있습니다.')
st.markdown('  - 따라서 오락 및 문화는 물가에 영향을 받지 않는 품목으로 볼 수 있습니다')
st.markdown('')
st.markdown('**의견 2**')
st.markdown('   - 2012년 대비 2016년에 물가지수가 다소 상승하였으나 이에 반해 지출금액은 큰 차이가 없다.')
st.markdown('   - 2020년~2021년에도 지수는 증가하였으나 지출금액은 큰 차이가 없다.')
st.markdown('   - 가격이 상승하면 이에 따라 지출금액도 어느정도 상승해야 동일한 양을 소비했다고 볼 수 있으며,')
st.markdown('   - 사람들이 일정 수준의 지출금액을 맞추기 위해 소비양을 줄였다고 해석할 수 있다.')
st.markdown('   - 즉, 사람들에게는 소비할 수 있는 최대 금액 기준이 있는 것으로 해석된다.')
st.markdown('   - 따라서 오락 및 문화는 물가에 영향을 받는 품목으로 해석할 수 있다.')
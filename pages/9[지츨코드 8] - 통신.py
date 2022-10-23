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
st.markdown('- 최종결론: 가격에 민감한 항목이다.')
st.markdown('- 2012년 ~ 2019년 물가지수(라인)와 지출금액(막대)의 추이가 비슷한 흐름을 가지고 있다.')
st.markdown('- 즉, 지수가 감소하면 지출금액도 함께 감소하는 흐름이라고 할 수 있다.')
st.markdown('- 흐름이 반대되는 2015~2016년, 물가지수는 다소 상승하였으나 지출은 다소 감소하였다.')
st.markdown('- 가격에 영향을 받았다고 해석할 수도 있으나, 이는 2014년 10월에 시행된 단통법의 영향이라고 볼 수 있다.')
st.markdown('- 단통법은 보조금을 받는 것이며, 사람들이 소비를 줄인 것이 아닌 보조금을 받아 실질 지출금액의 합계가 다소 줄어든 것으로 해석해는 것이 옳아보인다.')
st.markdown('- 2019년 ~ 2021년에는 물가지수가 다소 많이 하락을 하였지만, 지출금액은 이전과 비슷한 수준으로 보인다.')
st.markdown('- 소비량 = 지출금액/물가지수 인 점을 고려하고 2019~2020년 물가지수가 하락한 정도에 비해 지출이 하락한 정도가 작다는 점, 2021년에는 지수가 하락하였음에도 지출금액이 늘었다는 점을 고려하면 사람들의 소비량이 늘었다고 해석할 수 있다.')
st.markdown('- 지수 변동과 관련 없이 사람들이 일정 수준의 금액을 지출하려는 경향이 있다고 볼 수 있는데, 이는 가격에 민감한 것으로 볼 수 있다.')
st.markdown('- 지수가 지속적으로 떨어지는 것에는 5G 사용자가 포함되지 않았다는 점도 고려해야 한다. "통계청은 통계에서 5G 통신 요금제가 충분히 활성화되지 않은 것으로 판단, 2G·3G·LTE 요금제로만 산출했다" & "CPI는 동일한 품질하에서 가격변동을 측정하기 때문에 LTE 요금제에서 5G 요금제로의 가격 변동은 품질 상승에 의한 것으로 가격 상승으로 단정할 수 없다"')

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
st.markdown('- 원의 크기는 지출금액을 의미한다.')
st.markdown('- 전반적으로 소득이 많을 수록 더 많은 값을 지출하고 있다.')
st.markdown('- 물가지수가 상승함에 따라, 소득이 많은 사람들은 원의 분포가 다소 위로 이동하였음을 볼 수 있다.')
st.markdown('- 가격 상승에 따라 지출금액이 어느정도 상승할 수도 있음을 고려하였을 때 비슷한 양을 소비했거나 더 많은 양을 소비했음을 알 수 있다.')
st.markdown('- 그러나, 소득이 적은 사람들은 물가가 상승함에 따라 원의 크기가 더 작아지고 점점 아래로 분포하고 있음 볼 수 있다.')
st.markdown('- 이는 소득이 많은 사람은 가격에 민감하지 않게 반응하며, 소득이 적은 사람은 가격에 민감하게 반응함을 의미한다. ')
 
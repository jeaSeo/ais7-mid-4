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
   page_title="[지출코드 1] 식료품 및 비주류음료 - 으4으4",
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
code1 = pd.read_csv('data/out/code1.csv')


st.markdown('# 지출코드 1 - 식료품 및 비주류음료')
st.markdown('''
            **분석1.** 2012~2016 물가 상승으로 인해 식료품 등의 필수 품목의 실질 지출이 감소했다.  
            **분석2.** 2017년 조류인플루엔자 및 계란 파동, 오징어 어획량 감소의 원인에 따른 주 식료품 가격 인상으로 가계지출이 급증했다.  
            **분석3.** 2019년부터 역대급 폭염 및 기록적인 폭우로 출하량등이 감소하여 물가가 급증해 전체적으로 가격이 인상되었으며, 그만큼 가계지출이 증가했다.  
            따라서 식료품 및 비주류음료는 물가에 민감한 항목이다.
            ''')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

# 소비지수별 가계지출

# 지출코드1
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
df_raw_1

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(x = df_raw_1["연도"], y = df_raw_1["가계지출"]
           , name = "연도별 가계지출", width = 0.4, marker = dict(color = "#e6e8ef")),
            secondary_y = False)

fig.add_trace(
    go.Scatter(mode = 'lines+markers+text'
               , x= df_raw_1["연도"], y = df_raw_1["소비자물가지수"]
               , name = "연도별 소비자물가지수", marker = dict(color = "#8446Db")), secondary_y = True
)

fig.update_layout(
	legend=dict(
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

st.markdown('##### 각 소득계층의 연도별 가계지출')
temp = df_raw_1.loc[df_raw_1['소득계층'] != '전체']
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

st.markdown('##### 소득계층 별 각 가구형태의 소비자물가와 가계지출')
temp = df_raw_1.loc[df_raw_1['소득계층'] != '전체']
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
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown('##### 각 가구형태의 소비자물가지수별 가계지출')
temp = df_raw_1.loc[df_raw_1['소득계층'] != '전체']
temp = temp.loc[temp['가구형태'] != '전체가구']
fig = px.line(temp, x = "소비자물가지수", y = "가계지출", color = "소득계층", facet_col = "가구형태", markers = True, width=1000, height= 400)
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
            #    , title_text="소비자물가지수"
)
fig
st.markdown(' ')
st.markdown(' ')
st.markdown('식료품과 비주류음료는 조미식품, 채소, 신선수산동물, 육류, 과일을 포함')
st.markdown('지출목적 1- 연도별 소비자물가지수와 가계지출')
st.markdown('1. 2012~2016년도, 물가지수가 상승하는 상황에서 가계 지출 변동이 없다. ')
st.markdown('=> 소주, 맥주 등의 주류 지출은 전년대 대비 증가하였지만 주류를 제외한 식품 소비는 다소  줄어든 것으로 집계 됨')
st.markdown('=> 물가 상승으로 팍팍해진 삶 -> 식료품 등 필수 품목 실질 지출 줄어듦 (외식 문화 - 가구당 외식 월평균 2.3% 증가 ~ 식료품 소비 감소)')
st.markdown('2. 2017년도, 조류인플루엔자, 계란 파동 등의 영향으로 계란 가격이 전년 대비 43.7% 상승률을 기록하였고, 어확량이 감소한 오징어도 49.9% 상승률을 나타냄 ')
st.markdown('=> 주 식료품인 계란 가격 인상으로 인해 가계지출이 급증한 것으로 판단 됨')
st.markdown('3. 역대급 폭염과 기록적인 폭우로 출하량 감소, 산지 가격 증가 및 가공식품 오름세')
st.markdown('=> 또한, 우크라니아 전쟁 영향으로 물가 급격히 증가되었음')
st.markdown('=> 전체적으로 식료품 가격이 상승하여, 그만큼 가계지출이 증가하였음')
st.markdown('지출목적 1- 소비자물가에 대한 가구형태와 소득계층')
st.markdown('식료품 부문에서 근로자가구보다 근로자외가구에서 소비지출이 더 큰 것을 발견함')
st.markdown('- 이유 1 : 근로자가구에서의 식료품 및 비주류음료 소비지출은 "회사"에서 식사해결 등의 이유로 비교적 낮은 것으로 판단')
st.markdown('              : 1인 가구 증가 ~ 배달 및 테이크아웃의 증가, 패스트푸드점과 분식점 등의 매출액 증가 (최근, 소분, 소용량 제품 수요 증가, 조리식품 등 간편식 수요 확대)')
st.markdown('- 이유 2 : 근로자외가구는 자영업자 포함하기 때문에, 식료품 소비지출에 큰 영향을 준 것으로 판단 ')
st.markdown('=> 물가상승으로 인해 부담을 떠안는 자영업자 (재료비 상승 문제)')
st.markdown('지출목적 1&11 - 연도별 소비자물가지수와 가계지출')
st.markdown('11(음식점 - 외식), 1(식료품) 간의 관계를 비교를 하고 싶었으나, 지출코드 11은 숙박을 포함하고 있음')
st.markdown('—> 2019년 이후 11 항목이 급감한 이유는, 코로나19로 인해 숙박서비스 같은 대면 서비스 이용 줄었기 때문인 것으로 판단 됨')
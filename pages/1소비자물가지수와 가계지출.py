from plotly.graph_objs.scatter import marker
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

# 본 프로젝트 차트 모듈
import charts

# 선 그래프 여러개 - 지출코드용 df는 배열로 전달
def oneLineGroup(df, x, y, names, rows, cols, width=1000, height=800):
    fig = make_subplots(rows=rows, cols=cols, horizontal_spacing= 0.03, vertical_spacing= 0.12)
    code = 0
    for r in range(1, int(rows)+1):
        for c in  range(1, int(cols)+1):
            fig.add_trace(go.Scatter(x=df[df['지출코드'] == code+1][x], y=df[df['지출코드'] == code+1][y], 
                                    mode='lines+markers', name=names[code]), row=r, col=c)
            c += 1
            code += 1
        r += 1
    fig.update_layout(
        width= width,
        height= height,
        legend=dict(
            orientation="h", # 가로 방향으로
            yanchor="top", y=1.1, # y축 방향 위치 설정
            xanchor="right", x=1.0, # x축 방향 위치 설정
        )
        , margin=dict(l=20, r=0, t=110, b=0)
    ).update_xaxes(
        showgrid=True
        , gridwidth=1
        , title_text="연도"
    ).update_yaxes(
        showgrid=True
        , gridwidth=1
    )
    return fig

# page setting
st.set_page_config(
   page_title="소비자물가지수와 가계지출 - 으4으4",
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


st.markdown('# 소비자물가지수와 가계지출')
st.markdown('''
본 페이지는 소비자물가지수 데이터와 가계지출 데이터의 EDA결과 입니다.  \n
소비자물가지수는 지난 10년간 꾸준히 상승해 왔으며, 지출품목 별로는 통신, 식료품 및 비주류 음료, 음식 및 숙박 항목에 대한 가계지출이 높게 나타났습니다.  \n
또한 지출항목별로 연도 별 소비자물가지수와 가계지출 추세를 비교해 볼 때 [의류 및 신발, 교육] 항목은 소비자물가지수가 상승하는 반면 가계지출은 하락하는 추세를 보였으며, 이를 제외한 10개 항목은 비슷한 추세를 보였습니다.
            ''')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

# raw1
st.markdown('### 연도 별 소비자물가지수(종합)')
temp = raw01[raw01["지출코드"]== 0]
tempy = '연도'
tempw = '소비자물가지수'
fig = charts.linebar(temp, x=tempy, y=tempw, sy=tempw)
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')


# 연도 별 지출품목 별 가계지출(종합)
st.markdown('### 연도 별 지출품목 별 소비자물가지수(종합)')
names = [raw01[raw01['지출코드'] == x].iloc[0]['지출목적'] for x in range(1,13)]
fig = oneLineGroup(raw01, x='연도',y='소비자물가지수', names=names, rows=4, cols=3)
fig


# 연도 별 지출품목 별 소비자물가지수
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown('### 연도 별 가계지출(종합)')
# raw02_total = raw02[(raw02["소득계층"] == "전체")&(raw02["가구형태"]=="전체가구")&(raw02["지출코드"]==0)]
raw02_total = load_data('data/out/raw02_total.csv')
tempy = '연도'
tempw = '가계지출'
fig = charts.linebar(raw02_total, x=tempy, y=tempw, sy=tempw)
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

# 연도 별 지출품목 별 가계지출(종합)
st.markdown('### 연도 별 지출품목 별 가계지출(종합)')

raw02_total2 = raw02[(raw02["소득계층"] == "전체")&(raw02["가구형태"]=="전체가구")]
fig = oneLineGroup(raw02_total2, x='연도',y='가계지출', names=names, rows=4, cols=3)
fig
st.markdown('- 소비자물가지수와 가계 지출 모두 상승하는 추세이다.')
st.markdown('- 연도 별 소득계층, 가구형태, 지출목절별로 가계지출의 평균을 시각화하였을 때 상대적으로 2016년에서 2017년 사이의 증감폭이 큰 사실을 알 수 있다. ')
st.markdown('- 소득계층이 600만원이상인 집단과 가구형태가 근로자가구인 집단에서 가계지출이 가장 높게 나타났다.')
st.markdown('- 지출품목이 교통, 식료품 및 비주류 음료, 음식 및 숙박인 집단에서 가계지출이 상대적으로 높게 나타났다.')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')


st.markdown('### 소득계층 별 가구형태 별 전체 분석')
fig = charts.scatterGroup(raw02[(raw02["지출코드"].isin([1,3,4,6,8,10,11])) & (raw02["소득계층"] != "전체")]
                        , x='소비자물가지수', y='가계지출', color='지출목적',fcol='소득계층',size="가계지출")
fig
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')

#가구형태 = 전체가구, 지출목적 = 소비지출
st.markdown('### 소득계층 별 연도 별 가계지출(전체)')
#가구형태 = 전체가구, 지출목적 = 소비지출
ib_he = raw02.loc[(raw02["지출목적"] == "소비지출")&(raw02["가구형태"] == "전체가구")&(raw02["소득계층"] != "전체"), ["지출목적","연도", "소득계층", "가계지출"]]
#피봇
pv = ib_he.groupby(["연도","소득계층"])[["가계지출"]].mean().unstack()["가계지출"].T
#가구형태 = 전체가구, 지출목적 = 소비지출
#피봇
#heatmap시각화
fig = charts.heatmap(pv)
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

#가구형태 별 연도 별 가계지출(전체)
st.markdown('### 가구형태 별 연도 별 가계지출(전체)')
hs_he = raw02.loc[(raw02["소득계층"] == "전체")&(raw02["지출목적"]=="소비지출"),["연도","가구형태","가계지출"]]
#피봇
hs_he_pv = hs_he.groupby(["연도","가구형태"])[["가계지출"]].mean().unstack()
#시각화
#heatmap시각화
fig = charts.heatmap(hs_he_pv["가계지출"].T, height=300)
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')


# 지출목적 별 연도 별 가계지출(전체)
st.markdown('### 지출목적 별 연도 별 가계지출(전체)')
#소득계층 = 전체, 가구형태 = 전체가구
ct_he = raw02.loc[(raw02["소득계층"] == "전체")&(raw02["가구형태"]=="전체가구"), ["연도","지출코드","지출목적","가계지출"]]
#소비지출 삭제
ch_id = ct_he[ct_he["지출목적"] == "소비지출"].index
ct_he = ct_he.drop(ch_id)
#피봇
ct_he_pv = ct_he.groupby(["연도","지출목적"])[["가계지출"]].mean().unstack()
#시각화
fig = charts.heatmap(ct_he_pv["가계지출"].T, height=800)
fig

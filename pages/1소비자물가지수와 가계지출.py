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
소비자물가지수는 지난 10년간 꾸준히 상승해 왔으며, 지출품목별로는 통신, 식료품 및 비주류 음료, 음식 및 숙박 항목에 대한 가계지출이 높게 나타났습니다.  \n
또한 지출항목별로 연도별 소비자물가지수와 가계지출 추세를 비교해 볼 때 [의류 및 신발, 교육] 항목은 소비자물가지수가 상승하는 반면 가계지출은 하락하는 추세를 보였으며, 이를 제외한 10개 항목은 비슷한 추세를 보였습니다.
            ''')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

# raw1
st.markdown('### 연도별 소비자 물가지수(종합)')
fig = make_subplots(specs=[[{"secondary_y": True}]])
#add_traces
fig.add_trace(
    go.Line(x=raw01[raw01["지출코드"]== 0]["연도"], y=raw01[raw01["지출코드"]== 0]["소비자물가지수"], name="소비자물가지수"
            , marker=dict(color='#8446db')),
    secondary_y=True,
)
fig.add_trace(
    go.Bar(x=raw01[raw01["지출코드"]== 0]["연도"], y=raw01[raw01["지출코드"]== 0]["소비자물가지수"], name="소비자물가지수", 
          width = 0.4, marker = dict(color = "#e6e8ef")),
    secondary_y=False,
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
               , secondary_y=True
).update_yaxes(
        title_text="소비자물가지수"
        , secondary_y=False
)
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')


# 연도별 지출품목별 가계지출(종합)
st.markdown('### 연도별 지출품목별 소비자물가지수(종합)')
fig = make_subplots(rows=4, cols=3, horizontal_spacing= 0.03, vertical_spacing= 0.12, 
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
             mode='lines+markers', name='주택 수도 전기 및 연료'), row=2, col=1)
fig.add_trace(go.Scatter(x=raw01[raw01["지출코드"] == 5]["연도"],
                         y=raw01[raw01["지출코드"] == 5]["소비자물가지수"],
             mode='lines+markers', name='가정용품 및 가사 서비스'), row=2, col=2)
fig.add_trace(go.Scatter(x=raw01[raw01["지출코드"] == 6]["연도"],
                         y=raw01[raw01["지출코드"] == 6]["소비자물가지수"],
             mode='lines+markers', name='보건'), row=2, col=3)
fig.add_trace(go.Scatter(x=raw01[raw01["지출코드"] == 7]["연도"],
                         y=raw01[raw01["지출코드"] == 7]["소비자물가지수"],
             mode='lines+markers', name='교통'), row=3, col=1)
fig.add_trace(go.Scatter(x=raw01[raw01["지출코드"] == 8]["연도"],
                         y=raw01[raw01["지출코드"] == 8]["소비자물가지수"],
             mode='lines+markers', name='통신'), row=3, col=2)
fig.add_trace(go.Scatter(x=raw01[raw01["지출코드"] == 9]["연도"],
                         y=raw01[raw01["지출코드"] == 9]["소비자물가지수"],
             mode='lines+markers', name='오락 및 문화'), row=3, col=3)
fig.add_trace(go.Scatter(x=raw01[raw01["지출코드"] == 10]["연도"],
                         y=raw01[raw01["지출코드"] == 10]["소비자물가지수"],
             mode='lines+markers', name='교육'), row=4, col=1)
fig.add_trace(go.Scatter(x=raw01[raw01["지출코드"] == 11]["연도"],
                         y=raw01[raw01["지출코드"] == 11]["소비자물가지수"],
             mode='lines+markers', name='음식 및 숙박'), row=4, col=2)
fig.add_trace(go.Scatter(x=raw01[raw01["지출코드"] == 12]["연도"],
                         y=raw01[raw01["지출코드"] == 12]["소비자물가지수"],
             mode='lines+markers', name='기타 상품 및 서비스'), row=4, col=3)
# fig.update_layout(title='<b>연도별 지출품목별 가계지출(종합)</b>')

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
).update_xaxes(
    showgrid=True
    , gridwidth=1
    , title_text="연도"
).update_yaxes(
    showgrid=True
    , gridwidth=1
    # , title_text="소비자물가지수"
)
fig


# 연도별 지출품목별 소비자물가지수
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
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
    go.Bar(x=raw02_total["연도"], y=raw02_total["가계지출"], name="가계지출", 
          width = 0.4, marker = dict(color = "#e6e8ef")),
    secondary_y=False,
)
fig.add_trace(
    go.Line(x=raw02_total["연도"], y=raw02_total["가계지출"], name="가계지출"
            , marker = dict(color='#8446DB')),
    secondary_y=True,
)

fig.update_layout(
    # title_text="<b>연도별 가계지출(종합)</b>",
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="top", y=1.11, # y축 방향 위치 설정
        xanchor="right", x=1, # x축 방향 위치 설정
	)
    , margin=dict(l=10, r=0, t=80, b=20)
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
    , title_text="소비자물가지수"
    , secondary_y=True
).update_yaxes(
    # title_text='가계지출'
    # , secondary_y=True
)
fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

# 연도별 지출품목별 가계지출(종합)
st.markdown('### 연도별 지출품목별 가계지출(종합)')
raw02_total2 = raw02[(raw02["소득계층"] == "전체")&(raw02["가구형태"]=="전체가구")]
fig = make_subplots(rows=4, cols=3, horizontal_spacing= 0.03, vertical_spacing= 0.12, 
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
             mode='lines+markers', name='주택 수도 전기 및 연료'), row=2, col=1)
fig.add_trace(go.Scatter(x=raw02_total2[raw02_total2["지출코드"] == 5]["연도"],
                         y=raw02_total2[raw02_total2["지출코드"] == 5]["가계지출"],
             mode='lines+markers', name='가정용품 및 가사 서비스'), row=2, col=2)
fig.add_trace(go.Scatter(x=raw02_total2[raw02_total2["지출코드"] == 6]["연도"],
                         y=raw02_total2[raw02_total2["지출코드"] == 6]["가계지출"],
             mode='lines+markers', name='보건'), row=2, col=3)
fig.add_trace(go.Scatter(x=raw02_total2[raw02_total2["지출코드"] == 7]["연도"],
                         y=raw02_total2[raw02_total2["지출코드"] == 7]["가계지출"],
             mode='lines+markers', name='교통'), row=3, col=1)
fig.add_trace(go.Scatter(x=raw02_total2[raw02_total2["지출코드"] == 8]["연도"],
                         y=raw02_total2[raw02_total2["지출코드"] == 8]["가계지출"],
             mode='lines+markers', name='통신'), row=3, col=2)
fig.add_trace(go.Scatter(x=raw02_total2[raw02_total2["지출코드"] == 9]["연도"],
                         y=raw02_total2[raw02_total2["지출코드"] == 9]["가계지출"],
             mode='lines+markers', name='오락 및 문화'), row=3, col=3)
fig.add_trace(go.Scatter(x=raw02_total2[raw02_total2["지출코드"] == 10]["연도"],
                         y=raw02_total2[raw02_total2["지출코드"] == 10]["가계지출"],
             mode='lines+markers', name='교육'), row=4, col=1)
fig.add_trace(go.Scatter(x=raw02_total2[raw02_total2["지출코드"] == 11]["연도"],
                         y=raw02_total2[raw02_total2["지출코드"] == 11]["가계지출"],
             mode='lines+markers', name='음식 및 숙박'), row=4, col=2)
fig.add_trace(go.Scatter(x=raw02_total2[raw02_total2["지출코드"] == 12]["연도"],
                         y=raw02_total2[raw02_total2["지출코드"] == 12]["가계지출"],
             mode='lines+markers', name='기타 상품 및 서비스'), row=4, col=3)
# fig.update_layout(title='<b>연도별 지출품목별 가계지출(종합)</b>')

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
st.markdown('- 소비자물가지수와 가계 지출 모두 상승하는 추세이다.')
st.markdown('- 연도별 소득계층, 가구형태, 지출목절별로 가계지출의 평균을 시각화하였을 때 상대적으로 2016년에서 2017년 사이의 증감폭이 큰 사실을 알 수 있다. ')
st.markdown('- 소득계층이 600만원이상인 집단과 가구형태가 근로자가구인 집단에서 가계지출이 가장 높게 나타났다.')
st.markdown('- 지출품목이 교통, 식료품 및 비주류 음료, 음식 및 숙박인 집단에서 가계지출이 상대적으로 높게 나타났다.')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')


st.markdown('### 소득계층별 가구형태별 전체 분석')
fig= px.scatter(raw02[(raw02["지출목적"].isin(["식료품 및 비주류음료", "주택 수도 전기 및 연료","보건", "통신", "교육", "음식 및 숙박", "의류 및 신발"])) & (raw02["소득계층"] != "전체")]
        , x = "소비자물가지수", y = "가계지출", color = "지출목적" , facet_col = "소득계층", facet_col_wrap = 10, size = "가계지출",log_x = True, height = 500, width = 2000)

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
st.markdown('')

#가구형태 = 전체가구, 지출목적 = 소비지출
st.markdown('### 소득계층별 연도별 가계지출(전체)')
#가구형태 = 전체가구, 지출목적 = 소비지출
ib_he = raw02.loc[(raw02["지출목적"] == "소비지출")&(raw02["가구형태"] == "전체가구")&(raw02["소득계층"] != "전체"), ["지출목적","연도", "소득계층", "가계지출"]]
#피봇
pv = ib_he.groupby(["연도","소득계층"])[["가계지출"]].mean().unstack()["가계지출"].T
#가구형태 = 전체가구, 지출목적 = 소비지출
#피봇
#heatmap시각화
hm_fig = px.imshow(pv, text_auto=True, color_continuous_scale='Purples')
hm_fig.update_layout(
    width= 1000,
    height= 500
    , margin=dict(l=0, r=0, t=50, b=0)
    # , plot_bgcolor='#fff'
)
hm_fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

#가구형태별 연도별 가계지출(전체)
st.markdown('### 가구형태별 연도별 가계지출(전체)')
hs_he = raw02.loc[(raw02["소득계층"] == "전체")&(raw02["지출목적"]=="소비지출"),["연도","가구형태","가계지출"]]
#피봇
hs_he_pv = hs_he.groupby(["연도","가구형태"])[["가계지출"]].mean().unstack()
#시각화
hm_fig = px.imshow(hs_he_pv["가계지출"].T, text_auto=True, color_continuous_scale='Purples')
hm_fig.update_layout(
    width= 1000,
    height= 350
    , margin=dict(l=0, r=0, t=50, b=0)
)
hm_fig
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')


# 지출목적별 연도별 가계지출(전체)
st.markdown('### 지출목적별 연도별 가계지출(전체)')
#소득계층 = 전체, 가구형태 = 전체가구
ct_he = raw02.loc[(raw02["소득계층"] == "전체")&(raw02["가구형태"]=="전체가구"), ["연도","지출코드","지출목적","가계지출"]]
#소비지출 삭제
ch_id = ct_he[ct_he["지출목적"] == "소비지출"].index
ct_he = ct_he.drop(ch_id)
#피봇
ct_he_pv = ct_he.groupby(["연도","지출목적"])[["가계지출"]].mean().unstack()
#시각화
hm_fig = px.imshow(ct_he_pv["가계지출"].T, text_auto=True, color_continuous_scale='Purples')
hm_fig.update_layout(
    width= 1000,
    height= 800
    , margin=dict(l=0, r=0, t=50, b=0)
)
hm_fig

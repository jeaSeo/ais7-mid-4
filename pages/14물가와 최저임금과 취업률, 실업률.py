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
url3 = "data/in/raw03.csv"
url4 = "data/in/raw04.csv"
raw03 = load_data(url3)
# raw04 = load_data(url4)

# 정규화 과정
df_num = raw03[["실업률 (%)", "고용률 (%)"]]
df_std = (df_num - df_num.mean())/df_num.std()
df_std.insert(0, "시점", raw03["시점"])
df_std["전년대비 물가상승률"] = raw03["전년대비 물가상승률"]


st.markdown('# 물가상승률과 취업률')
st.markdown(' ')

# 전년대비 물가상승률과 연도별 고용률
st.markdown('#### 전년대비 물가상승률과 연도 별 고용률')
fig1 = make_subplots(specs=[[{"secondary_y": True}]])

fig1.add_trace(
    go.Scatter(mode = 'lines+markers+text', x= df_std["시점"], y = df_std["전년대비 물가상승률"], 
           name = "전년대비 물가상승률", marker = dict(color = "#DC5373")), secondary_y = False
)

# 고용률(정규화)
fig1.add_trace(
    go.Scatter(mode = 'lines+markers+text', x = df_std["시점"], y = df_std["고용률 (%)"]
           , name = "취업률", marker = dict(color = "#ccc")),
            secondary_y = True)

# 실업률(정규화)
fig1.add_trace(
    go.Scatter(mode = 'lines+markers+text', x = df_std["시점"], y = df_std["실업률 (%)"]
           , name = "실업률", marker = dict(color = "#ccc")),
            secondary_y = True)
fig1.update_layout(
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
    , title_text='전년대비 물가상승률(%)'
).update_yaxes(
    secondary_y = True
    , title_text='연도별 고용률(%)'
)
fig1
st.markdown('''
**2003년 ~ 2006년**: 국제 유가가 장기적인 상승로 인해 2004년까지 비교적 높은 물가상승률을 보였지만, 이후 환율이 하락하면서 물가인상의 압력을 상쇄하였다.  \n
**2008년**: 국제유가와 기타원자개 가격, 그리고 환율이 모두 상승하면서 조사한 데이터의 기간 아래 가장 큰 물가상승률을 기록하였다.  \n
**2009년 ~ 2010년**: 서브 프라임 모기지 사태로 인한 국제금융위기로 인해 수요가 줄어들면서 물가상승률이 하락하였다.  \n
**2011년**: 구제역 및 이상기후의 영향으로 농축수산물의 가격과 원자재 가격이 상승하면서 물가상승률이 상승세로 돌아섰다.  \n
**2012년**~ 2016년 : 국제원자재가격이 안정세에 돌입하면서 물가상승률이 하락하였다.  \n
**2017년**: 글로벌 원유수요 증가 및 중동지역 정정불안으로 인해 국제원유가격이 상승하면서 수입물가가 대폭 상승하여 물가상승률이 전년에 비해 급등하였다.  \n
**2018년 ~ 2019년**: 국제원자재 및 농산물가격이 안정되면서 물가상승률이 하락하였다.  \n
**2021년**: 코로나 판데믹 사태로 인해 국제 경기가 둔화되면서 정부가 경제 부양을 위한 여러 금융 지원 정책을 펼쳤고, 이는 자산의 가격 상승으로 이어지며 물가상승률이 급등하였다.\n
            ''')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')



# 전년대비 물가상승률과 연도별 고용률
st.markdown('#### 전년대비 물가상승률과 연도 별 고용률')
fig1 = make_subplots(specs=[[{"secondary_y": True}]])

fig1.add_trace(
    go.Scatter(mode = 'lines+markers+text', x= df_std["시점"], y = df_std["전년대비 물가상승률"], 
           name = "전년대비 물가상승률", marker = dict(color = "#ccc")), secondary_y = False
)

# 고용률(정규화)
fig1.add_trace(
    go.Scatter(mode = 'lines+markers+text', x = df_std["시점"], y = df_std["고용률 (%)"]
           , name = "취업률", marker = dict(color = "#ccc")),
            secondary_y = True)

# 실업률(정규화)
fig1.add_trace(
    go.Scatter(mode = 'lines+markers+text', x = df_std["시점"], y = df_std["실업률 (%)"]
           , name = "실업률", marker = dict(color = "#807DBA")),
            secondary_y = True)
fig1.update_layout(
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
    , title_text='전년대비 물가상승률(%)'
).update_yaxes(
    secondary_y = True
    , title_text='연도별 고용률(%)'
)
fig1
st.markdown('''
실업률의 급등은 고용률의 급락과 같은 원인을 공유합니다. \n 
2003년에는 수출증가세의 둔화와 국제 유가 상승 등으로 인한 경기회복률이 저하하면서 실업률이 증가하고 2005년까지 이어져가는 모습을 확인할 수 있습니다.  
2014년부터 2019년까지 실업률은 고용률과 같이 우상향하는데 이는 노동시장의 개선으로 인한 영향으로 볼 수 있습니다.  \n
예외적으로, 2008년의 경우 서브 프라임 모기지 사태의 발생으로 인한 금융위기가 발생했는데도 불구하고 자연실업률에 가까운 수치를 보여줬는데, 이는 구직 단념자와 같은 실질적인 미취업자가 통계에 실업자로 포함되지 않아 나타난 현상으로 볼 수 있습니다.
            ''')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')


# 물가상승률과 실업률 비교
st.markdown('#### 연도별 물가상승률과 취업률 및 실업률')
# 연도별 물가상승률과 취업률 및 실업률
fig15 = make_subplots(specs=[[{"secondary_y": True}]])

fig15.add_trace(
    go.Scatter(mode = 'lines+markers+text', x= df_std["시점"], y = df_std["전년대비 물가상승률"], 
           name = "전년대비 물가상승률", marker = dict(color = "#ccc")), secondary_y = False
)

# 실업률(정규화)
fig15.add_trace(
    go.Scatter(mode = 'lines+markers+text', x = df_std["시점"], y = df_std["실업률 (%)"]
           , name = "실업률", marker = dict(color = "#ccc")),
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
대규모 경제위기(~ 2001년: IMF 금융위기, 2009년 ~ 2010년: 서브 프라임 모기지사태로 인한 국제 금융 위기, 2020년: 코로나 팬대믹으로 인한 국제 경기 둔화)가 도래한 경우 고용률이 급락한 모습을 확인 할 수 있었으며, 2003년에는 5대 수출품목 산업의 부진으로 인해 해당 산업의 고용률이 낮아지면서 전체적인 고용률이 하락하였습니다.  \n
이를 제외한다면 전체적으로 고용률은 경제 위기상황에서 회복하여 우상향하는 모습을 확인 할 수 있었습니다.
            ''')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')


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
   page_title="[지출코드 7] 교통 - 으4으4",
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
code7 = pd.read_csv('data/out/code7.csv')


st.markdown('# 지출코드 7 - 교통')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

# 소비지수별 가계지출

st.markdown('##### 대상 품목')
code7
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
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

st.markdown(' ')
st.markdown('##### [첨고지표] 월간 유가지수(Dubai Crude)')
# 두바이유 (Dubai Crude), monthly
df_du = pd.read_csv('data/out/df_du.csv')
# df_du.columns = [' Dubai Crude']
fig = px.line(df_du, x='DATE', y=' Dubai Crude')
fig.update_layout(
	legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="bottom", y=-0.2, # y축 방향 위치 설정
        xanchor="left", x=0.28, # x축 방향 위치 설정
	)
    , margin=dict(l=0, r=0, t=10, b=20)
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

st.markdown('##### 가구형태로 본 소득계층 별 소비자물가와 가계지출')
raw_df_7 = raw02[raw02["지출코드"] == 7]
temp = raw_df_7.loc[raw_df_7['소득계층'] != '전체']
temp = temp.loc[temp['가구형태'] != '전체가구']
chart7 = px.scatter(temp, x = "소비자물가지수", y = "가계지출", color = "가구형태", facet_col = "소득계층"
            ,facet_col_wrap=4,  size = "가계지출",log_x = True, )
chart7.update_layout(
    width=1000
    , height = 650
	, legend=dict(
        orientation="h", # 가로 방향으로
        yanchor="top", y=1.12, # y축 방향 위치 설정
        xanchor="right", x=1, # x축 방향 위치 설정
	)
    , margin=dict(l=0, r=0, t=105, b=20)
    # , paper_bgcolor="LightSteelBlue"
    # , plot_bgcolor='#fff'
).update_xaxes(showgrid=True
               , gridwidth=1
            #    , title_text="소비자물가지수"
).update_yaxes(
                showgrid=True
               , gridwidth=1
)
chart7

st.markdown('교통지수는 개인운송수단 운영비와 운송서비스 이용비용 등의 항목으로 구성된 지수이다.')
st.markdown('그런데 근로가가구와 근로자외가구의 차트를 보면 재미있는 흐름을 읽을 수 있는데 바로 소득계층과 크게 관련없이 근로자와 근로자외가구(사업자 등)의 지출의 패턴이 같다는 것이다.')
st.markdown('차트를 보면 최저 소득계층(100만원 미만)의 근로자와 근로자외가구의 차이가 보이는데 바로 위 소득계층(100만원 이상~200만원 이하)부터 근로자 가구와 근로자외 가구의 차이가 거의 없어진다.')
st.markdown('처음 ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown('교통부분 소비자물가지수')
st.markdown('| 구분 | 설명 ||-----|----|| 운송장비 | 승용차,수입 승용차,경 승용차 등 일반적인 탈 것 || 개인 운송장비 운영 | 연료 및 윤활류, 자동차용품, 주차료 등 전반적인 운송장비의 운영비를 말함 || 운송 서비스 | 전철료, 택시료, 택배이용료 등 운송관련 서비스 이용요금임 |')
st.markdown('- 운송장비, 개인 운송장비 운영, 운송서비스를 총괄하는 지수')
st.markdown('- 국제유가가 국내 물가에 반영되려면 통상 2~3주정도 소요')
st.markdown('- 유가에 대한 소비자 물가 지수가 오르면 상대적으로 높은 소득을 가지는 계층일수록 가계지출에 대한 변동폭이 컸음')
st.markdown('- 이는 유가 변동으로 인한 운송서비스 비용에 대한 변화가 영향을 미치지 않았나 생각해볼 수 있음')
st.markdown('  - 개인 운송장비 혹은 비행기 등 운송서비스')
st.markdown('- 왜냐하면 저소득층일수록 유가에 대한 영향이 큰데 차트에서 보면 교통에서는 지수가 올라도 저소득층의 가계지출 그에맞게 변하거나 지수보다 뎔 변화하는 경향이 보이기 때문')
st.markdown('  - 기본적으로 유가가 상승하면 저소득층의 연로비(난방, 운송비 등)가 소득대비 비중이 높아지는 특성이 있는듯 하다')
st.markdown('- 연도별로 보았을 때 2014~2016년 유가가 급락하던 시기의 소비자물가지수의 낙폭은 국제유가와 비슷함')
st.markdown('  - 그러나 가계지출은 많이 줄어들지 않음')
st.markdown('  - 따라서 물가가 떨어져서 소비가 늘어난 것으로 볼 수 있음')
st.markdown('- 2019년부터 시작된 지수의 하락이 2021년까지 지속되었고 물가지수, 가계지출이모두 비슷한 흐름을 가짐')
st.markdown('  - 이는 코로나19의 영향으로 소비위축이 되어 지수하락에도 불구하고 소비가 늘어나지 않은 모습')
st.markdown('    - 2014~2016년과 다름')
st.markdown('- 국제유가는 외부 요인이 많이 작용하여 변동이 일어나는 부분')
st.markdown('- 유가는 수요는 거의 비슷하기에 공급이 가격변동에 많은 영향을 주는 경향')
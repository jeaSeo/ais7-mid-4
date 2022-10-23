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


from PIL import Image

# page setting
st.set_page_config(layout="wide")

@st.cache
def load_data(url):
    return pd.read_csv(url)
url1 = "data/out/raw01.csv"
url2 = "data/out/raw02.csv"
raw01 = load_data(url1)
raw02 = load_data(url2)



st.markdown('# 으4으4 - 소비자물가지수가 사회에 미치는 영향')
st.markdown(' ')
st.markdown('''
            최근, 코로나19와 러시아-우크라이나 전쟁 등으로 인한 우리는 유례없는 급격한 물가 인플레이션을 겪고 있습니다.  
            이러한 상황 속에서 치솟는 물가가 우리의 삶에 어떠한 영향을 끼치는지 알아보기 위해 과거부터 측정된 소비자 물가지수 데이터를 분석하며 물가상승이 가계지출에 미치는 영향을 분석하고자 합니다.
            ''')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown('#### 💡 가설')
st.markdown('**_가설 1_**: 소비자물가지수는 가계지출에 영향을 주지 않는다.')
st.markdown('**_가설 2_**: 소비자물가지수는 가계지출에 영향을 준다.')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')

st.markdown('#### 👀 예상결론')
st.markdown('소비자물가지수를 구성하는 12개의 지출품목 중 가중치가 100이 넘는 아래의 항목 5개는 물가 상승에 따른 가격에 민감하게 반응하지 않을 것')
image1 = Image.open('data/image1.png')
st.image(image1, caption='가중치가 100이 넘는 항목, 가중치: 전년도 지출금액에서 차지하는 정도 즉, 중요도를 기준으로 산정')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')

st.markdown('#### 👩🏻‍💻 분석 과정')
st.markdown('다음과 같은 순서로 데이터 수집 및 전처리, 데이터 분석, 최종 결론 도출을 하였습니다.')
image2 = Image.open('data/image2.png')
st.image(image2, width=800)
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')

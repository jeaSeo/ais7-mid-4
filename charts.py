import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from PIL import Image


# 바 랑 라인 동시에
def linebar(df, x, y, sy=None, width=700, mainColor="#8446Db"):
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Bar(x = df[x], y = df[y] , name = (x+'별'+y), width = 0.4, marker = dict(color = "#e6e8ef")), secondary_y = False)
    if sy != None:
        fig.add_trace(go.Scatter(mode = 'lines+markers+text', x= df[x], y = df[sy], name = (x+" 별 "+y), marker = dict(color = mainColor)), secondary_y = True)
        
    fig.update_layout(
        width=width
        , legend=dict(
            orientation="h", # 가로 방향으로
            yanchor="top", y=1.11, # y축 방향 위치 설정
            xanchor="right", x=1, # x축 방향 위치 설정
        )
        , margin=dict(l=10, r=0, t=80, b=20)
        # , paper_bgcolor="LightSteelBlue"
        , plot_bgcolor='#fff'
    ).update_xaxes(
        showgrid=True
        , gridwidth=1
        , gridcolor='#f0f0f0'
        , title_text=x
    ).update_yaxes(
        showgrid=True
        , gridwidth=1
        , gridcolor='#f0f0f0'
    ).update_yaxes(
        title_text=y
        , secondary_y = False
    )
    
    if sy != None:
        fig.update_layout(

        ).update_yaxes(
            title_text=sy
            , secondary_y = True
        )
        
    return fig

# 스케터 한개짜리
def scatter(df, x, y, color, size, width=1000, height=400):
    fig = px.scatter(df, x=x,y=y,color=color,size=size,log_x = True)
    fig.update_layout(
        width=width
        , height= height
        , legend=dict(
            orientation="h", # 가로 방향으로
            yanchor="top", y=1.18, # y축 방향 위치 설정
            xanchor="right", x=1, # x축 방향 위치 설정
        )
        , margin=dict(l=0, r=0, t=90, b=20)
    ).update_xaxes(
        showgrid=True
        , gridwidth=1
        , title_text=x
    ).update_yaxes(
        showgrid=True
        , gridwidth=1
    )
    return fig

# 스캐터로 크기까지 표현
def scatterGroup(df, x, y, color, fcol, size, facet_col_wrap = 10, width=1000, height=800):
    fig= px.scatter(df , x = x, y = y, color = color
                    , facet_col = fcol, facet_col_wrap = facet_col_wrap, size = size,log_x = True)
    fig.update_layout(
        title_text="<b></b>",
        width= width,
        height= height,
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
        , title_text=x
    ).update_yaxes(
        showgrid=True
        , gridwidth=1
        , secondary_y=True
    )
    return fig

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

# heatmap
def heatmap(df, text_auto=True, colorTheme='Purples', width=1000, height=500):
    fig = px.imshow(df, text_auto=text_auto, color_continuous_scale=colorTheme)
    fig.update_layout(
        width= width
        , height= height
        , margin=dict(l=0, r=0, t=50, b=0)
    )
    return fig

# 단일 Histogram
def histogram(df, x, y, color, histfunc='avg', barmode="group"):
    fig = px.histogram(df, x=x, y=y, histfunc=histfunc,color=color, barmode=barmode)
    fig.update_layout(
        legend=dict(
            orientation="h", # 가로 방향으로
            yanchor="top", y=1.11, # y축 방향 위치 설정
            xanchor="right", x=1, # x축 방향 위치 설정
        )
        , margin=dict(l=0, r=0, t=90, b=20)
    ).update_xaxes(
        showgrid=True
        , gridwidth=1
        , title_text=x
    ).update_yaxes(
        showgrid=True
        , gridwidth=1
    )
    return fig

# allproperty heatmap
def histoGroup(df, x, y, color, fcol, histfunc='avg', barmode="group", facet_col_wrap=4, width=1000, height=400):
    fig = px.histogram(df, x=x, y=y , color=color, facet_col=fcol, histfunc=histfunc
            , barmode = barmode, facet_col_wrap=facet_col_wrap)
    fig.update_layout(
        width= width
        , height= height
        , legend=dict(
            orientation="h", # 가로 방향으로
            yanchor="top", y=1.25, # y축 방향 위치 설정
            xanchor="right", x=1, # x축 방향 위치 설정
        )
        , margin=dict(l=0, r=0, t=105, b=20)
    ).update_xaxes(
        showgrid=True
        , gridwidth=1
    ).update_yaxes(
        showgrid=True
        , gridwidth=1
    )
    return fig

# 차트 하나에 멀티라인인거 그룹
def multiLineGroup(df, x, y, color, fcol, width=1000, height=400):
    fig = px.line(df, x=x, y=y, color=color, facet_col=fcol, markers = True)
    fig.update_layout(
        width=width
        , height=height
        , legend=dict(
            orientation="h", # 가로 방향으로
            yanchor="top", y=1.25, # y축 방향 위치 설정
            xanchor="right", x=1, # x축 방향 위치 설정
        )
        , margin=dict(l=0, r=0, t=105, b=20)
    ).update_xaxes(
        showgrid=True
        , gridwidth=1
        , title_text="소비자물가지수"
    ).update_yaxes(
        showgrid=True
        , gridwidth=1
    )
    return fig

# 선 세개짜리 라인차트
def tripleLineplot(df, x, y1, c1, y2, c2, y3, c3):
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Scatter(mode = 'lines+markers+text', x= df[x], y = df[y1], 
            name = y1, marker = dict(color = c1)), 
                secondary_y = True)

    # 실업률(정규화)
    fig.add_trace(
        go.Scatter(mode = 'lines+markers+text', x = df[x], y = df[y2]
            , name = y2, marker = dict(color = c2)),
                secondary_y = True)

    # 고용률(정규화)
    fig.add_trace(
        go.Scatter(mode = 'lines+markers+text', x =df[x], y = df[y3]
            , name = y3, marker = dict(color = c3)),
                secondary_y = False)

    fig.update_layout(
        legend=dict(
            orientation="h", # 가로 방향으로
            yanchor="top", y=1.11, # y축 방향 위치 설정
            xanchor="right", x=1, # x축 방향 위치 설정
        )
        , margin=dict(l=10, r=0, t=80, b=20)
        # , paper_bgcolor="LightSteelBlue"
        , plot_bgcolor='#fff'
    ).update_xaxes(
        showgrid=True
        , gridwidth=1
        , gridcolor='#f0f0f0'
        , title_text=x
    ).update_yaxes(
        showgrid=True
        , gridwidth=1
        , gridcolor='#f0f0f0'
        , title_text=y3
    ).update_yaxes(
        title_text=y1
        , secondary_y=True
    )
    return fig


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
st.markdown('''
# 🎃 ʜᴀᴘᴘʏ ʜᴀʟʟᴏᴡᴇᴇɴ 👻  \n
''')
st.markdown('#### ')
halloween = Image.open('data/halloween.jpg')
st.image(halloween)
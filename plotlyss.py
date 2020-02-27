"""
Plotly 是一款用来做数据分析和可视化的在线平台，功能非常强大,
可以在线绘制很多图形比如条形图、散点图、饼图、直方图等等;
而且还是支持在线编辑.
"""

import plotly
import plotly.offline as py
import numpy as np
import plotly.graph_objs as go
from plotly.graph_objs import Scatter, Layout
'''
    #setting offline
    #plotly.offline.init_notebook_mode(connected=True)

'''


plotly.offline.offline = True

tracer1 = go.Scatter(
    y=np.random.randn(5000),
    mode='markers',
    marker=dict(
        size=5,
        color=np.random.randn(5000),
        colorscale='Viridis',
        showscale=True
    )
)

data=[tracer1]
py.plot(data, filename='scatter-plot-with-colorscale.html')




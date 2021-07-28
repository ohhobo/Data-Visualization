import plotly.express as px
import json
import pandas as pd

with open('data/data_lons.json') as f:
    lons=json.load(f)
with open('data/data_lats.json') as f:
    lats=json.load(f)
with open('data/data_titles.json') as f:
    titles=json.load(f)
with open('data/data_mags.json') as f:
    mags=json.load(f)

data=pd.DataFrame(
    data=zip(lons,lats,titles,mags),columns=['经度','纬度','位置','震级']
)
data.head()
fig=px.scatter(
    # x=lons,
    # y=lats,
    # labels={'x':'经度','y':'纬度'},
    data,
    x='经度',
    y='纬度',
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置'
)
fig.write_html('global_earthquakes.html')
fig.show()
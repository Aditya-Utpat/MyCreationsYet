from bokeh.plotting import figure,show,output_file
from bokeh.layouts import gridplot
import sqlite3

conn = sqlite3.connect('youtube_data.sqlite')
cur = conn.cursor()

cur.execute(''' SELECT name,subscribers,videocount,id FROM channel ''')
channels = cur.fetchall()
names = [x[0] for x in channels]

output_file('graph.html')
fig = figure(title='subscriber graph',x_axis_label='channels',y_axis_label='subscribers',x_range=names)
fig.vbar(x=names, top=[x[1] for x in channels], width=0.9)

fig1 = figure(title='video count',x_axis_label='channels',y_axis_label='videos',x_range=names)
fig1.vbar(x=names, top=[x[2] for x in channels], width=0.9)

fig2 = figure(title='likes over time',x_axis_label='period',y_axis_label='likes')
figs = gridplot([[fig,fig1]])
show(figs)
conn.close()

import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

#Labels
lb = ['Media','Statistics','DataBase','Data Mining','Data Visualization','Programming','Cloud Computing','Machine Learning',  #Base Nodes 0,1,...7,
      'Video', 'Graphics',                                                                       #Media 8,9,
      'Scipy', 'Statsmodel','SAS',                                                               #Stats 10,11,12
      'MySQL','SQLServer','MongoDB',                                                             #DB 13,14,15
      'Pandas','Scikit-learn','Numpy','dplyr','IDE',                                             #DataMining 16,....,20
      'Bokeh', 'Matplotlib', 'Plotly','GIS','Tableau','PowerBI',                                 #Data Viz 21,...,26,
      'APIs','Python','R','Java/JS','HTML/CSS', 'Docker',                                        #Programming 27,...,32
      'Azure','Google Cloud',                                                                    #Cloud Comp 33,34,
      'Keras','NLTK','Tensorflow',                                                               #Machine Learning 35,...,37
      'Data Analysis', 'Software Development', 'Web Development']                                #Final Nodes 38,39,40

#'Keras','NLTK','Tensorflow','Pytorch','Scikit-learn','Scipy','numpy']                   #Machine Learning 48,...,54

    
#targets    
tg = [0,0,               #media
      1,1,1,              #Stats
      2,2,2,              #DB
      3,3,3,3,3,          #DM
      4,4,4,4,4,4,        #DViz
      5,5,5,5,5,5,    #Programming
      6,6,                #Cloud Comp
      7,7,7,7,7,7,        #ML
      38,38,38,38,38,38,39,40,40,40,38]        
            


#source
src = [8,9,                             #links media 2
     10,11,12,                          #links Stats 3
     13,14,15,                          #links DB    3
     16,17,18,19,20,                    #links DM    5
     21,22,23,24,25,26,                 #links DViz  6
     27,28,29,30,31,32,                 #links Programming 6
     33,34,                             #links Cloud Comp  2
     35,36,37,10,17,18,                 #links ML 6
     0,1,2,3,4,5,5,6,0,5,7]             #end links 11

Clink = ['#8dd3c7', '#8dd3c7',
         '#ffffb3','#ffffb3','#ffffb3',
         '#bebada','#bebada','#bebada',
         '#fb8072', '#fb8072','#fb8072','#fb8072','#fb8072',
         '#80b1d3', '#80b1d3','#80b1d3','#80b1d3','#80b1d3','#80b1d3',
         '#fdb462', '#fdb462','#fdb462','#fdb462','#fdb462','#fdb462',
         '#b3de69', '#b3de69',
         '#fccde5', '#fccde5','#fccde5','#fccde5','#fccde5','#fccde5',
         '#8dd3c7','#ffffb3','#bebada','#fb8072','#80b1d3','#fdb462','#fdb462','#b3de69','#8dd3c7','#fdb462','#fccde5']


Cnodes = ['#36afff','#36afff',
          '#36afff','#36afff','#36afff',
          '#36afff','#36afff','#36afff',
          '#000000','#000000','#000000','#000000','#000000',
          '#000000','#000000','#000000','#000000','#000000','#000000',
          '#000000','#000000','#000000','#000000','#000000','#000000',
          '#000000','#000000',
          '#000000','#000000','#000000','#000000','#000000','#000000',
          '#FF9B00','#FF9B00','#FF9B00','#FF9B00','#FF9B00','#FF9B00','#1E4785','#AE1C28', '#AE1C28','#AE1C28','#FF9B00']


vl = [1.05,2.45,                                         #values Media
     3, 3, 1.5,                                          #values Stats
     5, 3, 2,                                            #values DB
     7,2,4,2,5,                                          #values DM
     7,3,2,4,2,2,                                        #values Dviz
     4.125, 9.625, 2.75, 4.125, 5.5, 1.375,              #values programming
     4.5, 3,                                             #values Cloud
     .5, .3, 1.4,.3,.3,.3,                             #values ML
     2.5,7.5,10,20,20,10,15,7.5,1,2.5,4]
      
      
links = dict(source=src, target=tg, value=vl, color=Clink, line = dict(color = "black", width = 0.05 ))
nodes = dict(label=lb, pad=200, thickness=10, color=Cnodes)
data = go.Sankey(link=links, node=nodes,  orientation = 'h')
fig = go.Figure(data )

fig.update_layout( 
    font=dict(size = 12, color = 'black', family='verdana'),
    paper_bgcolor='white', width=1000, height=900)

fig.show()

len(lb), len(src), len(tg), len(vl)

#fig.write_image("skillsChart.svg")

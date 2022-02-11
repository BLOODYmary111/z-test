import csv
import plotly.figure_factory as ff 
import statistics
import random
import pandas as pd 
import plotly.graph_objects as go

df=pd.read_csv("newdata.csv")
data=df["average"].to_list()
population_mean=mean=statistics.mean(data)
standard_deviation=statistics.stdev(data)
print("standar deviation of population is",standard_deviation)
print("population mean is ", population_mean)

fig=ff.create_distplot([data],["average"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
fig.show()



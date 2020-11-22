from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

df=pandas.read_csv("bachelors.csv")
x=df["Year"]
y=df["Computer Science"]

output_file("Graph.html")

f=figure()
f.line(x,y)

show(f)
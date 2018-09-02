# making a basic bokeh line graph...

# importing Bokeh...
from bokeh.plotting import figure
from bokeh.io import output_file, show


# prepare some data...
# lists must have same length in order to plot them in Bokeh...cuz bokeh pairs them together...eg; x[1] and y[6] etc...
x=[1,2,3,4,5]
y=[6,7,8,9,10]

#prepare the output file...
output_file("Line.html")

#create figure object...
f=figure()

#create line plot
#f.line(x,y)
f.triangle(x,y,size=20,color="purple",alpha=0.5)
#f.circle(x,y,size=20,color="purple",alpha=0.5)

# write the plot in the figure object...
show(f)

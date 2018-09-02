"""
Plotting Weather Data (Practice)
Section 17, Lecture 191
Please produce the following graph using the data from this Excel file: http://pythonhow.com/data/verlegenhuken.xlsx

"""

import pandas
from bokeh.plotting import figure, output_file, show

# prepare some data...
# lists must have same length in order to plot them in Bokeh...cuz bokeh pairs them together...eg; x[1] and y[6] etc...
df=pandas.read_excel("verlegenhuken.xls",sheet_name=0)
df["Temperature"]=df["Temperature"]/10 # passing the columns
df["Pressure"]=df["Pressure"]/10 # passing the columns

#create figure object...
p=figure(plot_width=500,plot_height=400,tools='pan',logo=None)

p.title.text="Temperature and Air Pressure"
p.title.text_color="Gray"
p.title.text_font="arial"
p.title.text_font_style="bold"
p.xaxis.minor_tick_line_color=None
p.yaxis.minor_tick_line_color=None
p.xaxis.axis_label="Temperature (°C)"
p.yaxis.axis_label="Pressure (hPa)"

#create line plot
p.circle(df["Temperature"],df["Pressure"],size=0.5)
#prepare the output file...
output_file("weather_man.html")

# write the plot in the figure object...
show(p)

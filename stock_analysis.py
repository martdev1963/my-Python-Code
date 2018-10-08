from pandas_datareader import data
import datetime
# you can use Shift-J/K to select multiple cells and Shift-M will merge all the selected cells.
from bokeh.plotting import figure, show, output_file


start=datetime.datetime(2015,11,1)
end=datetime.datetime(2016,3,10)
# name parameter is for the company's ticker... like AAPL for Apple Inc...
# data used to build candlestick chart: High, Low, Open Close Date...
df=data.DataReader(name="GOOG",data_source="yahoo",start=start,end=end)
df

date_increase=df.index[df.Close > df.Open]
date_decrease=df.index[df.Close < df.Open]

df.Open

# function definition...the return values of this function are used to set the coordinates for the rectangle glyphs...
def inc_dec(c, o):
    if c > o:
        value="Increase"
    elif c < o:
        value="Decrease"
    else:
        value="Equal"
    return value

# creates new status column with list of data returned by function inc_dec(c,o)...
df["Status"]=[inc_dec(c,o) for c, o in zip(df.Close,df.Open)]

df["Middle"]=(df.Open+df.Close)/2  # y coordinate of rectangle...center point...
df["Height"]=abs(df.Close-df.Open) # bottom and top of rectangle...


p=figure(x_axis_type='datetime', width=1000, height=300, sizing_mode="scale_width")
p.title.text="Candlestick Chart"
#-------------------------------------------------------------------------------------------------------------------
#                                      // NEW CODE//
# Candlestick segments
# Section 20 Lecture 216    TIME: 1:36 / 5:02
# alpha factor for plot/figure object (p=figure)...how transparent you want the grid lines to appear...
# a value of zero gives you 100% transparency on the grid... (the range is between 0-1...floating point values)
#-------------------------------------------------------------------------------------------------------------------
p.grid.grid_line_alpha=0.3
#p.grid.grid_line_alpha=1
p.grid.grid_line_alpha=0
#p.grid.grid_line_alpha=1

hours_12=12*60*60*1000 # width of rectangle glyphs expressed in milliseconds along the x axis...

#-------------------------------------------------------------------------------------------------------------------
# rect() takes 4 mandatory parameters...
# x coordinate, y coordinate, 12 hour width, height
# Displaying the data using the Rectangle glyphs...
#-------------------------------------------------------------------------------------------------------------------

# segment() takes 4 mandatory parameters...
p.segment(df.index, df.High, df.index, df.Low, color="Black") # (df.index, df.High) x, y coords...
# df.index is the date column...
p.rect(df.index[df.Status=="Increase"],df.Middle[df.Status=="Increase"], hours_12,
       df.Height[df.Status=="Increase"], fill_color="#CCFFFF", line_color="black")

p.rect(df.index[df.Status=="Decrease"],df.Middle[df.Status=="Decrease"], hours_12,
       df.Height[df.Status=="Decrease"], fill_color="#FF3333", line_color="black")

output_file("cs.html")
show(p)

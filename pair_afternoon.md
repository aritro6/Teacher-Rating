
## Part 1: Plotting with matplotlib

Refer to today's [lecture files](https://github.com/zipfian/DSI_Lectures/blob/master/pandas-seaborn) for more examples. You may also find these links useful:
- [matplotlib tutorial](http://matplotlib.org/users/pyplot_tutorial.html)
- [More about matplotlib's Figure and Axes classes](http://matplotlib.org/users/artists.html)
- [Seaborn tutorial](https://web.stanford.edu/~mwaskom/software/seaborn/tutorial.html)
- [Plotting with pandas](http://pandas.pydata.org/pandas-docs/version/0.15.0/visualization.html)

Start your file with these imports
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```
If you are working in an ipython notebook, add the line
```python
%matplotlib inline
```

###### Pro tip zone
- use ```plt.title()```, ```plt.xlabel()```, and ```plt.ylabel()``` to specify axis labels and plot titles
- use ```plt.xlim()```, ```plt.ylim()```, and/or ```plt.axis()``` to change the range of values displayed on your plot. These functions take lists as arguments: ```[xmin, xmax]```, ```[ymin, ymax]```, and ```[xmin, xmax, ymin, ymax]``` respectively.

These tasks should help you get familiar with matplotlib basics:

1. The following code generates two arrays populated with integers from 0 to 999
  ```
  x1 = np.random.randint(1000, size=50)
  x2 = np.random.randint(1000, size=50)
  ```
  Make a scatterplot of x1 vs. x2, and give the points different colors based on whether or not the sum of x1 and x2 for that point is even.  

###### Pro tip zone

  The ```c``` parameter of ```plt.scatter()``` accepts an array of the same length as your data specifying a color for each point, either as a string (such as 'r' or 'b') or as a number to which a colormap is applied (you can use the  ```cmap``` keyword argument to specify which colormap to use; pick your favorite [here](http://matplotlib.org/examples/color/colormaps_reference.html)). You can even pass it an array of booleans, since ```True``` will be treated as ```1``` and ```False``` as ```0```. Very useful for dichotomously categorized data!  

2. Plot some functions
 - legends, linear, log

3. Make a bar plot with rotated labels

4. make a scatterplot with colors based on labels

5. Make a 2x2 subplot

6. Save figures

7. plot in a notebook and in a script

8. multiple line/marker styles in one plot

9. pandas
 - scatter plot
 - scattermatrix
 - histogram

10. seaborn


## Part 2: Bike Share Data

You will be exploring and graphing the data from the Bay Area Bike Share.  

Import the data and review it well enough to understand the contents.  The data directory contains a README with further explanation.
```
data/bay_area_bikeshare/README.txt
```

In order to better understand the relationships between various features of the data, you should:

1. Create a graph that is based on data from only one of the columns of the original data.  For example, this might be a histogram of that data.

2. Create a graph that is based on data from only two columns of the original data.  This might be a scatterplot, a faceted histogram, etc.

3. Create graph that is based on data from at least 3 columns of the original data.  This could be a colored scatterplot, a scatterplot matrix, faceted histograms, etc.

For each of the three parts, your goal should be to create the most interesting or insightful graph you can, given the constraints on how much data is used.  Create a separate document that explains why you find each graph insightful and/or what you learn from the results.

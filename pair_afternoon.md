
## Part 1: Plotting with matplotlib

Refer to today's [lecture files](https://github.com/zipfian/DSI_Lectures/blob/master/pandas-seaborn) for more examples. You may also find these links useful:
- [matplotlib tutorial](http://matplotlib.org/users/pyplot_tutorial.html)
- [More about matplotlib's Figure and Axes classes](http://matplotlib.org/users/artists.html)
- [Seaborn tutorial](https://web.stanford.edu/~mwaskom/software/seaborn/tutorial.html)
- [Plotting with pandas](http://pandas.pydata.org/pandas-docs/version/0.15.0/visualization.html)

Let's do some puzzles together. I'll show you a graph and a portion of the commands used to generate it, and you'll try to reproduce it.

1. Plot some fake data
2. Plot some functions
 - labels, titles, legends, linear, log
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

import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

hist_data = [snodgrass,twain]
group_labels = ['Snodgrass Writings','Mark Twain Writings']

fig = ff.create_distplot(hist_data,group_labels,bin_size=[0.005,0.005])
pyo.plot(fig)
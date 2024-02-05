import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pyscript import document
from pyscript import display

# Integer converter
def to_int(value):
    if value:
        return int(value, 10)
    else:
        return 0

# Plot reign length
def render_chart():
    plt.rc('font', size=9)
    fig, ax = plt.subplots()
    df.plot.scatter(x="start", y="span", alpha=0.35, ax=ax)
    # ax = df.plot.scatter(x="start", y="span", alpha=0.35)
    ax.set(xlabel="Year BC", ylabel="Reign length")
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top') 
    display(fig)
    chartLabel = document.querySelector('#chart p');
    chartLabel.style.display = "block";
    # hide loading dialog
    dialog = document.querySelector('dialog');
    dialog.close()

# Render csv data table
def render_table():
    pd.set_option("display.max_rows", None)
    display(df, target="df")
    tableLabel = document.querySelector('#df p');
    tableLabel.style.display = "block";

# Convert dictionary for converting digit strings to integers.
convert = dict(zip(['start', 'state', 'lord', 'span', 'notes'], [to_int, None, None, to_int, None]))

# Read table and convert digit strings to int.
df = pd.read_csv("./assets/wangbiao.csv", header=0, converters=convert)

render_chart()
render_table()
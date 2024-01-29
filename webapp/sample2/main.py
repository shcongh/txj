import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pyscript import document
from pyscript import display

# integer converter
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
    # display(fig, target="chart")
    display(fig)
    dialog = document.querySelector('dialog');
    dialog.close()
    # loading = document.querySelector('.loading');
    # loading.style.display = "none";
    chartLabel = document.querySelector('#chart p');
    chartLabel.style.display = "block";

def render_data():
    # gb_state = df.groupby('state')
    pd.set_option("display.max_rows", None)
    display(df, target="df")
    dataLabel = document.querySelector('#df p');
    dataLabel.style.display = "block";

# Convert dictionary for converting digit strings to integers.
convert = dict(zip(['start', 'state', 'lord', 'span', 'notes'], [to_int, None, None, to_int, None]))

# Read table and convert digit strings to int.
df = pd.read_csv("./assets/wangbiao.csv", header=0, converters=convert)

# plt.rcParams['font.sans-serif'] = ['SimHei'] # Or any other Chinese characters
# plt.rcParams['font.family'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

render_chart()
render_data()
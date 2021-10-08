import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
height = df["Avg Rating"].tolist()

figure = ff.create_distplot([height],["Average Rating"],show_hist = False)
figure.show()
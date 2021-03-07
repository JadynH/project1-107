import pandas as pd
import csv
import plotly.graph_objects as boo
df = pd.read_csv("data.csv")
student_df = df.loc[df['student_id'] == "TRL_mno"] 

print(student_df.groupby("level") ["attempt"].mean()) 

fig = boo.Figure(boo.Scatter(
            x= student_df.groupby("level") ["attempt"].mean(), 
            y= ['level 1', 'level 2', 'level 3', 'level 4'],
            orientation = 'h'
))
fig.show()

import plotly.graph_objects as go
import random

# Generate 20 random numbers
random_numbers = [random.randint(1, 100) for _ in range(20)]

# Create a table
table = go.Figure(data=[go.Table(header=dict(values=['Numbers']),
                 cells=dict(values=[random_numbers]))])

table.show()

# Create a line graph
line_graph = go.Figure(data=go.Scatter(x=list(range(1, 21)), y=random_numbers, mode='lines+markers'))

line_graph.show()
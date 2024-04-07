import plotly.graph_objects as go
import random

# Generate 20 números aleatoris
random_numbers = [random.randint(1, 100) for _ in range(20)]

# Crea una línia de gràfic amb els números aleatoris
line_graph = go.Figure(data=go.Scatter(x=list(range(1, 21)), y=random_numbers, mode='lines+markers'))

line_graph.show()
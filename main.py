import random

import plotly
import plotly.graph_objects as go

# Defining the dimensions of world and number of frames
DIM = 150
NUM_FRAMES = 1000
INIT_STATE = [[random.choice([0, 1])
               for _ in range(DIM)] for _ in range(DIM)]


class World:
    """Environment for the game"""

    def __init__(self, state):
        self.state = state

    def getActiveNeighbors(self, col, row):
        res = 0
        if col-1 >= 0:
            res += self.state[col-1][row]
        if col+1 < DIM:
            res += self.state[col+1][row]
        if row-1 >= 0:
            res += self.state[col][row-1]
        if row+1 < DIM:
            res += self.state[col][row+1]
        if col-1 >= 0 and row-1 >= 0:
            res += self.state[col-1][row-1]
        if col-1 >= 0 and row+1 < DIM:
            res += self.state[col-1][row+1]
        if col+1 < DIM and row-1 >= 0:
            res += self.state[col+1][row-1]
        if col+1 < DIM and row+1 < DIM:
            res += self.state[col+1][row+1]
        return res

    def update(self):
        newstate = [[0 for _ in range(DIM)] for _ in range(DIM)]
        for col in range(DIM):
            for row in range(DIM):
                numNeighbors = self.getActiveNeighbors(col, row)
                selfState = self.state[col][row]
                if (numNeighbors < 2 or numNeighbors > 3) and selfState:
                    newstate[col][row] = 0
                elif numNeighbors == 3 and not selfState:
                    newstate[col][row] = 1
                else:
                    newstate[col][row] = self.state[col][row]
        self.state = newstate

    def getState(self):
        return self.state


# World
world = World(INIT_STATE)
frames = []
for i in range(NUM_FRAMES):
    frames.append(world.getState())
    world.update()
fig = go.Figure(data=[go.Heatmap(z=frames[0],
                                 colorscale='gray', reversescale=True,
                                 showscale=False,
                                 zmin=0, zmax=1, hoverinfo='skip')],
                layout=go.Layout(xaxis=dict(visible=False),
                                 yaxis=dict(visible=False),
                                 margin=dict(t=20, l=325, r=325, b=20),
                                 height=750,
                                 width=1400,
                                 updatemenus=[dict(
                                     type="buttons",
                                     buttons=[dict(label="Play",
                                                   method="animate",
                                                   args=[None])])]
                                 ),
                frames=[go.Frame(data=[go.Heatmap(z=f,
                                                  colorscale='gray',
                                                  reversescale=True,
                                                  showscale=False,
                                                  zmin=0, zmax=1,
                                                  hoverinfo='skip')]) for f in frames[1:]])

plotly.offline.plot(fig, filename="simulation.html",
                    auto_open=False, auto_play=False)

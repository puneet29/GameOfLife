# Conway's Game of Life

This is an attempt to simulate the [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). Game of Life is a cellular automaton which was devised by John Conway, a British Mathematician. The beauty of patterns that emerge from a simple condition on birth and death of each cell is truly amazing. This is just randomly initialized world which slowly forms the still lifeforms, oscillators, and spaceships.

## How to run

1. Install python.

2. Install dependencies using `pip install -r requirements.txt`

3. Run the main.py file: `python main.py`. Options available

    - `DIM`: Dimensions of the grid world. (DIM x DIM)
    - `NUM_FRAMES`: Number of frames that will be generated for the simulation.
    - `INIT_STATE`: Initial state of each cell in the grid world. (0 dead, 1 alive)

4. Run the simulation on your browser from the file `simulation.html`

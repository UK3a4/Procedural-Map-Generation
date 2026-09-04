V0.1 Initial heightmap prototype

Goal
    Create my first procedural heightmap and experiment with making neighboring cells more similar.

What I implemented
    Generated 2D heightmap using NumPy.
    Added a seed so the same input seed produces the same heightmap.
    Implemented basic 2x2 neighborhood averaging.
    Visualized the result with Matplotlib.

What I learned
    Basic principles of working with NumPy.
    How to make heightmap more smooth by averaging neighboring cells.

Next question
    How can I generate values directly, instead of generating random numbers and smoothing them afterward?


V0.2 Neighbor--dependent heightmap

Goal
    Experiment with generating a heightmap where neighboring cells influence each others.

What I Changed
    Reworked heightmap generation system from full random values to a system where neighboring cells influence each others.
    Added a random cooficent in the range 0.8 - 1.2 to introduce variation
    Added an amplitude parametr to control height range.

What I learned
    For each cell i calculate an average of the available neighboring values then apply a small random variation.
    This creates a much better, smooth, natural looking terrain heightmap.

Next question
    How can I prevent the gradual/decay while keeping the local variation and spatial continuity?
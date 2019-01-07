# gridpit

= a playground for route finding algorithms. Where a grid is used to represent and visualise some networks.

## Features:
* grid pit
* random walk
* A Star route finding

## To Do:
* improve viz - formalise grid and agent interaction methods (ie grid_update_background, agent_update, grid_update_fore())
* add grid maze - ie more complex randomised nets
* sim some more complex nets, ie mazes
* sim some more complex nets, add some weights
* try some other algs
* try some ML, maybe just a perceptron?
* make testing and comparison framework ie PIT

## Structure:
* CANVAS - viz layers for grid background, agent update, grid foreground (ie obstructions)
* GRID - generation and representation of network structure with start, goal and obstruction nodes
* AGENTS - navigates the grid
* PIT - object for testing various agents on given grids
